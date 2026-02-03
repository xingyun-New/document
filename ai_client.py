"""
AI客户端
支持多种AI服务提供商
"""
import json
import requests
from typing import Dict, Any, Optional
from datetime import datetime
from loguru import logger


class AIClient:
    """AI客户端基类"""
    
    def __init__(self, api_key: str, api_base: str, model: str = "qwen-plus"):
        """
        初始化AI客户端
        
        Args:
            api_key: API密钥
            api_base: API基础URL
            model: 模型名称
        """
        self.api_key = api_key
        self.api_base = api_base
        self.model = model
    
    def chat(self, messages: str, **kwargs) -> str:
        """
        发送聊天请求
        
        Args:
            messages: 消息内容
            **kwargs: 其他参数
            
        Returns:
            AI响应文本
        """
        raise NotImplementedError("子类必须实现chat方法")


class DashScopeClient(AIClient):
    """阿里云通义千问客户端"""
    
    def __init__(self, api_key: str, model: str = "qwen3-max-preview", timeout: int = 60):
        """
        初始化通义千问客户端
        
        Args:
            api_key: API密钥
            model: 模型名称
            timeout: 超时时间（秒）
        """
        api_base = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
        super().__init__(api_key, api_base, model)
        self.timeout = timeout
        self.last_usage = None  # 保存最后一次调用的token使用情况
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def chat(self, messages, **kwargs) -> str:
        """
        发送聊天请求到通义千问
        
        Args:
            messages: 消息内容（可以是字符串或消息列表）
            **kwargs: 其他参数
            
        Returns:
            AI响应文本
        """
        try:
            # 处理messages参数
            # 如果messages已经是列表格式（标准OpenAI格式），直接使用
            if isinstance(messages, list):
                formatted_messages = messages
            else:
                # 否则当作单个user消息
                formatted_messages = [
                    {
                        "role": "user",
                        "content": str(messages)
                    }
                ]
            
            # 构建请求数据
            data = {
                "model": self.model,
                "messages": formatted_messages,
                "temperature": kwargs.get("temperature", 0.3),
                "top_p": kwargs.get("top_p", 1.0),
                "max_tokens": kwargs.get("max_tokens", 6000),
                "frequency_penalty": kwargs.get("frequency_penalty", 0),
                "presence_penalty": kwargs.get("presence_penalty", 0)
            }
            
            # 发送请求
            response = requests.post(
                self.api_base,
                headers=self.headers,
                json=data,
                timeout=self.timeout
            )
            
            # 检查响应
            if not response.ok:
                error_detail = ""
                try:
                    error_json = response.json()
                    error_detail = error_json.get('message', error_json.get('error', str(error_json)))
                except:
                    error_detail = response.text[:200]
                
                logger.error(f"AI请求失败 (状态码: {response.status_code})")
                logger.error(f"错误详情: {error_detail}")
                logger.error(f"请求模型: {self.model}")
                logger.error(f"API Base: {self.api_base}")
                raise requests.exceptions.HTTPError(f"{response.status_code}: {error_detail}")
            
            result = response.json()
            
            # 保存token使用情况
            if "usage" in result:
                self.last_usage = {
                    'prompt_tokens': result["usage"].get("prompt_tokens", 0),
                    'completion_tokens': result["usage"].get("completion_tokens", 0),
                    'total_tokens': result["usage"].get("total_tokens", 0)
                }
            else:
                self.last_usage = None
            
            # 提取回复内容
            if "choices" in result and len(result["choices"]) > 0:
                content = result["choices"][0]["message"]["content"]
                logger.info(f"AI响应成功，长度: {len(content)}, tokens: {self.last_usage}")
                return content
            else:
                logger.error(f"AI响应格式异常: {result}")
                raise ValueError("AI响应格式异常")
                
        except requests.exceptions.RequestException as e:
            logger.error(f"AI请求失败: {str(e)}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"AI响应解析失败: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"AI调用异常: {str(e)}")
            raise


class OpenAIClient(AIClient):
    """OpenAI客户端"""
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo", timeout: int = 60):
        """
        初始化OpenAI客户端
        
        Args:
            api_key: API密钥
            model: 模型名称
            timeout: 超时时间（秒）
        """
        api_base = "https://api.openai.com/v1/chat/completions"
        super().__init__(api_key, api_base, model)
        self.timeout = timeout
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def chat(self, messages: str, **kwargs) -> str:
        """
        发送聊天请求到OpenAI
        
        Args:
            messages: 消息内容
            **kwargs: 其他参数
            
        Returns:
            AI响应文本
        """
        try:
            # 构建请求数据
            data = {
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": messages
                    }
                ],
                "temperature": kwargs.get("temperature", 0.3),
                "top_p": kwargs.get("top_p", 1.0),
                "max_tokens": kwargs.get("max_tokens", 6000),
                "frequency_penalty": kwargs.get("frequency_penalty", 0),
                "presence_penalty": kwargs.get("presence_penalty", 0)
            }
            
            # 发送请求
            response = requests.post(
                self.api_base,
                headers=self.headers,
                json=data,
                timeout=self.timeout
            )
            
            # 检查响应
            response.raise_for_status()
            result = response.json()
            
            # 提取回复内容
            if "choices" in result and len(result["choices"]) > 0:
                content = result["choices"][0]["message"]["content"]
                logger.info(f"OpenAI响应成功，长度: {len(content)}")
                return content
            else:
                logger.error(f"OpenAI响应格式异常: {result}")
                raise ValueError("OpenAI响应格式异常")
                
        except requests.exceptions.RequestException as e:
            logger.error(f"OpenAI请求失败: {str(e)}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"OpenAI响应解析失败: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"OpenAI调用异常: {str(e)}")
            raise


class AIClientFactory:
    """AI客户端工厂"""
    
    @staticmethod
    def create_client(provider: str, api_key: str, **kwargs) -> AIClient:
        """
        创建AI客户端
        
        Args:
            provider: 服务提供商 (dashscope/openai)
            api_key: API密钥
            **kwargs: 其他参数
            
        Returns:
            AI客户端实例
        """
        if provider.lower() == "dashscope":
            model = kwargs.get("model", "qwen-plus")
            return DashScopeClient(api_key, model)
        elif provider.lower() == "openai":
            model = kwargs.get("model", "gpt-3.5-turbo")
            return OpenAIClient(api_key, model)
        else:
            raise ValueError(f"不支持的AI服务提供商: {provider}")


def main():
    """测试函数"""
    print("=== AI客户端测试 ===\n")
    
    # 测试通义千问客户端
    try:
        # 从配置文件读取配置
        with open("config/ai_prompts.json", 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        model_config = config.get("model_config", {})
        api_key = model_config.get("api_key")
        api_base = model_config.get("api_base")
        model = model_config.get("default_model", "qwen-plus")
        
        if api_key and api_base:
            print("使用通义千问客户端测试...")
            client = DashScopeClient(api_key, model)
            
            # 简单测试
            test_message = "你好，请简单介绍一下自己"
            response = client.chat(test_message)
            print(f"AI回复: {response[:100]}...")
        else:
            print("AI配置不完整，跳过测试")
    
    except Exception as e:
        print(f"测试失败: {str(e)}")


if __name__ == "__main__":
    main()

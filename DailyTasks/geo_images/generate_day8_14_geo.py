# -*- coding: utf-8 -*-
"""
生成Day8-Day14几何图形
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, Arc
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def setup_figure(figsize=(6, 6)):
    """设置图形基础"""
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax

def add_point_label(ax, x, y, label, offset=(0.1, 0.1), fontsize=14):
    """添加点标签"""
    ax.plot(x, y, 'ko', markersize=5)
    ax.annotate(label, (x, y), xytext=(x + offset[0], y + offset[1]), fontsize=fontsize, fontweight='bold')

def draw_line(ax, p1, p2, color='black', linewidth=1.5):
    """画线段"""
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, linewidth=linewidth)

def draw_angle_mark(ax, vertex, p1, p2, radius=0.3, color='blue'):
    """画角标记"""
    angle1 = np.arctan2(p1[1] - vertex[1], p1[0] - vertex[0]) * 180 / np.pi
    angle2 = np.arctan2(p2[1] - vertex[1], p2[0] - vertex[0]) * 180 / np.pi
    arc = Arc(vertex, radius*2, radius*2, angle=0, theta1=min(angle1, angle2), theta2=max(angle1, angle2), color=color)
    ax.add_patch(arc)

def draw_right_angle(ax, vertex, p1, p2, size=0.2):
    """画直角标记"""
    v1 = np.array(p1) - np.array(vertex)
    v2 = np.array(p2) - np.array(vertex)
    v1 = v1 / np.linalg.norm(v1) * size
    v2 = v2 / np.linalg.norm(v2) * size
    corner = np.array(vertex) + v1 + v2
    ax.plot([vertex[0] + v1[0], corner[0]], [vertex[1] + v1[1], corner[1]], 'b-', linewidth=1)
    ax.plot([corner[0], vertex[0] + v2[0]], [corner[1], vertex[1] + v2[1]], 'b-', linewidth=1)

# ================== Day8 几何图形 ==================

def day8_geo_01():
    """8字型模型 - OA=OC, OB=OD"""
    fig, ax = setup_figure()
    O = (0, 0)
    A = (0, 2)
    B = (-1.5, -0.5)
    C = (0, -2)
    D = (1.5, 0.5)
    
    draw_line(ax, A, B)
    draw_line(ax, A, D)
    draw_line(ax, C, B)
    draw_line(ax, C, D)
    draw_line(ax, A, C)
    draw_line(ax, B, D)
    
    add_point_label(ax, *O, 'O', (0.1, 0.1))
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, 0))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, 0))
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    plt.savefig('day8_geo_01.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day8_geo_02():
    """K字型模型 - AB∥CD"""
    fig, ax = setup_figure()
    A = (-2, 2)
    B = (2, 2)
    C = (2, -2)
    D = (-2, -2)
    O = (0, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, D, C)
    draw_line(ax, A, C)
    draw_line(ax, B, D)
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.4, -0.3))
    add_point_label(ax, *O, 'O', (0.1, 0.1))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 3.5)
    plt.savefig('day8_geo_02.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day8_geo_03():
    """沙漏型模型"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-1.5, 1)
    C = (0, -1)
    D = (1.5, 1)
    E = (0, -3)
    
    draw_line(ax, A, B)
    draw_line(ax, A, D)
    draw_line(ax, B, C)
    draw_line(ax, D, C)
    draw_line(ax, C, E)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, 0))
    add_point_label(ax, *C, 'C', (0.2, 0))
    add_point_label(ax, *D, 'D', (0.1, 0))
    add_point_label(ax, *E, 'E', (0.1, -0.3))
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-4, 4)
    plt.savefig('day8_geo_03.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day8_geo_04():
    """四边形ABCD, AB=CD, AD=CB"""
    fig, ax = setup_figure()
    A = (0, 2)
    B = (3, 2)
    C = (3, 0)
    D = (0, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, C, D)
    draw_line(ax, D, A)
    draw_line(ax, B, D, color='blue', linewidth=1)
    
    add_point_label(ax, *A, 'A', (-0.3, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.3, -0.3))
    
    ax.set_xlim(-1, 4.5)
    ax.set_ylim(-1, 3.5)
    plt.savefig('day8_geo_04.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day8_geo_05():
    """等腰三角形ABC, AB=AC, D是BC中点"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (0, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, A, D, color='blue', linewidth=1)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, -0.4))
    
    draw_right_angle(ax, D, A, C)
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day8_geo_05.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# ================== Day9 几何图形 ==================

def day9_geo_01():
    """角的拼凑 - ∠1=∠2, 加同角"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (0, 1.5)
    E = (-1, 0)
    F = (1, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, A, D)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.2, 0))
    
    # 标注角1和角2
    ax.annotate('1', (-0.3, 2.3), fontsize=12, color='red')
    ax.annotate('2', (0.3, 2.3), fontsize=12, color='red')
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day9_geo_01.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_geo_02():
    """截长补短 - 在长边上截取"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (-1.2, 1.2)  # AB上的点
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, D, C, color='blue', linewidth=1)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.4, 0.1))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day9_geo_02.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_geo_03():
    """隐藏条件 - 中点、垂直"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (0, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, A, D, color='blue', linewidth=1.5)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, -0.4))
    
    # 中点标记
    ax.plot(-1, 0, 'b|', markersize=10)
    ax.plot(1, 0, 'b|', markersize=10)
    
    draw_right_angle(ax, D, A, C)
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day9_geo_03.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# ================== Day10 几何图形 ==================

def day10_geo_01():
    """等腰三角形 - 三线合一"""
    fig, ax = setup_figure()
    A = (0, 3.5)
    B = (-2.5, 0)
    C = (2.5, 0)
    D = (0, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, A, D, color='blue', linewidth=1.5)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, -0.4))
    
    draw_right_angle(ax, D, A, C, size=0.25)
    
    # 等边标记
    ax.annotate('', xy=(-1, 1.75), xytext=(-1.5, 1.75),
                arrowprops=dict(arrowstyle='-', color='red'))
    ax.annotate('', xy=(1, 1.75), xytext=(1.5, 1.75),
                arrowprops=dict(arrowstyle='-', color='red'))
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 4.5)
    plt.savefig('day10_geo_01.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day10_geo_02():
    """等腰三角形 + 全等综合"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (0, 0)
    E = (-1.2, 1.2)
    F = (1.2, 1.2)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, B, E, color='blue')
    draw_line(ax, C, F, color='blue')
    draw_line(ax, E, F, color='green', linewidth=1)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *E, 'E', (-0.4, 0.1))
    add_point_label(ax, *F, 'F', (0.1, 0.1))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day10_geo_02.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# ================== Day11 几何图形 ==================

def day11_geo_01():
    """直角三角形 - 斜边中线"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (0, 0)
    C = (4, 0)
    D = (2, 1.5)  # 斜边中点
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, A, C)
    draw_line(ax, B, D, color='blue', linewidth=1.5)
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, 0.1))
    
    draw_right_angle(ax, B, A, C, size=0.3)
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 4)
    plt.savefig('day11_geo_01.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day11_geo_02():
    """勾股定理 - 3,4,5直角三角形"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (0, 0)
    C = (4, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, A, C)
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    
    draw_right_angle(ax, B, A, C, size=0.3)
    
    # 标注边长
    ax.annotate('3', (-0.5, 1.5), fontsize=12, color='blue')
    ax.annotate('4', (2, -0.5), fontsize=12, color='blue')
    ax.annotate('5', (2.5, 2), fontsize=12, color='red')
    
    ax.set_xlim(-1.5, 5)
    ax.set_ylim(-1, 4)
    plt.savefig('day11_geo_02.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day11_geo_03():
    """HL判定"""
    fig, ax = setup_figure((8, 4))
    
    # 第一个直角三角形
    A1 = (0, 2.5)
    B1 = (0, 0)
    C1 = (2, 0)
    
    draw_line(ax, A1, B1)
    draw_line(ax, B1, C1)
    draw_line(ax, A1, C1)
    draw_right_angle(ax, B1, A1, C1, size=0.2)
    
    add_point_label(ax, *A1, 'A', (-0.3, 0.1))
    add_point_label(ax, *B1, 'B', (-0.3, -0.25))
    add_point_label(ax, *C1, 'C', (0.1, -0.25))
    
    # 第二个直角三角形
    D = (4, 2.5)
    E = (4, 0)
    F = (6, 0)
    
    draw_line(ax, D, E)
    draw_line(ax, E, F)
    draw_line(ax, D, F)
    draw_right_angle(ax, E, D, F, size=0.2)
    
    add_point_label(ax, *D, 'D', (-0.3, 0.1))
    add_point_label(ax, *E, 'E', (-0.3, -0.25))
    add_point_label(ax, *F, 'F', (0.1, -0.25))
    
    ax.set_xlim(-1, 7)
    ax.set_ylim(-0.8, 3.5)
    plt.savefig('day11_geo_03.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# ================== Day12 几何图形 ==================

def day12_geo_01():
    """倍长中线"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (0, 0)
    E = (0, -3)  # 倍长后的点
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, A, E, color='blue', linewidth=1.5)
    draw_line(ax, B, E, color='green', linewidth=1)
    draw_line(ax, C, E, color='green', linewidth=1)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, 0.1))
    add_point_label(ax, *C, 'C', (0.1, 0.1))
    add_point_label(ax, *D, 'D', (0.15, 0.1))
    add_point_label(ax, *E, 'E', (0.1, -0.3))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-4, 4)
    plt.savefig('day12_geo_01.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day12_geo_02():
    """作垂线"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2.5, 0)
    C = (2.5, 0)
    H = (0, 0)  # 垂足
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, A, H, color='blue', linewidth=1.5)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *H, 'H', (0.1, -0.4))
    
    draw_right_angle(ax, H, A, C, size=0.25)
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 4)
    plt.savefig('day12_geo_02.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day12_geo_03():
    """作平行线"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (0, 1.5)  # BC中点到A的中点
    E = (-1, 1.5)  # 平行线
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, D, E, color='blue', linewidth=1.5)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.15, 0.1))
    add_point_label(ax, *E, 'E', (-0.4, 0.1))
    
    # 平行标记
    ax.annotate('∥', (0.5, 0.7), fontsize=14, color='blue')
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day12_geo_03.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# ================== Day13 几何图形 ==================

def day13_geo_01():
    """平面直角坐标系"""
    fig, ax = setup_figure()
    
    # 画坐标轴
    ax.annotate('', xy=(4, 0), xytext=(-4, 0),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.annotate('', xy=(0, 4), xytext=(0, -4),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    # 标注
    ax.annotate('x', (3.8, -0.4), fontsize=14)
    ax.annotate('y', (0.2, 3.8), fontsize=14)
    ax.annotate('O', (-0.4, -0.4), fontsize=14)
    
    # 象限标注
    ax.annotate('第一象限\n(+,+)', (1.5, 2), fontsize=10, ha='center')
    ax.annotate('第二象限\n(-,+)', (-2, 2), fontsize=10, ha='center')
    ax.annotate('第三象限\n(-,-)', (-2, -2), fontsize=10, ha='center')
    ax.annotate('第四象限\n(+,-)', (1.5, -2), fontsize=10, ha='center')
    
    # 画网格
    for i in range(-3, 4):
        ax.axhline(y=i, color='lightgray', linewidth=0.5, zorder=0)
        ax.axvline(x=i, color='lightgray', linewidth=0.5, zorder=0)
    
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4.5, 4.5)
    plt.savefig('day13_geo_01.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day13_geo_02():
    """点的对称"""
    fig, ax = setup_figure()
    
    # 画坐标轴
    ax.annotate('', xy=(4, 0), xytext=(-4, 0),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.annotate('', xy=(0, 4), xytext=(0, -4),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    ax.annotate('x', (3.8, -0.3), fontsize=12)
    ax.annotate('y', (0.15, 3.8), fontsize=12)
    ax.annotate('O', (-0.35, -0.35), fontsize=12)
    
    # 画点
    P = (2, 3)
    P1 = (2, -3)  # 关于x轴对称
    P2 = (-2, 3)  # 关于y轴对称
    P3 = (-2, -3)  # 关于原点对称
    
    ax.plot(*P, 'ro', markersize=8)
    ax.plot(*P1, 'bo', markersize=8)
    ax.plot(*P2, 'go', markersize=8)
    ax.plot(*P3, 'mo', markersize=8)
    
    ax.annotate('P(2,3)', (P[0]+0.2, P[1]+0.2), fontsize=10, color='red')
    ax.annotate("P'(2,-3)\n关于x轴", (P1[0]+0.2, P1[1]-0.5), fontsize=9, color='blue')
    ax.annotate("P''(-2,3)\n关于y轴", (P2[0]-1.2, P2[1]+0.2), fontsize=9, color='green')
    ax.annotate("P'''(-2,-3)\n关于原点", (P3[0]-1.2, P3[1]-0.5), fontsize=9, color='purple')
    
    # 画网格
    for i in range(-3, 4):
        ax.axhline(y=i, color='lightgray', linewidth=0.5, zorder=0)
        ax.axvline(x=i, color='lightgray', linewidth=0.5, zorder=0)
    
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4.5, 4.5)
    plt.savefig('day13_geo_02.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# ================== 习题集图形 ==================

def exercise_8_fig_01():
    """Day8习题 - 四边形ABCD"""
    fig, ax = setup_figure()
    A = (0, 2)
    B = (3, 2)
    C = (3, 0)
    D = (0, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, C, D)
    draw_line(ax, D, A)
    draw_line(ax, A, C, color='blue', linewidth=1)
    draw_line(ax, B, D, color='blue', linewidth=1)
    
    add_point_label(ax, *A, 'A', (-0.3, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.3, -0.3))
    
    ax.set_xlim(-1, 4.5)
    ax.set_ylim(-1, 3.5)
    plt.savefig('exercise8_fig01.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def exercise_8_fig_02():
    """Day8习题 - 8字型"""
    fig, ax = setup_figure()
    O = (0, 0)
    A = (-1.5, 2)
    B = (1.5, 1)
    C = (1.5, -2)
    D = (-1.5, -1)
    
    draw_line(ax, A, B)
    draw_line(ax, A, D)
    draw_line(ax, C, B)
    draw_line(ax, C, D)
    
    add_point_label(ax, *O, 'O', (0.1, 0.1))
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.4, -0.3))
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    plt.savefig('exercise8_fig02.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def exercise_10_fig_01():
    """Day10习题 - 等腰三角形BD⊥AC, CE⊥AB"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (1.2, 1.8)  # AC上的点
    E = (-1.2, 1.8)  # AB上的点
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, B, D, color='blue')
    draw_line(ax, C, E, color='blue')
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.15, 0.1))
    add_point_label(ax, *E, 'E', (-0.4, 0.1))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('exercise10_fig01.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def exercise_11_fig_01():
    """Day11习题 - 直角三角形30度角"""
    fig, ax = setup_figure()
    A = (0, 0)
    B = (4, 0)
    C = (0, 4*np.tan(np.radians(30)))
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, A, C)
    
    add_point_label(ax, *A, 'A', (-0.3, -0.3))
    add_point_label(ax, *B, 'B', (0.1, -0.3))
    add_point_label(ax, *C, 'C', (-0.4, 0.1))
    
    draw_right_angle(ax, A, C, B, size=0.3)
    
    # 标注30度
    ax.annotate('30°', (3.2, 0.3), fontsize=12, color='blue')
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 3.5)
    plt.savefig('exercise11_fig01.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def exercise_12_fig_01():
    """Day12习题 - 平行四边形"""
    fig, ax = setup_figure()
    A = (0, 2)
    B = (3, 2)
    C = (4, 0)
    D = (1, 0)
    E = (1.5, 2)  # BC上的点
    F = (2.5, 0)  # AD上的点
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, C, D)
    draw_line(ax, D, A)
    draw_line(ax, A, E, color='blue')
    draw_line(ax, C, F, color='blue')
    
    add_point_label(ax, *A, 'A', (-0.3, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.3, -0.3))
    add_point_label(ax, *E, 'E', (0.1, 0.15))
    add_point_label(ax, *F, 'F', (0.1, -0.35))
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 3.5)
    plt.savefig('exercise12_fig01.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# 主函数
def main():
    print("Generating Day8-Day14 geometry figures...")
    
    # Day8图形
    print("Generating Day8 figures...")
    day8_geo_01()
    day8_geo_02()
    day8_geo_03()
    day8_geo_04()
    day8_geo_05()
    
    # Day9图形
    print("Generating Day9 figures...")
    day9_geo_01()
    day9_geo_02()
    day9_geo_03()
    
    # Day10图形
    print("Generating Day10 figures...")
    day10_geo_01()
    day10_geo_02()
    
    # Day11图形
    print("Generating Day11 figures...")
    day11_geo_01()
    day11_geo_02()
    day11_geo_03()
    
    # Day12图形
    print("Generating Day12 figures...")
    day12_geo_01()
    day12_geo_02()
    day12_geo_03()
    
    # Day13图形
    print("Generating Day13 figures...")
    day13_geo_01()
    day13_geo_02()
    
    # 习题集图形
    print("Generating exercise figures...")
    exercise_8_fig_01()
    exercise_8_fig_02()
    exercise_10_fig_01()
    exercise_11_fig_01()
    exercise_12_fig_01()
    
    print("All figures generated successfully!")

if __name__ == "__main__":
    main()


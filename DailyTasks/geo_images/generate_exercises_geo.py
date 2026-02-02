# -*- coding: utf-8 -*-
"""
Generate geometry figures for Day9-Day14 exercise sets
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Arc
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def setup_figure(figsize=(6, 6)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax

def add_point_label(ax, x, y, label, offset=(0.1, 0.1), fontsize=14):
    ax.plot(x, y, 'ko', markersize=5)
    ax.annotate(label, (x, y), xytext=(x + offset[0], y + offset[1]), fontsize=fontsize, fontweight='bold')

def draw_line(ax, p1, p2, color='black', linewidth=1.5):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, linewidth=linewidth)

def draw_right_angle(ax, vertex, p1, p2, size=0.2):
    v1 = np.array(p1) - np.array(vertex)
    v2 = np.array(p2) - np.array(vertex)
    v1 = v1 / np.linalg.norm(v1) * size
    v2 = v2 / np.linalg.norm(v2) * size
    corner = np.array(vertex) + v1 + v2
    ax.plot([vertex[0] + v1[0], corner[0]], [vertex[1] + v1[1], corner[1]], 'b-', linewidth=1)
    ax.plot([corner[0], vertex[0] + v2[0]], [corner[1], vertex[1] + v2[1]], 'b-', linewidth=1)

# ================== Day9 Exercises ==================

def day9_ex_04():
    """AB//CD, AB=CD, E is intersection"""
    fig, ax = setup_figure()
    A, B = (-2, 2), (2, 2)
    D, C = (-2, -2), (2, -2)
    E = (0, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, D, C)
    draw_line(ax, A, E)
    draw_line(ax, E, C)
    draw_line(ax, B, E)
    draw_line(ax, E, D)
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.4, -0.3))
    add_point_label(ax, *E, 'E', (0.15, 0.1))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 3.5)
    plt.savefig('day9_ex_04.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_07():
    """Angle BAC = DAC, angle B = D"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (0, 0)
    D = (2, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, A, D)
    draw_line(ax, B, C)
    draw_line(ax, C, D)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.4))
    add_point_label(ax, *D, 'D', (0.1, -0.3))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day9_ex_07.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_09():
    """AB perp BD, CD perp BD"""
    fig, ax = setup_figure()
    A = (0, 2.5)
    B = (0, 0)
    C = (4, 2.5)
    D = (4, 0)
    E = (2, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, D)
    draw_line(ax, D, C)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, 0.1))
    add_point_label(ax, *D, 'D', (0.1, -0.3))
    
    draw_right_angle(ax, B, A, D, size=0.25)
    draw_right_angle(ax, D, B, C, size=0.25)
    
    ax.set_xlim(-1, 5.5)
    ax.set_ylim(-1, 3.5)
    plt.savefig('day9_ex_09.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_10():
    """angle 1 = 2, angle 3 = 4"""
    fig, ax = setup_figure()
    A = (0, 0)
    B = (4, 0)
    C = (3, 2)
    D = (1, 2)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, A, D)
    draw_line(ax, B, C)
    draw_line(ax, B, D)
    
    add_point_label(ax, *A, 'A', (-0.4, -0.3))
    add_point_label(ax, *B, 'B', (0.1, -0.3))
    add_point_label(ax, *C, 'C', (0.1, 0.1))
    add_point_label(ax, *D, 'D', (-0.4, 0.1))
    
    ax.annotate('1', (0.6, 0.3), fontsize=11, color='red')
    ax.annotate('2', (0.3, 0.6), fontsize=11, color='red')
    ax.annotate('3', (3.4, 0.3), fontsize=11, color='blue')
    ax.annotate('4', (3.1, 0.6), fontsize=11, color='blue')
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 3)
    plt.savefig('day9_ex_10.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_11():
    """ACB = DEB = 90"""
    fig, ax = setup_figure()
    A = (0, 0)
    B = (4, 0)
    C = (1.5, 0)
    D = (2.5, 2)
    E = (2.5, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, C, D)
    draw_line(ax, B, D)
    draw_line(ax, D, E)
    draw_line(ax, A, D)
    
    add_point_label(ax, *A, 'A', (-0.3, -0.3))
    add_point_label(ax, *B, 'B', (0.1, -0.3))
    add_point_label(ax, *C, 'C', (0, -0.4))
    add_point_label(ax, *D, 'D', (0.1, 0.1))
    add_point_label(ax, *E, 'E', (0.1, -0.4))
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 3)
    plt.savefig('day9_ex_11.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_31():
    """AB//CD, AB=CD"""
    fig, ax = setup_figure()
    A, B = (-2, 2), (1, 2)
    D, C = (-1, -1), (2, -1)
    E = (0, 0.5)
    
    draw_line(ax, A, B)
    draw_line(ax, D, C)
    draw_line(ax, A, E)
    draw_line(ax, E, C)
    draw_line(ax, B, E)
    draw_line(ax, E, D)
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.4, -0.3))
    add_point_label(ax, *E, 'E', (0.15, 0.1))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-2.5, 3.5)
    plt.savefig('day9_ex_31.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_35():
    """ACB=ADB=90, AC=AD"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (0, 0)
    C = (-1.5, 1.5)
    D = (1.5, 1.5)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, A, D)
    draw_line(ax, B, C)
    draw_line(ax, B, D)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (0.1, -0.3))
    add_point_label(ax, *C, 'C', (-0.4, 0))
    add_point_label(ax, *D, 'D', (0.15, 0))
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 4)
    plt.savefig('day9_ex_35.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# ================== Day10 Exercises ==================

def day10_ex_08():
    """Isosceles ABC, BD perp AC"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (1, 1.5)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, B, D, color='blue')
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.15, 0.1))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day10_ex_08.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day10_ex_10():
    """AB=AC, D,E on BC, BD=CE"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2.5, 0)
    C = (2.5, 0)
    D = (-1, 0)
    E = (1, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, A, D, color='blue')
    draw_line(ax, A, E, color='blue')
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.1, -0.4))
    add_point_label(ax, *E, 'E', (0.1, -0.4))
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 4)
    plt.savefig('day10_ex_10.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day10_ex_23():
    """BD=BC=AD"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (-0.6, 1.2)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, B, D, color='blue')
    draw_line(ax, D, C, color='blue')
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.4, 0.1))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day10_ex_23.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day10_ex_25():
    """Isosceles, D is midpoint"""
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
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 4.5)
    plt.savefig('day10_ex_25.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day10_ex_26():
    """BD perp AC, CE perp AB"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (1.2, 1.8)
    E = (-1.2, 1.8)
    O = (0, 1.2)
    
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
    add_point_label(ax, *O, 'O', (0.15, 0))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day10_ex_26.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day10_ex_28():
    """DE//AC, DF//AB"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (0.5, 0)
    E = (-0.75, 1.5)
    F = (1.25, 1.5)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, D, E, color='blue')
    draw_line(ax, D, F, color='blue')
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, -0.4))
    add_point_label(ax, *E, 'E', (-0.4, 0.1))
    add_point_label(ax, *F, 'F', (0.15, 0.1))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day10_ex_28.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day10_ex_32():
    """DE perp AB, DF perp AC"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (0, 0)
    E = (-1, 1.5)
    F = (1, 1.5)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, A, D, color='blue')
    draw_line(ax, D, E, color='green')
    draw_line(ax, D, F, color='green')
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, -0.4))
    add_point_label(ax, *E, 'E', (-0.4, 0.1))
    add_point_label(ax, *F, 'F', (0.15, 0.1))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day10_ex_32.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# ================== Day11 Exercises ==================

def day11_ex_09():
    """Rt triangle, D is midpoint of AB"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (0, 0)
    C = (4, 0)
    D = (0, 1.5)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, A, C)
    draw_line(ax, C, D, color='blue')
    
    # D is midpoint marker
    ax.plot(2, 1.5, 'ko', markersize=4)
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, 2, 1.5, 'D', (0.1, 0.1))
    
    draw_right_angle(ax, B, A, C, size=0.3)
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 4)
    plt.savefig('day11_ex_09.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day11_ex_11():
    """AB perp BD, CD perp BD"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (0, 0)
    C = (4, 3)
    D = (4, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, D)
    draw_line(ax, D, C)
    draw_line(ax, A, C)
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, 0.1))
    add_point_label(ax, *D, 'D', (0.1, -0.3))
    
    draw_right_angle(ax, B, A, D, size=0.3)
    draw_right_angle(ax, D, B, C, size=0.3)
    
    ax.set_xlim(-1, 5.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day11_ex_11.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day11_ex_26():
    """CD perp AB"""
    fig, ax = setup_figure()
    A = (0, 0)
    B = (5, 0)
    C = (2, 0)
    D = (2, 2.4)
    
    draw_line(ax, A, B)
    draw_line(ax, A, D)
    draw_line(ax, D, B)
    draw_line(ax, C, D, color='blue')
    
    add_point_label(ax, *A, 'A', (-0.3, -0.3))
    add_point_label(ax, *B, 'B', (0.1, -0.3))
    add_point_label(ax, 2, 0, 'D', (0.1, -0.4))
    add_point_label(ax, 2, 2.4, 'C', (0.1, 0.1))
    
    draw_right_angle(ax, (2, 0), (2, 2.4), B, size=0.2)
    
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 3.5)
    plt.savefig('day11_ex_26.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day11_ex_27():
    """ACB=ADB=90, AC=AD"""
    fig, ax = setup_figure()
    A = (2, 3)
    B = (2, 0)
    C = (0, 1.5)
    D = (4, 1.5)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, A, D)
    draw_line(ax, B, C)
    draw_line(ax, B, D)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (0.1, -0.3))
    add_point_label(ax, *C, 'C', (-0.4, 0))
    add_point_label(ax, *D, 'D', (0.15, 0))
    
    ax.set_xlim(-1, 5.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day11_ex_27.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day11_ex_28():
    """AB perp BD, CD perp BD, E midpoint"""
    fig, ax = setup_figure()
    A = (0, 2.5)
    B = (0, 0)
    C = (4, 2.5)
    D = (4, 0)
    E = (2, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, D)
    draw_line(ax, D, C)
    draw_line(ax, A, E, color='blue')
    draw_line(ax, E, C, color='blue')
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, 0.1))
    add_point_label(ax, *D, 'D', (0.1, -0.3))
    add_point_label(ax, *E, 'E', (0, -0.4))
    
    draw_right_angle(ax, B, A, D, size=0.25)
    draw_right_angle(ax, D, B, C, size=0.25)
    
    ax.set_xlim(-1, 5.5)
    ax.set_ylim(-1, 3.5)
    plt.savefig('day11_ex_28.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day11_ex_31():
    """AB perp BC, DC perp BC, AC=BD"""
    fig, ax = setup_figure()
    A = (0, 2.5)
    B = (0, 0)
    C = (4, 0)
    D = (4, 2.5)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, C, D)
    draw_line(ax, A, C, color='blue')
    draw_line(ax, B, D, color='blue')
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, 0.1))
    
    draw_right_angle(ax, B, A, C, size=0.25)
    draw_right_angle(ax, C, B, D, size=0.25)
    
    ax.set_xlim(-1, 5.5)
    ax.set_ylim(-1, 3.5)
    plt.savefig('day11_ex_31.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# ================== Day12 Exercises ==================

def day12_ex_03():
    """D is midpoint, double median"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (0, 0)
    E = (0, -3)
    
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
    plt.savefig('day12_ex_03.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day12_ex_21():
    """D midpoint, E on AD, F on AC"""
    fig, ax = setup_figure()
    A = (0, 4)
    B = (-2.5, 0)
    C = (2.5, 0)
    D = (0, 0)
    E = (0, 2)
    F = (1.25, 2)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, A, D, color='gray')
    draw_line(ax, B, F, color='blue')
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, -0.4))
    add_point_label(ax, *E, 'E', (-0.4, 0))
    add_point_label(ax, *F, 'F', (0.15, 0.1))
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 5)
    plt.savefig('day12_ex_21.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day12_ex_22():
    """Isosceles, angle A = 36, BD bisector"""
    fig, ax = setup_figure()
    # 36 degree isosceles
    A = (0, 3.5)
    B = (-1.5, 0)
    C = (1.5, 0)
    D = (0.5, 1.75)  # On AC
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, B, D, color='blue')
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.15, 0.1))
    
    ax.annotate('36°', (0.1, 3), fontsize=10, color='red')
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 4.5)
    plt.savefig('day12_ex_22.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day12_ex_23():
    """ACB=90, AC=BC, DE perp AC, DF perp BC"""
    fig, ax = setup_figure()
    A = (0, 0)
    B = (3, 0)
    C = (3, 3)
    D = (1.5, 1.5)
    E = (0, 1.5)
    F = (1.5, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, A, C)
    draw_line(ax, D, E, color='blue')
    draw_line(ax, D, F, color='blue')
    
    add_point_label(ax, *A, 'A', (-0.3, -0.3))
    add_point_label(ax, *B, 'B', (0.1, -0.3))
    add_point_label(ax, *C, 'C', (0.1, 0.1))
    add_point_label(ax, *D, 'D', (0.15, 0.1))
    add_point_label(ax, *E, 'E', (-0.4, 0))
    add_point_label(ax, *F, 'F', (0, -0.4))
    
    draw_right_angle(ax, A, C, B, size=0.25)
    
    ax.set_xlim(-1, 4.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day12_ex_23.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day12_ex_30():
    """AD median, AD = 1/2 BC"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (0, 0)
    E = (-1, 1.5)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, A, D, color='blue')
    draw_line(ax, D, E, color='green')
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, -0.4))
    add_point_label(ax, *E, 'E', (-0.4, 0.1))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day12_ex_30.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# ================== Day13 Exercises ==================

def day13_ex_31():
    """Coordinate system with points"""
    fig, ax = setup_figure()
    
    # Draw axes
    ax.annotate('', xy=(5, 0), xytext=(-4, 0),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.annotate('', xy=(0, 5), xytext=(0, -3),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    ax.annotate('x', (4.8, -0.4), fontsize=12)
    ax.annotate('y', (0.2, 4.8), fontsize=12)
    ax.annotate('O', (-0.4, -0.4), fontsize=12)
    
    # Draw grid
    for i in range(-3, 5):
        ax.axhline(y=i, color='lightgray', linewidth=0.5, zorder=0)
        ax.axvline(x=i, color='lightgray', linewidth=0.5, zorder=0)
    
    # Points
    points = {'A': (3, 2), 'B': (-2, 4), 'C': (-3, -1), 
              'D': (4, -3), 'E': (0, 2), 'F': (-3, 0)}
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown']
    
    for (name, coord), color in zip(points.items(), colors):
        ax.plot(*coord, 'o', markersize=8, color=color)
        ax.annotate(f'{name}({coord[0]},{coord[1]})', 
                   (coord[0]+0.2, coord[1]+0.2), fontsize=9, color=color)
    
    ax.set_xlim(-4.5, 5.5)
    ax.set_ylim(-3.5, 5.5)
    plt.savefig('day13_ex_31.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# ================== Day14 Exercises ==================

def day14_ex_03():
    """AB=DC, angle ABD = CDB"""
    fig, ax = setup_figure()
    A = (0, 2)
    B = (0, 0)
    C = (4, 0)
    D = (4, 2)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, C, D)
    draw_line(ax, D, A)
    draw_line(ax, B, D, color='blue')
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, 0.1))
    
    ax.set_xlim(-1, 5.5)
    ax.set_ylim(-1, 3)
    plt.savefig('day14_ex_03.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day14_ex_04():
    """AB perp BD, CD perp BD"""
    fig, ax = setup_figure()
    A = (0, 2.5)
    B = (0, 0)
    C = (4, 2.5)
    D = (4, 0)
    E = (2, 1.25)
    
    draw_line(ax, A, B)
    draw_line(ax, B, D)
    draw_line(ax, D, C)
    draw_line(ax, A, C)
    draw_line(ax, B, C, color='gray', linewidth=1)
    draw_line(ax, A, D, color='gray', linewidth=1)
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, 0.1))
    add_point_label(ax, *D, 'D', (0.1, -0.3))
    add_point_label(ax, *E, 'E', (0.1, 0.15))
    
    draw_right_angle(ax, B, A, D, size=0.25)
    draw_right_angle(ax, D, B, C, size=0.25)
    
    ax.set_xlim(-1, 5.5)
    ax.set_ylim(-1, 3.5)
    plt.savefig('day14_ex_04.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day14_ex_36():
    """AB=CD, AD=CB"""
    fig, ax = setup_figure()
    A = (0, 2)
    B = (3, 2)
    C = (3, 0)
    D = (0, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, C, D)
    draw_line(ax, D, A)
    draw_line(ax, B, D, color='blue')
    
    add_point_label(ax, *A, 'A', (-0.3, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.3, -0.3))
    
    ax.set_xlim(-1, 4.5)
    ax.set_ylim(-1, 3)
    plt.savefig('day14_ex_36.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day14_ex_37():
    """angle 1=2, A=D"""
    fig, ax = setup_figure()
    A = (0, 2.5)
    B = (0, 0)
    C = (2, 0)
    D = (4, 2.5)
    E = (4, 0)
    F = (2, 1.25)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, C, F)
    draw_line(ax, A, F)
    draw_line(ax, D, E)
    draw_line(ax, E, C)
    draw_line(ax, D, F)
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0, -0.4))
    add_point_label(ax, *D, 'D', (0.1, 0.1))
    add_point_label(ax, *E, 'E', (0.1, -0.3))
    add_point_label(ax, *F, 'F', (0.1, 0.15))
    
    ax.set_xlim(-1, 5.5)
    ax.set_ylim(-1, 3.5)
    plt.savefig('day14_ex_37.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day14_ex_41():
    """ACB=ADB=90, AC=AD"""
    fig, ax = setup_figure()
    A = (2, 3)
    B = (2, 0)
    C = (0, 1.5)
    D = (4, 1.5)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, A, D)
    draw_line(ax, B, C)
    draw_line(ax, B, D)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (0.1, -0.3))
    add_point_label(ax, *C, 'C', (-0.4, 0))
    add_point_label(ax, *D, 'D', (0.15, 0))
    
    ax.set_xlim(-1, 5.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day14_ex_41.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day14_ex_46():
    """BD, CE are heights"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (1.2, 1.8)
    E = (-1.2, 1.8)
    H = (0, 1.2)
    
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
    add_point_label(ax, *H, 'H', (0.15, 0))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1, 4)
    plt.savefig('day14_ex_46.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day14_ex_47():
    """D midpoint, AE=EF"""
    fig, ax = setup_figure()
    A = (0, 4)
    B = (-2.5, 0)
    C = (2.5, 0)
    D = (0, 0)
    E = (0, 2)
    F = (1.25, 2)
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, A, D, color='gray')
    draw_line(ax, B, F, color='blue')
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, -0.4))
    add_point_label(ax, *E, 'E', (-0.4, 0))
    add_point_label(ax, *F, 'F', (0.15, 0.1))
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 5)
    plt.savefig('day14_ex_47.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day14_ex_49():
    """AB//CD, E midpoint of BD"""
    fig, ax = setup_figure()
    A = (-2, 2)
    B = (1, 2)
    C = (2, -1)
    D = (-1, -1)
    E = (0, 0.5)
    
    draw_line(ax, A, B)
    draw_line(ax, D, C)
    draw_line(ax, A, C, color='blue')
    draw_line(ax, B, D, color='blue')
    
    add_point_label(ax, *A, 'A', (-0.4, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.4, -0.3))
    add_point_label(ax, *E, 'E', (0.15, 0.1))
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-2.5, 3.5)
    plt.savefig('day14_ex_49.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def main():
    print("Generating Day9 exercise figures...")
    day9_ex_04()
    day9_ex_07()
    day9_ex_09()
    day9_ex_10()
    day9_ex_11()
    day9_ex_31()
    day9_ex_35()
    
    print("Generating Day10 exercise figures...")
    day10_ex_08()
    day10_ex_10()
    day10_ex_23()
    day10_ex_25()
    day10_ex_26()
    day10_ex_28()
    day10_ex_32()
    
    print("Generating Day11 exercise figures...")
    day11_ex_09()
    day11_ex_11()
    day11_ex_26()
    day11_ex_27()
    day11_ex_28()
    day11_ex_31()
    
    print("Generating Day12 exercise figures...")
    day12_ex_03()
    day12_ex_21()
    day12_ex_22()
    day12_ex_23()
    day12_ex_30()
    
    print("Generating Day13 exercise figures...")
    day13_ex_31()
    
    print("Generating Day14 exercise figures...")
    day14_ex_03()
    day14_ex_04()
    day14_ex_36()
    day14_ex_37()
    day14_ex_41()
    day14_ex_46()
    day14_ex_47()
    day14_ex_49()
    
    print("All exercise figures generated!")

if __name__ == "__main__":
    main()


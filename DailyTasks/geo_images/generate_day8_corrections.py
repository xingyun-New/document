# -*- coding: utf-8 -*-
"""
Generate geometry figures for Day8 exercise set corrections and additions
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

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

# ================== Day8 New Figures ==================

def exercise8_fig_quad():
    """Generic Quadrilateral for Q5, Q9, Q21, Q27"""
    fig, ax = setup_figure()
    A = (0, 2)
    B = (3, 2)
    C = (3, 0)
    D = (0, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, C, D)
    draw_line(ax, D, A)
    draw_line(ax, B, D, color='blue') # Diagonal BD
    draw_line(ax, A, C, color='gray', linewidth=1) # Diagonal AC
    
    add_point_label(ax, *A, 'A', (-0.3, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.3, -0.3))
    
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 3)
    plt.savefig('exercise8_fig_quad.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def exercise8_fig11():
    """Q11: AB=AC, AD=AE, BD=CE"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (-1.2, 1.8) # On AB
    E = (1.2, 1.8)  # On AC
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, B, D, color='blue') # Actually D is on AB, wait.
    # Re-read Q11: AB=AC, AD=AE, BD=CE. D, E are usually points on sides.
    # If D on AB, E on AC, then AD=AE implies isosceles triangle ADE.
    # Then BD = AB - AD, CE = AC - AE. Since AB=AC and AD=AE, then BD=CE.
    # But Q11 asks to prove Triangle ABD congruent to ACE?
    # Let's check triangles: ABD and ACE. AB=AC, AD=AE, Angle A common. SAS.
    # The question gives BD=CE... Maybe D, E are not on AB, AC?
    # Usually "AB=AC, AD=AE" implies a structure like:
    # Triangle ABC and Triangle ADE sharing vertex A.
    # Let's draw common vertex A.
    
    # Redraw: AB=AC, AD=AE. 
    # Likely: Triangle ABD and ACE.
    # AB=AC, AD=AE, BD=CE (SSS) -> Triangle ABD congruent to ACE.
    # So D and E are just points such that these lengths match.
    
    A = (0, 3)
    B = (-1.5, 0)
    C = (1.5, 0)
    D = (-0.8, 1.5) # Arbitrary point
    E = (0.8, 1.5)  # Arbitrary point
    
    draw_line(ax, A, B)
    draw_line(ax, A, D)
    draw_line(ax, B, D)
    
    draw_line(ax, A, C)
    draw_line(ax, A, E)
    draw_line(ax, C, E)
    
    # Indicate sides
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.4, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.4, 0))
    add_point_label(ax, *E, 'E', (0.1, 0))
    
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 3.5)
    plt.savefig('exercise8_fig11.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def exercise8_fig13():
    """Q13: OA=OB, OC=OD, AOC=BOD"""
    fig, ax = setup_figure()
    O = (0, 0)
    A = (-1, 2)
    B = (1, 2)
    C = (-2, 1)
    D = (2, 1)
    
    draw_line(ax, O, A)
    draw_line(ax, O, C)
    draw_line(ax, A, C)
    
    draw_line(ax, O, B)
    draw_line(ax, O, D)
    draw_line(ax, B, D)
    
    add_point_label(ax, *O, 'O', (0.1, -0.3))
    add_point_label(ax, *A, 'A', (-0.3, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (-0.4, 0))
    add_point_label(ax, *D, 'D', (0.1, 0))
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 3)
    plt.savefig('exercise8_fig13.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def exercise8_fig15():
    """Q15: AB=CD, AC=BD, E/F midpoints"""
    fig, ax = setup_figure()
    A = (-1.5, 0)
    B = (1.5, 0)
    C = (-0.5, 2) # C position
    D = (2.5, 2)  # D position? No, AB=CD, AC=BD suggests isosceles trapezoid or similar
    # Let's make Triangle ABC and BAD congruent (SSS). AB common, AC=BD, BC=AD? 
    # Question says "AB=CD, AC=BD". 
    # Usually this is: A, B, C, D on a line? Or Quadrilateral?
    # "E is midpoint of AB, F is midpoint of CD".
    # Likely disjoint segments or a quadrilateral.
    # Given AC=BD and AB=CD.
    # Triangle ABC and DCB? No.
    # Triangle ACE and BDF congruent?
    # Let's assume two triangles sharing a base or typical congruence figure.
    # Let's draw: Two separate triangles or connected.
    # Let's assume Quadrilateral ACBD.
    
    A = (0, 0)
    B = (4, 0)
    C = (3, 2)
    D = (1, 2)
    # Check AB=CD? No.
    # Let's try: A=(-1,0), B=(1,0). E=(0,0).
    # C=(-1,2), D=(1,2). F=(0,2).
    # AB = 2. CD = 2. AB=CD.
    # AC = 2. BD = 2. AC=BD.
    # This works. Parallel segments.
    
    A = (-1, 0)
    B = (1, 0)
    E = (0, 0)
    C = (-1, 2)
    D = (1, 2)
    F = (0, 2)
    
    draw_line(ax, A, B)
    draw_line(ax, C, D)
    draw_line(ax, A, C)
    draw_line(ax, B, D)
    draw_line(ax, A, F, color='blue') # ACE? C-E?
    draw_line(ax, C, E, color='blue')
    draw_line(ax, B, F, color='green')
    draw_line(ax, D, E, color='green') # BDF? D-F?
    
    # Q asks: ACE cong BDF?
    # A, C, E -> Triangle ACE.
    # B, D, F -> Triangle BDF.
    
    add_point_label(ax, *A, 'A', (-0.3, -0.3))
    add_point_label(ax, *B, 'B', (0.1, -0.3))
    add_point_label(ax, *C, 'C', (-0.3, 0.1))
    add_point_label(ax, *D, 'D', (0.1, 0.1))
    add_point_label(ax, *E, 'E', (0, -0.4))
    add_point_label(ax, *F, 'F', (0, 0.2))
    
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 3)
    plt.savefig('exercise8_fig15.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def exercise8_fig25():
    """Q25: Two Rt Triangles"""
    fig, ax = setup_figure()
    A = (0, 2)
    B = (0, 0)
    C = (1.5, 0)
    
    D = (3, 2)
    E = (3, 0)
    F = (4.5, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, A, C)
    draw_right_angle(ax, B, A, C, size=0.3)
    
    draw_line(ax, D, E)
    draw_line(ax, E, F)
    draw_line(ax, D, F)
    draw_right_angle(ax, E, D, F, size=0.3)
    
    add_point_label(ax, *A, 'A', (-0.3, 0.1))
    add_point_label(ax, *B, 'B', (-0.3, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    
    add_point_label(ax, *D, 'D', (-0.3, 0.1))
    add_point_label(ax, *E, 'E', (-0.3, -0.3))
    add_point_label(ax, *F, 'F', (0.1, -0.3))
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 3)
    plt.savefig('exercise8_fig25.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def exercise8_fig36():
    """Q36 Corrected: AB=DC, BAC=DCA (Parallel)"""
    fig, ax = setup_figure()
    A = (0, 2)
    B = (3, 2)
    C = (4, 0)
    D = (1, 0) # Parallelogram-like
    
    # Actually Q says AB=DC, angle BAC=DCA.
    # BAC and DCA are alternate interior angles if AB//CD.
    # But condition is given directly.
    # Construct: AB and CD. AC is transversal.
    
    draw_line(ax, A, B)
    draw_line(ax, C, D)
    draw_line(ax, A, C) # Diagonal
    draw_line(ax, B, C)
    draw_line(ax, A, D)
    
    add_point_label(ax, *A, 'A', (-0.3, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.3, -0.3))
    
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-1, 3)
    plt.savefig('exercise8_fig36.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def exercise8_fig38():
    """Q38: AB=DC, BE=CF, ABE=DCF"""
    fig, ax = setup_figure()
    # A, B, E... on a line? No.
    # ABE is a triangle. DCF is a triangle.
    # Points B, E, C, F on a line usually.
    # B, E, C, F collinear.
    
    A = (1, 2)
    B = (0, 0)
    E = (1.5, 0)
    
    D = (4, 2)
    C = (3, 0)
    F = (4.5, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, E)
    draw_line(ax, A, E)
    
    draw_line(ax, D, C)
    draw_line(ax, C, F)
    draw_line(ax, D, F)
    
    # Connecting line for context
    draw_line(ax, B, F, color='gray', linewidth=0.5)
    
    add_point_label(ax, *A, 'A', (0, 0.1))
    add_point_label(ax, *B, 'B', (-0.3, -0.3))
    add_point_label(ax, *E, 'E', (0.1, -0.3))
    
    add_point_label(ax, *D, 'D', (0, 0.1))
    add_point_label(ax, *C, 'C', (-0.2, -0.3))
    add_point_label(ax, *F, 'F', (0.1, -0.3))
    
    ax.set_xlim(-1, 5.5)
    ax.set_ylim(-1, 3)
    plt.savefig('exercise8_fig38.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def main():
    print("Generating Day8 correction figures...")
    exercise8_fig_quad()
    exercise8_fig11()
    exercise8_fig13()
    exercise8_fig15()
    exercise8_fig25()
    exercise8_fig36()
    exercise8_fig38()
    print("Done.")

if __name__ == "__main__":
    main()


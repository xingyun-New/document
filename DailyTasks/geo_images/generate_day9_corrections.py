# -*- coding: utf-8 -*-
"""
Generate geometry figures for Day9 exercise set corrections and additions
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

# ================== Day9 New Figures ==================

def day9_ex_05():
    """Two separated triangles ABC and DEF"""
    fig, ax = setup_figure(figsize=(8, 4))
    
    # Triangle ABC
    A = (0, 2)
    B = (-1, 0)
    C = (1.5, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, A, C)
    
    add_point_label(ax, *A, 'A', (-0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.3, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    
    # Triangle DEF
    D = (4, 2)
    E = (3, 0)
    F = (5.5, 0)
    
    draw_line(ax, D, E)
    draw_line(ax, E, F)
    draw_line(ax, D, F)
    
    add_point_label(ax, *D, 'D', (-0.1, 0.1))
    add_point_label(ax, *E, 'E', (-0.3, -0.3))
    add_point_label(ax, *F, 'F', (0.1, -0.3))
    
    ax.set_xlim(-1.5, 6)
    ax.set_ylim(-1, 3)
    plt.savefig('day9_ex_05.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_06():
    """Two separated Rt triangles ABC and DEF"""
    fig, ax = setup_figure(figsize=(8, 4))
    
    # Triangle ABC
    C = (0, 0)
    A = (0, 2)
    B = (3, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, A, C)
    draw_right_angle(ax, C, A, B, size=0.3)
    
    add_point_label(ax, *A, 'A', (-0.3, 0))
    add_point_label(ax, *B, 'B', (0.1, -0.3))
    add_point_label(ax, *C, 'C', (-0.3, -0.3))
    
    # Triangle DEF
    F = (5, 0)
    D = (5, 2)
    E = (8, 0)
    
    draw_line(ax, D, E)
    draw_line(ax, E, F)
    draw_line(ax, D, F)
    draw_right_angle(ax, F, D, E, size=0.3)
    
    add_point_label(ax, *D, 'D', (-0.3, 0))
    add_point_label(ax, *E, 'E', (0.1, -0.3))
    add_point_label(ax, *F, 'F', (-0.3, -0.3))
    
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 3)
    plt.savefig('day9_ex_06.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_13():
    """Butterfly shape: AB//CD, E intersection"""
    fig, ax = setup_figure()
    A, B = (-2, 2), (2, 2)
    C, D = (2, -2), (-2, -2) # Note order for butterfly
    # Wait, usually butterfly is AB top, CD bottom.
    # Triangles ABE and DCE.
    # Lines AC and BD intersect at E.
    # If AB//CD, then ABE and DCE are similar/congruent.
    
    E = (0, 0)
    A = (-2, 1.5)
    B = (2, 1.5)
    C = (2, -1.5)
    D = (-2, -1.5)
    
    draw_line(ax, A, B) # Top
    draw_line(ax, D, C) # Bottom
    draw_line(ax, A, C) # Diagonal
    draw_line(ax, B, D) # Diagonal
    
    add_point_label(ax, *A, 'A', (-0.3, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.3, -0.3))
    add_point_label(ax, *E, 'E', (0.2, 0))
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2, 2)
    plt.savefig('day9_ex_13.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_23():
    """Triangles with common vertex A: ABD and ACE"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-2, 0)
    C = (2, 0)
    D = (-1, 0)
    E = (1, 0)
    
    # Or maybe rotation? "Angle 1 = Angle 2" usually means BAD = CAE.
    # Let's draw A, B, C, D, E such that BAD = CAE.
    # Often D is on BC? Or general?
    # "Angle B = Angle C". This suggests isosceles ABC.
    # If D, E on BC, then ABD and ACE.
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, C)
    draw_line(ax, A, D)
    draw_line(ax, A, E)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.3, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.2, -0.4))
    add_point_label(ax, *E, 'E', (0.1, -0.4))
    
    ax.annotate('1', (-0.3, 2), fontsize=10, color='red')
    ax.annotate('2', (0.3, 2), fontsize=10, color='red')
    
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-1, 3.5)
    plt.savefig('day9_ex_23.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_24():
    """AB perp BD, CD perp BD"""
    fig, ax = setup_figure()
    B = (0, 0)
    D = (4, 0)
    A = (0, 2)
    C = (4, 2)
    E = (2, 0) # Intersection of AC and BD? No, E is on BD?
    # Q24: AB perp BD, CD perp BD, AB=CD. Prove Rt ABE cong Rt DCE.
    # This implies E is midpoint of BD.
    
    draw_line(ax, A, B)
    draw_line(ax, B, D)
    draw_line(ax, C, D)
    draw_line(ax, A, E)
    draw_line(ax, C, E)
    
    add_point_label(ax, *A, 'A', (-0.3, 0))
    add_point_label(ax, *B, 'B', (-0.3, -0.3))
    add_point_label(ax, *C, 'C', (0.1, 0))
    add_point_label(ax, *D, 'D', (0.1, -0.3))
    add_point_label(ax, *E, 'E', (0, -0.4))
    
    draw_right_angle(ax, B, A, D, size=0.25)
    draw_right_angle(ax, D, C, B, size=0.25)
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 3)
    plt.savefig('day9_ex_24.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_29():
    """Angle B=C=90, Angle 1=2, AB=AC? No AB=AC not possible if B=C=90 unless A is infinite or rectangle"""
    # Q29: Angle B = Angle C = 90. Angle 1 = Angle 2. AB = AC.
    # If B=C=90, then AB // CD? No, AB perp BC, AC perp BC?
    # Then A, B, C must be distinct.
    # If AB=AC, and B=90, C=90? Impossible for triangle ABC.
    # Maybe Quadrilateral? "Triangle ABD congruent to ACE".
    # So B, C are vertices of triangles.
    # Likely A is top vertex. B, C on a line? No "B=C=90".
    # Ah, maybe AB perp BD and AC perp CE?
    # Let's assume: A is common vertex. ABD and ACE are triangles.
    # Angle B = Angle C = 90.
    # A, B, D and A, C, E.
    # D, E are points.
    # Angle 1 = Angle 2 (likely BAD = CAE).
    # AB = AC.
    
    fig, ax = setup_figure()
    A = (0, 0)
    B = (-2, 1)
    D = (-2, 3) # AB perp BD? No, Angle B=90 in Triangle ABD. So ABD=90.
    # Let's say ABD=90, ACE=90.
    
    A = (0, 0)
    B = (-2, 2) # AB length 2.82
    C = (2, 2)  # AC length 2.82. AB=AC.
    
    # D such that ABD=90. AB vector (-2, 2). Perp vector (2, 2) or (-2, -2).
    # Let's simplify. A at origin.
    # AB along x-axis? No, B=C=90 suggests parallelism if on same line.
    
    # Scenario: Two Rt triangles ABD and ACE sharing vertex A.
    # Angle ABD = 90, Angle ACE = 90.
    # AB = AC.
    # Angle BAD = Angle CAE (Angle 1 = Angle 2).
    
    A = (0, 0)
    B = (-3, 0)
    D = (-3, 2)
    
    C = (3, 0)
    E = (3, 2) # If CAE = BAD?
    # If BAD is angle between y-axis and AD? No.
    # Let's rotate.
    
    draw_line(ax, A, B)
    draw_line(ax, B, D)
    draw_line(ax, A, D)
    draw_right_angle(ax, B, A, D, size=0.3) # Wait B is 90.
    
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-1.5, 1)
    D = (-2.5, 0) # AB perp BD? 
    # Let's place B at origin for ease? No A is common.
    
    # Geometry:
    # A(0, 2). B(-2, 0). C(2, 0).
    # AB = AC.
    # D on line perp to AB at B. E on line perp to AC at C.
    
    A = (0, 2)
    B = (-1.5, 0)
    C = (1.5, 0)
    
    # Vector AB = (-1.5, -2). Perp = (2, -1.5).
    D = (-1.5 + 1, 0 - 0.75) # Direction
    # Let's just draw schematically.
    
    # Just draw two triangles.
    A = (0, 2)
    B = (-2, 0)
    D = (-3, 1) # Make ABD look 90 at B
    C = (2, 0)
    E = (3, 1)  # Make ACE look 90 at C
    
    draw_line(ax, A, B)
    draw_line(ax, B, D)
    draw_line(ax, A, D)
    
    draw_line(ax, A, C)
    draw_line(ax, C, E)
    draw_line(ax, A, E)
    
    # Mark 90
    # Approximate visually or calculate.
    # Let's just assume visual representation.
    
    add_point_label(ax, *A, 'A', (0, 0.1))
    add_point_label(ax, *B, 'B', (-0.3, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.3, 0))
    add_point_label(ax, *E, 'E', (0.1, 0))
    
    ax.annotate('1', (-0.5, 1.5), color='red')
    ax.annotate('2', (0.5, 1.5), color='red')
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 3)
    plt.savefig('day9_ex_29.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_30():
    """AB perp BC, DC perp BC, AB=DC"""
    fig, ax = setup_figure()
    B = (0, 0)
    C = (4, 0)
    A = (0, 2)
    D = (4, 2)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, C, D)
    draw_line(ax, A, C)
    draw_line(ax, B, D)
    
    draw_right_angle(ax, B, A, C, size=0.3) # B is 90
    draw_right_angle(ax, C, B, D, size=0.3) # C is 90
    
    add_point_label(ax, *A, 'A', (-0.3, 0))
    add_point_label(ax, *B, 'B', (-0.3, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, 0))
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 3)
    plt.savefig('day9_ex_30.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_36():
    """AE perp EC, BF perp FC, E-C-F collinear, AE=BF, EC=FC"""
    fig, ax = setup_figure()
    C = (0, 0)
    E = (-2, 0)
    F = (2, 0)
    A = (-2, 2)
    B = (2, 2) # AE=BF=2.
    
    draw_line(ax, E, F)
    draw_line(ax, E, A)
    draw_line(ax, A, C)
    
    draw_line(ax, F, B)
    draw_line(ax, B, C)
    
    draw_right_angle(ax, E, A, C, size=0.3)
    draw_right_angle(ax, F, B, C, size=0.3)
    
    add_point_label(ax, *A, 'A', (-0.3, 0))
    add_point_label(ax, *E, 'E', (-0.3, -0.3))
    add_point_label(ax, *C, 'C', (0, -0.4))
    add_point_label(ax, *F, 'F', (0.1, -0.3))
    add_point_label(ax, *B, 'B', (0.1, 0))
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 3)
    plt.savefig('day9_ex_36.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_37():
    """AB//DC, angle ABD = CDB"""
    fig, ax = setup_figure()
    A = (0, 2)
    B = (3, 2)
    C = (3, 0)
    D = (0, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, C, D)
    draw_line(ax, A, D)
    draw_line(ax, B, C)
    draw_line(ax, B, D)
    
    add_point_label(ax, *A, 'A', (-0.3, 0.1))
    add_point_label(ax, *B, 'B', (0.1, 0.1))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (-0.3, -0.3))
    
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 3)
    plt.savefig('day9_ex_37.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_38():
    """BAD=CAD, ABD=ACD"""
    fig, ax = setup_figure()
    A = (0, 3)
    B = (-1.5, 0)
    C = (1.5, 0)
    D = (0, 1) # D on bisector
    
    draw_line(ax, A, B)
    draw_line(ax, A, C)
    draw_line(ax, B, D)
    draw_line(ax, C, D)
    draw_line(ax, A, D)
    
    add_point_label(ax, *A, 'A', (0.1, 0.1))
    add_point_label(ax, *B, 'B', (-0.3, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, -0.1))
    
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 3.5)
    plt.savefig('day9_ex_38.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_39():
    """AB perp BC, DC perp BC, E midpoint"""
    fig, ax = setup_figure()
    A = (0, 2)
    B = (0, 0)
    C = (4, 0)
    D = (4, 2)
    E = (2, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, C)
    draw_line(ax, C, D)
    draw_line(ax, A, E)
    draw_line(ax, D, E)
    
    draw_right_angle(ax, B, A, E, size=0.25)
    draw_right_angle(ax, C, D, E, size=0.25)
    
    add_point_label(ax, *A, 'A', (-0.3, 0))
    add_point_label(ax, *B, 'B', (-0.3, -0.3))
    add_point_label(ax, *C, 'C', (0.1, -0.3))
    add_point_label(ax, *D, 'D', (0.1, 0))
    add_point_label(ax, *E, 'E', (0, -0.4))
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 3)
    plt.savefig('day9_ex_39.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def day9_ex_40():
    """Angle B=C=90, BAD=CAE, AD=AE"""
    fig, ax = setup_figure()
    # Similar to 39 but AD=AE.
    # B, C 90 deg.
    B = (0, 0)
    C = (4, 0)
    A = (2, 3) # No, B=90, C=90 implies AB//CD? No B, C in ABC?
    # "In figure... angle B=C=90". This means AB perp BC, DC perp BC? No.
    # Maybe ABC and triangle...
    # Vertices A, B, C...
    # Likely: AB perp BD, AC perp CE? No.
    # Let's assume Quadrilateral ABCD or similar.
    # Or Triangle ABC? B=C=90 impossible.
    # Standard figure: AB perp BC, AC perp ...
    # Wait, "Angle B = Angle C = 90".
    # Triangle ABD and ACE?
    # B, C are vertices.
    # A is common.
    # Let's assume figure like Q39: A, D, E, B, C...
    
    # Interpretation: AB perp BD, AC perp CD?
    # If B, C are 90 degrees.
    # And BAD=CAE.
    # AD=AE.
    # Let's use the Q29 figure style.
    # A is top. B, C are feet of perpendiculars.
    # D, E on the base?
    # Or B, C on the legs?
    
    # Common figure: A is top. AB perp BD (B=90). AC perp CE (C=90).
    # But B, C are just angles.
    # Let's assume two triangles ABD and ACE.
    # B=90, C=90.
    
    A = (0, 3)
    B = (-2, 1) # AB
    D = (-3, 0) # BD. Angle ABD=90.
    
    C = (2, 1)
    E = (3, 0)
    
    draw_line(ax, A, B)
    draw_line(ax, B, D)
    draw_line(ax, A, D)
    
    draw_line(ax, A, C)
    draw_line(ax, C, E)
    draw_line(ax, A, E)
    
    add_point_label(ax, *A, 'A', (0, 0.1))
    add_point_label(ax, *B, 'B', (-0.3, 0))
    add_point_label(ax, *D, 'D', (-0.3, -0.3))
    add_point_label(ax, *C, 'C', (0.1, 0))
    add_point_label(ax, *E, 'E', (0.1, -0.3))
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 4)
    plt.savefig('day9_ex_40.jpg', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

def main():
    print("Generating Day9 correction figures...")
    day9_ex_05()
    day9_ex_06()
    day9_ex_13()
    day9_ex_23()
    day9_ex_24()
    day9_ex_29()
    day9_ex_30()
    day9_ex_36()
    day9_ex_37()
    day9_ex_38()
    day9_ex_39()
    day9_ex_40()
    print("Done.")

if __name__ == "__main__":
    main()



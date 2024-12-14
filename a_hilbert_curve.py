import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from mpl_toolkits.mplot3d import Axes3D
from turtle3d import Turtle3D

# Rotation matrix in 90 deg on X
Rx = np.array([
        [1, 0, 0],
        [0, 0, -1],
        [0, 1, 0]
    ])

# Rotation matrix in 90 deg on Y
Ry = np.array([
        [0, 0, 1],
        [0, 1, 0],
        [-1, 0, 0]
    ])
 
# Rotation matrix in 90 deg on Z
Rz = np.array([
        [0, -1, 0],
        [1, 0, 0],
        [0, 0, 1]
    ])

# L-System rules for 3D Hilbert Curve
def apply_lsystem(axiom, rules, iterations):
    for _ in range(iterations):
        axiom = ''.join([rules.get(c, c) for c in axiom])  # Apply the rules to generate the new string

    return axiom

# Interpret the L-system string and trace the 3D path
def interpret_lsystem(axiom, length):
    # Starting position and direction
    turtle = Turtle3D()
    
    points = [turtle.position()]  # Store the starting position
    
    # Process the L-system string
    for symbol in axiom:
        if symbol == 'F':  # Move forward and draw
            turtle.forward(length)
            points.append(turtle.position())
        elif symbol == '+':
            turtle.yaw(90)
            # frame = frame @ Rz
        elif symbol == '-':
            turtle.yaw(-90)
            # frame = frame @ Rz.T
        elif symbol == '^':
            turtle.pitch(90)
            # frame = frame @ Rx
        elif symbol == 'v':
            turtle.pitch(-90)
            # frame = frame @ Rx.T
        elif symbol == '>':
            turtle.roll(-90)
            # frame = frame @ Ry
        elif symbol == '<':
            turtle.roll(-90)
            # frame = frame @ Ry.T
    
    return np.array(points)

# Plot the resulting 3D curve
def plot_curve(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Number of points per group
    group_size = 8
    num_groups = len(points) // group_size + (1 if len(points) % group_size else 0)
    
    # Color map for cycling through colors
    cmap = get_cmap('tab10')  # Use a qualitative color map
    colors = [cmap(i % 10) for i in range(num_groups)]

    # Plot each group with a different color
    for i in range(num_groups):
        group_points = points[i * group_size : (i + 1) * group_size]
        if len(group_points) > 1:  # Plot only if there are multiple points in the group
            group_points = np.array(group_points)
            ax.plot(
                group_points[:, 0], group_points[:, 1], group_points[:, 2],
                color=colors[i], label=f"Group {i+1}"
            )
    
    # Axis labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("3D Hilbert Curve (L-System)")
    ax.legend()  # Optional: Add legend for group colors
    ax.set_aspect('equal', adjustable='box')
    plt.show()

# Parameters
'''
F: Move forward
+: Rotate Yaw 90 deg (Z)
-: Rotate Yaw -90 deg (Z)
^: Rotate Pitch 90 deg (Y)
v: Rotate Pitch -90 deg (Y)
>: Rotate Roll 90 deg (X)
<: Rotate Roll -90 deg (X)
'''
rules = {
    'X': '^ F + F + F v F v F + F + F ^'
}
iterations = 1  # Number of iterations for the L-system (change for more detail)
axiom = "X"  # Starting axiom
length = 1.0  # Length of each step

# Generate the L-system string by applying production rules
lsystem_string = apply_lsystem(axiom, rules, iterations)

# Interpret the L-system and generate the 3D points
points = interpret_lsystem(lsystem_string, length)

# Debugging: Print rounded points to check the generation
print("\nGenerated points:")
print(np.round(points, 2))

# Plot the resulting 3D Hilbert curve
plot_curve(points)

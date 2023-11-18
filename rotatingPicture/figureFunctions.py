import matplotlib.pyplot as plt
import numpy as np


def display_rotated_parallelogram(matrix1, matrix2, limits, size_coefficient, rotation_angle):
    fig, ax = plt.subplots()

    # Extract x and y coordinates from the matrices
    x1, x2, x3, x4 = matrix1[0, :]
    y1, y2, y3, y4 = matrix1[1, :]

    # Find the center of the parallelogram
    center_x = np.mean([x1, x2, x3, x4])
    center_y = np.mean([y1, y2, y3, y4])

    # Translate to the origin
    matrix1[0, :] -= center_x
    matrix1[1, :] -= center_y

    matrix2[0, :] -= center_x
    matrix2[1, :] -= center_y

    # Rotate around the origin
    alpha = np.radians(rotation_angle)
    beta = size_coefficient
    rotation_matrix = np.array([[np.cos(alpha), -np.sin(alpha)],
                                [np.sin(alpha), np.cos(alpha)]])

    scale_matrix = np.array([[beta, 0],
                                [0, beta]])
    matrix2 = np.dot(rotation_matrix, matrix2)
    matrix2 = np.dot(scale_matrix, matrix2)

    print(matrix2)

    # Translate back to the original position
    matrix1[0, :] += center_x
    matrix1[1, :] += center_y

    matrix2[0, :] += center_x
    matrix2[1, :] += center_y

    # Set axis limits manually
    ax.set_xlim(-limits, limits)
    ax.set_ylim(-limits, limits)

    # Draw axes
    ax.axhline(0, color='black', lw=2)
    ax.axvline(0, color='black', lw=2)

    # Add labels
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    # Add title
    ax.set_title("Rotated Parallelogram")

    # Mark the center
    ax.plot(center_x, center_y, marker='o', markersize=8, color='purple', label='Center')

    # Plot the original parallelogram
    parallelogram_x = [x1, x2, x3, x4, x1]
    parallelogram_y = [y1, y2, y3, y4, y1]
    ax.plot(parallelogram_x, parallelogram_y, marker='o', linestyle='-', color='blue', label='Original Parallelogram')

    # Plot the rotated parallelogram
    parallelogram_x_rot = matrix2[0, :].tolist() + [matrix2[0, 0]]
    parallelogram_y_rot = matrix2[1, :].tolist() + [matrix2[1, 0]]
    ax.plot(parallelogram_x_rot, parallelogram_y_rot, marker='o', linestyle='-', color='red', label='Rotated Parallelogram')

    # Add legend
    ax.legend()

    # Display the plot
    plt.grid(True)
    plt.savefig('rotated_parallelogram.png')


def calculate_fourth_point(x1, y1, x2, y2, x3, y3):
    x4 = x1 + x3 - x2
    y4 = y1 + y3 - y2

    return x4, y4

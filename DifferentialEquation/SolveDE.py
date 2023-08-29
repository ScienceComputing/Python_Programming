import numpy as np
import matplotlib.pyplot as plt

def solve_heat_equation(L, T, Nx, Nt, alpha):
    """
    Solves the 1D heat equation using the Finite Difference Method.

    Parameters:
    - L: Length of the spatial domain
    - T: Total simulation time
    - Nx: Number of spatial grid points
    - Nt: Number of time steps
    - alpha: Thermal diffusivity

    Returns:
    - U: 2D array containing the solution
    - x: Array of spatial grid points
    - t: Array of time points
    """

    # Calculate grid spacings
    dx = L / (Nx - 1)
    dt = T / Nt

    # Initialize solution array
    U = np.zeros((Nx, Nt+1))

    # Set initial condition
    x = np.linspace(0, L, Nx)
    U[:, 0] = np.sin(np.pi * x)  # Example initial condition

    # Time-stepping loop
    for n in range(Nt):
        for i in range(1, Nx-1):
            U[i, n+1] = U[i, n] + alpha * (U[i+1, n] - 2 * U[i, n] + U[i-1, n]) * dt / dx**2

    # Create arrays for time and space
    t = np.linspace(0, T, Nt+1)

    return U, x, t

# Parameters
L = 1.0           # Length of spatial domain
T = 0.1           # Total simulation time
Nx = 50           # Number of spatial grid points
Nt = 1000         # Number of time steps
alpha = 0.01      # Thermal diffusivity

# Solve the heat equation
U, x, t = solve_heat_equation(L, T, Nx, Nt, alpha)
print(U, x, t)

# Plot the results
plt.figure(figsize=(8, 6))
plt.imshow(U, cmap='hot', aspect='auto', extent=[0, T, 0, L])
plt.colorbar(label='Temperature')
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('1D Heat Equation Simulation')
plt.show()

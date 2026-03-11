"""
Particle filter localization example.

Demonstrates 1D localization using a simple particle filter that
estimates a fixed true position from noisy particles.
"""

import numpy as np
import matplotlib.pyplot as plt


NUM_PARTICLES = 200


if __name__ == "__main__":
    # Initialize particles uniformly over the 1D space.
    particles = np.random.uniform(0, 10, NUM_PARTICLES)

    true_position = 5.0
    estimates: list[float] = []

    for _ in range(50):
        # Propagate particles with process noise.
        particles += np.random.normal(0, 0.2, NUM_PARTICLES)

        # Compute weights based on distance to the true position.
        weights = np.exp(-(particles - true_position) ** 2)
        weights /= np.sum(weights)

        # Estimate position as weighted average of particles.
        estimate = np.sum(particles * weights)
        estimates.append(estimate)

        # Resample particles according to their weights.
        indices = np.random.choice(range(NUM_PARTICLES), NUM_PARTICLES, p=weights)
        particles = particles[indices]

    plt.plot(estimates, label="Estimate")
    plt.axhline(true_position, color="r", linestyle="--", label="True position")

    plt.title("Particle filter localization")
    plt.xlabel("Step")
    plt.ylabel("Estimated position")
    plt.legend()

    plt.savefig("../assets/particle_filter_localization.png")

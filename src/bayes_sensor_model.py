"""
Bayesian sensor model example.

Simulates iterative Bayesian updating of a binary state belief using a
single sensor with fixed accuracy.
"""

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    prior = 0.5
    sensor_accuracy = 0.8

    measurements: list[float] = []

    for _ in range(30):
        # Random binary measurement: True/False with equal probability.
        is_event = np.random.rand() > 0.5

        likelihood = sensor_accuracy if is_event else 1 - sensor_accuracy

        # Bayesian update for a Bernoulli variable with known sensor accuracy.
        posterior = (likelihood * prior) / (
            likelihood * prior + (1 - likelihood) * (1 - prior)
        )

        prior = posterior
        measurements.append(prior)

    plt.plot(measurements)
    plt.ylim(0, 1)

    plt.title("Bayesian sensor update")
    plt.xlabel("Update step")
    plt.ylabel("Belief (posterior)")

    plt.savefig("../assets/bayes_sensor_model.png")

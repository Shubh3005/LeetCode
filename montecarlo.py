import random
import math

def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if math.sqrt(x**2 + y**2) <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate

# Number of random points
num_samples = 1000000
pi_estimate = monte_carlo_pi(num_samples)

print(f"Estimated Pi using {num_samples} samples: {pi_estimate}")

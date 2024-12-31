import math

def newton_sqrt_inv(x):
    if x == 0:
        return 0
    guess = 1.0 / math.sqrt(x)
    for _ in range(5):
        guess = guess * (1.5 - 0.5 * x * guess * guess)
    return guess

def normalize_velocity(velocity):
    mag_squared = sum(v ** 2 for v in velocity)
    inv_mag = newton_sqrt_inv(mag_squared)
    return tuple(v * inv_mag for v in velocity)

velocities = []
n = int(input("Enter number of velocity vectors: "))
for _ in range(n):
    velocity = tuple(map(int, input("Enter velocity vector (x y z): ").split()))
    velocities.append(velocity)

for i, velocity in enumerate(velocities, 1):
    normalized = normalize_velocity(velocity)
    print(f"normalized vec{i}: {normalized[0]:.6f} {normalized[1]:.6f} {normalized[2]:.6f}")

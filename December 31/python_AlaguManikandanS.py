import math

def normalize_vectors(vectors):
    def approximate_inverse_sqrt(value):
        x = 1 / math.sqrt(value)
        x = x * (1.5 - 0.5 * value * x * x)
        return x

    normalized_vectors = []
    for vec in vectors:
        magnitude_squared = sum(v ** 2 for v in vec)
        inv_magnitude = approximate_inverse_sqrt(magnitude_squared)
        normalized_vectors.append([v * inv_magnitude for v in vec])

    return normalized_vectors

vectors = [
    [3, 4, 0],
    [-6, 8, 0],
    [5, 12, 0],
]

normalized = normalize_vectors(vectors)
for vec in normalized:
    print(vec)

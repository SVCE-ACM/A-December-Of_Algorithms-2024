def fast_inverse_sqrt(x: float) -> float:
    three_halfs = 1.5
    x2 = x * 0.5
    i = int.from_bytes(x.to_bytes(8, 'little'), 'little')
    i = 0x5f3759df - (i >> 1)
    y = float.fromhex(hex(i))
    y = y * (three_halfs - (x2 * y * y))
    return y

def normalize_vectors(vectors):
    result = []
    for vec in vectors:
        x, y, z = vec
        magnitude_squared = x * x + y * y + z * z
        inv_magnitude = fast_inverse_sqrt(magnitude_squared)
        result.append((x * inv_magnitude, y * inv_magnitude, z * inv_magnitude))
    return result

vectors = [
    (3, 4, 0),
    (-6, 8, 0),
    (5, 12, 0)
]

normalized_vectors = normalize_vectors(vectors)
for vec in normalized_vectors:
    print(f"{vec[0]:.6f} {vec[1]:.6f} {vec[2]:.6f}")

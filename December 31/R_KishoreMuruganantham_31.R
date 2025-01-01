fast_inverse_sqrt <- function(x) {
  three_halfs <- 1.5
  x2 <- x * 0.5
  i <- as.integer(bitwXor(as.integer(as.double(x)), 0x5f3759df))
  y <- as.double(i)
  y <- y * (three_halfs - (x2 * y * y))
  return(y)
}

normalize_vectors <- function(vectors) {
  result <- list()
  for (vec in vectors) {
    x <- vec[1]
    y <- vec[2]
    z <- vec[3]
    magnitude_squared <- x * x + y * y + z * z
    inv_magnitude <- fast_inverse_sqrt(magnitude_squared)
    result <- append(result, list(c(x * inv_magnitude, y * inv_magnitude, z * inv_magnitude)))
  }
  return(result)
}

vectors <- list(
  c(3, 4, 0),
  c(-6, 8, 0),
  c(5, 12, 0)
)

normalized_vectors <- normalize_vectors(vectors)
for (vec in normalized_vectors) {
  cat(sprintf("%.6f %.6f %.6f\n", vec[1], vec[2], vec[3]))
}

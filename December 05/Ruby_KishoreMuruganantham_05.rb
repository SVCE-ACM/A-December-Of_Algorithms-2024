def josephus(n, k)
  safe_position = 0
  (1..n).each do |i|
    safe_position = (safe_position + k) % i
  end
  safe_position + 1
end

# Test cases
puts josephus(3, 2)  # Output: 3
puts josephus(5, 3)  # Output: 4

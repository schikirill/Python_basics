src = [300, 2, 12, 44, 1, 0, 1, 4, 10, 7, 1, 78, 123, 55, 90, 29]
result = [src[n] for n in range(1, len(src)) if src[n] > src[n - 1]]

print(result)
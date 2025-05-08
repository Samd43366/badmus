sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_size = len(sample_list) // 3

# Split and reverse each chunk
result = []
for i in range(0, len(sample_list), chunk_size):
    chunk = sample_list[i:i+chunk_size]
    result.append(chunk[::-1])

print(result)

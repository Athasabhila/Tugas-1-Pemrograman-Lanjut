def decode_matrix(matrix):
    transposed_matrix = list(map(list, zip(*matrix)))

    decoded_string = " ".join("".join(filter(str.isalnum, column)) for column in transposed_matrix)

    return decoded_string

with open("matrix.txt", "r") as file:

    matrix = [line.strip() for line in file.readlines()]

rows = len(matrix)
cols = max(len(row) for row in matrix)

for i in range(rows):
    matrix[i] += " " * (cols - len(matrix[i]))

decoded_script = decode_matrix(matrix)
print(decoded_script)

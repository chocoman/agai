def visualize_matrix(X):
    height, width = X.shape
    for i in range(height):
        row = ''
        for j in range(width):
            row += '#' if X[i,j] > 0.5 else ' '
        print(row)


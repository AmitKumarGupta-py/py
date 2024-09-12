import numpy as np
import pandas as pd

# Create a 3x3 square matrix with arbitrary values
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Compute eigenvalues and eigenvectors using np.linalg.eig()
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Create a Pandas DataFrame to store the results
df = pd.DataFrame({
    'Eigenvalues': eigenvalues,
    'Eigenvectors': [str(eigenvector) for eigenvector in eigenvectors.T]
})

# Save the DataFrame to a CSV file with formatting
df.to_csv('eigenvalues_and_eigenvectors.csv', index=False)
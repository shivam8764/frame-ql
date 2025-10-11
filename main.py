from frame_ql import DataFrame

data = {
    'student_id': [101, 102, 103, 104, 105, 106],
    'class': ['A', 'A', 'B', 'B', 'C', 'C'],
    'score': [85, 92, 78, 88, 95, 71]
}

df = DataFrame(data)

print("--- Full DataFrame ---")
print(df)

print("\n--- DataFrame Shape ---")
print(f"Shape: {df.shape}")

print("\n--- DataFrame Head (first 5 rows) ---")
print(df.head())

print("\n--- DataFrame Head (first 3 rows) ---")
print(df.head(3))

# Example of what happens with bad data (uncomment to test)
# bad_data = {'col1': [1, 2, 3], 'col2': [4, 5]}
# bad_df = DataFrame(bad_data)
def faktorial(n):
    if n == 1:  # Base case
        return 1
    else:
        return n * faktorial(n - 1)  # Recursive call

# Pemanggilan recursive function
hasil = faktorial(5)
print(hasil)  # Output: 120
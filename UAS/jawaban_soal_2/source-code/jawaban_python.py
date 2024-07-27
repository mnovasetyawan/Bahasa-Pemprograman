try:
    # Blok kode yang mungkin menyebabkan pengecualian
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result is:", result)
except ValueError:
    # Menangani pengecualian ketika input tidak bisa dikonversi ke integer
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    # Menangani pengecualian ketika terjadi pembagian dengan nol
    print("Error! Cannot divide by zero.")
finally:
    # Blok kode ini akan selalu dieksekusi, terlepas dari apakah ada pengecualian atau tidak
    print("Execution completed.")
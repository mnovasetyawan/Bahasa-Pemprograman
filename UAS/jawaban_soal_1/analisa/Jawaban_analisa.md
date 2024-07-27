#### Function di Python

Function adalah blok kode yang terorganisir dan dapat digunakan kembali yang digunakan untuk melakukan tindakan atau menghitung nilai. Functions membantu mengelompokkan kode yang melakukan tugas tertentu, sehingga memudahkan untuk membaca dan mengelola kode.
Definisi Function

Di Python, function didefinisikan menggunakan kata kunci def diikuti oleh nama function dan tanda kurung. Parameter function dituliskan di dalam tanda kurung, dan kode yang dijalankan ketika function dipanggil ditempatkan di dalam blok indentasi.

Contoh:
```
def nama_function(parameter1, parameter2):
    # blok kode
    hasil = parameter1 + parameter2
    return hasil
```

Pemanggilan function dilakukan dengan menyebut nama function diikuti oleh tanda kurung yang berisi argumen yang diperlukan.

Contoh:
```
hasil = nama_function(5, 3)
print(hasil)  # Output: 8
```

#### Recursive Function di Python

Recursive function adalah function yang memanggil dirinya sendiri dalam rangka menyelesaikan suatu masalah. Recursive function biasanya digunakan untuk masalah yang dapat dipecah menjadi sub-masalah yang lebih kecil dan serupa.
Definisi Recursive Function

Dalam recursive function, sangat penting untuk mendefinisikan kondisi dasar (base case) yang akan menghentikan rekursi, untuk mencegah loop tak berujung.

Contoh sederhana dari recursive function adalah perhitungan faktorial:
```
def faktorial(n):
    if n == 1:  # Base case
        return 1
    else:
        return n * faktorial(n - 1)  # Recursive call

# Pemanggilan recursive function
hasil = faktorial(5)
print(hasil)  # Output: 120
```

Pada contoh di atas:

    faktorial(5) memanggil faktorial(4).
    faktorial(4) memanggil faktorial(3).
    faktorial(3) memanggil faktorial(2).
    faktorial(2) memanggil faktorial(1).
    faktorial(1) mencapai base case dan mengembalikan 1.
    Nilai dikembalikan kembali melalui rantai panggilan: 2 * 1, 3 * 2, 4 * 6, dan akhirnya 5 * 24.

#### Keuntungan dan Kelemahan Recursive Function

Keuntungan:

    Sederhana dan Elegan: Recursive function bisa lebih sederhana dan lebih mudah dimengerti daripada iterasi dalam beberapa kasus.
    Penyelesaian Masalah Terstruktur: Recursive function sangat berguna untuk menyelesaikan masalah yang memiliki struktur berulang, seperti algoritma pencarian dan pengurutan tertentu (misalnya, merge sort, quick sort).

Kelemahan:

    Efisiensi: Recursive function bisa kurang efisien dalam penggunaan memori karena setiap panggilan function disimpan di stack.
    Risiko Stack Overflow: Tanpa base case yang benar atau jika masalah terlalu besar, recursive function bisa menyebabkan stack overflow.
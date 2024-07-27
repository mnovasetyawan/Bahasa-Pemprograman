import tkinter
from tkinter import messagebox

# Fungsi yang akan dipanggil ketika tombol ditekan
def on_button_click():
    """
    Fungsi ini dipanggil ketika tombol 'Submit' ditekan.
    Fungsi ini mengambil teks dari kotak teks dan menampilkan kotak pesan
    dengan teks yang dimasukkan oleh pengguna.
    """
    user_input = entry.get()
    messagebox.showinfo("Info", f"You entered: {user_input}")

# Membuat instance dari Tk
root = tkinter.Tk()
root.title("Simple GUI Example")

# Menambahkan label ke jendela
label = tkinter.Label(root, text="Enter something:")
label.pack(pady=10)

# Menambahkan kotak teks ke jendela
entry = tkinter.Entry(root)
entry.pack(pady=10)

# Menambahkan tombol ke jendela
button = tkinter.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)

# Menjalankan event loop
root.mainloop()

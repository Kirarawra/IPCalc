import tkinter as tk
from tkinter import messagebox
from calculator import hitung_subnet

def hitung_ip():
    try:
        ip = input_ip.get()
        hasil = hitung_subnet(ip)

        teks_hasil = ""
        for nama, nilai in hasil.items():
            teks_hasil += f"{nama}: {nilai}\n"

        label_hasil.config(text=teks_hasil)

    except ValueError:
        messagebox.showerror(
            "Error",
            "IP tidak valid!\nContoh: 192.168.1.10/24"
        )

window = tk.Tk()
window.title("IPCalc TKJ")
window.geometry("400x350")

judul = tk.Label(
    window,
    text="KALKULATOR IP ADDRESS",
    font=("Arial", 14, "bold")
)
judul.pack(pady=15)

tk.Label(
    window,
    text="Masukkan IP Address / Prefix:"
).pack()

input_ip = tk.Entry(window, width=30)
input_ip.pack(pady=5)
input_ip.insert(0, "192.168.1.10/24")


tombol = tk.Button(
    window,
    text="Hitung IP",
    command=hitung_ip
)
tombol.pack(pady=10)

label_hasil = tk.Label(
    window,
    text="Hasil akan muncul di sini",
    justify="left",
    font=("Arial", 10)
)
label_hasil.pack(pady=10)

<<<<<<< HEAD
window.mainloop()
=======
window.mainloop()
>>>>>>> 4e6ba0174a07c90bcec6746d5f7f80b5515c34d0


import customtkinter as ct
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import sympy as sp
import biseksi2 
import newraph1
import regulaf1
import secant1
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Pengaturan tampilan
ct.set_appearance_mode("light")
ct.set_default_color_theme("blue")

# Membuat jendela utama
app = ct.CTk()
app.title("NOREX - Nonlinear Root Explorer")
app.geometry("1550x780")

# Membagi jendela menjadi 3 kolom
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=2)
app.grid_columnconfigure(2, weight=3)

app.grid_rowconfigure(0, weight=0)
app.grid_rowconfigure(1, weight=1)

# header NOREX
header = ct.CTkFrame(
    app,
    fg_color="#172554",
    corner_radius=5,
    height=100
)
header.grid(
    row=0,
    column=0,
    columnspan=3,
    padx=3,
    pady=3,
    sticky="ew"
)
header.grid_propagate(False)

judul = ct.CTkLabel(
    header,
    text="NOREX",
    font=("ROG Fonts", 30, "bold"),
    text_color="white"
)
judul.pack(pady=(20, 5))

subjudul = ct.CTkLabel(
    header,
    text="NONLINEAR ROOT EXPLORER",
    font=("Cooper Black", 20, "bold"),
    text_color="#BFDBFE"
)
subjudul.pack(pady=3)

garis = ct.CTkFrame(
    header,
    height=4,
    fg_color="#94AEF0"
)
garis.pack(fill="x", padx=10, pady=10)

judul2 = ct.CTkLabel(
    header,
    text="Numerical Methods Application",
    font=("Berlin Sans FB Demi", 24, "bold"),
    text_color="white"
)
judul2.pack(pady=3)

metode_text = ct.CTkLabel(
    header,
    text="Bisection • Regula Falsi • Newton-Raphson • Secant",
    font=("Book Antiqua", 16 , "bold"),
    text_color="#BFDBFE"
)
metode_text.pack(pady=3)

# ==================================
# KOLOM 1
# ==================================

kolom1 = ct.CTkFrame(app, fg_color="#DCE3EA")
kolom1.grid(
    row=1,
    column=0,
    padx=5,
    pady=5,
    sticky="nsew"
)

# Label fungsi
label_fungsi = ct.CTkLabel(
    kolom1,
    text="Masukkan Fungsi f(x):",
    text_color = "#263979",
    font=("Bookman Old Style", 18 ,"bold")
)
label_fungsi.pack(pady=10)

# Kotak input fungsi
input_fungsi = ct.CTkEntry(
    kolom1,
    placeholder_text="Contoh: x**2+x-1",
    width=250,
    height=40
)
input_fungsi.pack(pady=5)

judul1 = ct.CTkLabel(
    kolom1,
    text="PILIH METODE",
    font=("Cooper Black", 20, "bold")
)
judul1.pack(pady=20)

metode = ct.StringVar(value="Pilihan Metode")
pilihan = ct.CTkOptionMenu(
    kolom1,
    values=["Biseksi", "Regula Falsi","Newton-Raphson", "Secant"],
    variable=metode,
    font=("Arial", 18, "bold"),
    dropdown_font=("Arial", 16),
    fg_color="#172554",
    button_color="#1E3A8A",
    button_hover_color="#1D4ED8",
    text_color="#FFFFFF",
    dropdown_fg_color="#172554",
    dropdown_text_color="#FFFFFF",
    dropdown_hover_color="#1E40AF"
)
pilihan.pack(pady=10)

# 5. Membuat fungsi untuk tombol
def pilih():
    hasil.configure(metode.get())

frame_parameter = ct.CTkFrame(kolom1)
frame_parameter.pack(fill="x", padx=10, pady=5)

label_a = ct.CTkLabel(frame_parameter, text="Batas bawah (a)")
input_a = ct.CTkEntry(frame_parameter)

label_b = ct.CTkLabel(frame_parameter, text="Batas atas (b)")
input_b = ct.CTkEntry(frame_parameter)

label_e = ct.CTkLabel(frame_parameter, text="Toleransi eror (e)")
input_e = ct.CTkEntry(frame_parameter)

def ubah_metode(pilihan):
    for widget in [label_a, input_a, label_b, input_b, label_e, input_e]:
        widget.pack_forget()
    if pilihan == "Biseksi":
        label_a.pack(pady=5)
        input_a.pack(pady=5)

        label_b.pack(pady=5)
        input_b.pack(pady=5)
        
        label_e.pack(pady=5)
        input_e.pack(pady=5)

    elif pilihan == "Regula Falsi":
        label_a.pack(pady=5)
        input_a.pack(pady=5)
        
        label_b.pack(pady=5)
        input_b.pack(pady=5)
                
        label_e.pack(pady=5)
        input_e.pack(pady=5)
        
    elif pilihan == "Newton-Raphson":
        label_a.pack(pady=5)
        input_a.pack(pady=5)

        label_b.pack_forget()
        input_b.pack_forget()

        label_e.pack(pady=5)
        input_e.pack(pady=5)
    else :
        label_a.pack(pady=5)
        input_a.pack(pady=5)
        
        label_b.pack(pady=5)
        input_b.pack(pady=5)
                
        label_e.pack(pady=5)
        input_e.pack(pady=5)
        
pilihan.configure(command=ubah_metode)

def hitung():
    try:
        fungsi = input_fungsi.get()
        a = float(input_a.get())
        e = float(input_e.get())

        if metode.get() == "Biseksi":
            b = float(input_b.get())
            akar, data = biseksi2.biseksi(fungsi, a, b, e)

        elif metode.get() == "Newton-Raphson":
            akar, data = newraph1.newraph(fungsi, a, e)

        elif metode.get() == "Regula Falsi":
            b = float(input_b.get())
            akar, data = regulaf1.regulafalsi(fungsi, a, b, e) 

        elif metode.get() == "Secant":
            b = float(input_b.get())
            akar, data = secant1.secant(fungsi, a, b, e)

        else:
            raise ValueError("Pilih metode terlebih dahulu.")

        label_hasil.configure(text=f"Penyelesaian: {akar:.6f}")

    except (ValueError, TypeError, SyntaxError) as kesalahan:
        from tkinter import messagebox
        messagebox.showerror("Kesalahan", str(kesalahan))
    tampilkan_iterasi(data, metode.get())
    tampilkan_grafik(fungsi, data, metode.get())


tombol = ct.CTkButton(
    kolom1,
    text="HITUNG",
    font=("Arial", 18, "bold"),
    command=hitung
)

tombol.pack(pady=15)
label_hasil = ct.CTkLabel(
    kolom1,
    text="Penyelesaian: belum dihitung",
    font=("Arial", 18, "bold"),
    text_color="blue"
)
label_hasil.pack(pady=15)


# ==================================
# KOLOM 2
# ==================================

kolom2 = ct.CTkFrame(app, fg_color="#D6E8F5")
kolom2.grid(
    row=1,
    column=1,
    padx=5,
    pady=5,
    sticky="nsew"
)

judul2 = ct.CTkLabel(
    kolom2,
    text="DATA ITERASI",
    font=("Cooper Black", 20, "bold")
)
judul2.pack(pady=20)

frame_tabel = ct.CTkFrame (kolom2)
frame_tabel.pack (fill="both", expand=True, padx=10, pady=10)

def tampilkan_iterasi(data, metode):

    # Bersihkan tabel sebelumnya
    for widget in frame_tabel.winfo_children():
        widget.destroy()

    # Menentukan judul kolom
    if metode == "Biseksi":
        kolom = ["Iterasi", "a", "b", "x_baru",
                 "f(x_baru)", "Error"]

    elif metode == "Newton-Raphson":
        kolom = ["Iterasi", "x_baru", "f(x_baru)",
                 "f'(x_baru)", "Error"]

    elif metode == "Regula Falsi":
        kolom = ["Iterasi", "a", "b", "x_baru",
                         "f(x_baru)", "Error"]

    else :
        kolom = ["Iterasi", "x_baru", 
                         "f(x_baru)", "Error"]

        
    # Membuat judul tabel
    for j, nama in enumerate(kolom):
        label = ct.CTkLabel(
            frame_tabel,
            text=nama,
            font=("Arial", 13, "bold")
        )
        label.grid(row=0, column=j, padx=5, pady=5)

    # Menampilkan isi setiap iterasi
    for i, baris in enumerate(data):

        if metode == "Biseksi":
            nilai = [
                baris["iterasi ke-"],
                baris["a"],
                baris["b"],
                baris["x_baru"],
                baris["f(x_baru)"],
                baris["eror"]
            ]

        elif metode == "Newton-Raphson":
            nilai = [
                baris["iterasi ke-"],
                baris["x_baru"],
                baris["f(x_baru)"],
                baris["f'(x_baru)"],
                baris["eror"]
            ]
        elif metode == "Regula Falsi":
            nilai = [
                baris["iterasi ke-"],
                baris["a"],
                baris["b"],
                baris["x_baru"],
                baris["f(x_baru)"],
                baris["eror"]
            ]
        else:
            nilai = [
                baris["iterasi ke-"],
                baris["x_baru"],
                baris["f(x_baru)"],
                baris["eror"]
            ]

        for j, isi in enumerate(nilai):
            label = ct.CTkLabel(
                frame_tabel,
                text=str(isi),
                font=("Arial", 12)
            )
            label.grid(row=i+1, column=j, padx=5, pady=5)


# ==================================
# KOLOM 3
# ==================================

kolom3 = ct.CTkFrame(app, fg_color="#C5E4EA")
kolom3.grid(
    row=1,
    column=2,
    padx=5,
    pady=5,
    sticky="nsew"
)

judul3 = ct.CTkLabel(
    kolom3,
    text="GRAFIK",
    font=("Arial", 20, "bold")
)
judul3.pack(pady=20)

frame_grafik = ct.CTkFrame(kolom3)
frame_grafik.pack(fill="both", expand=True, padx=10, pady=10)

# Membuat grafik satu kali
fig = Figure(figsize=(7, 5))
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=frame_grafik)
canvas.get_tk_widget().pack(fill="both", expand=True)


def tampilkan_grafik(fungsi, data, metode):

    # Bersihkan isi grafik lama
    ax.clear()

    # Membuat simbol dan fungsi numerik
    x = sp.Symbol("x")
    f = sp.sympify(fungsi)
    f_num = sp.lambdify(x, f, "numpy")

    # Mengambil titik iterasi
    nilai_x = [baris["x_baru"] for baris in data]

    # Menentukan rentang grafik
    if nilai_x:
        x_min = min(nilai_x) - 2
        x_max = max(nilai_x) + 2
    else:
        x_min, x_max = -5, 5

    x_grafik = np.linspace(x_min, x_max, 300)
    y_grafik = f_num(x_grafik)

    # Menggambar kurva fungsi
    ax.plot(x_grafik, y_grafik, label="f(x)")

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

    # Menggambar titik iterasi
    if nilai_x:
        y_iterasi = [f_num(nilai) for nilai in nilai_x]

        ax.scatter(
            nilai_x,
            y_iterasi,
            color="red",
            label="Titik iterasi",
            zorder=3
        )

    ax.set_title(f"Grafik Metode {metode}")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()

    # Memperbarui grafik
    canvas.draw_idle()

def tutup_aplikasi():
    canvas.get_tk_widget().destroy()
    plt.close(fig)
    app.destroy()

app.protocol("WM_DELETE_WINDOW", tutup_aplikasi)

# Menjalankan GUI
app.mainloop()

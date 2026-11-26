import sympy as sp

def regulafalsi(fungsi, a, b, e):
    # 1. Mendefinisikan variabel x
    x = sp.Symbol('x')
    # 2. Mengubah fungsi menjadi ekspresi matematika
    f = sp.sympify(fungsi)
    # 3. Menghitung nilai fungsi pada batas interval
    hasil_a = float(f.subs(x, a))
    hasil_b = float(f.subs(x, b))
    # 4. Memeriksa toleransi
    if e <= 0:
        raise ValueError("Toleransi harus lebih besar dari nol.")
    # 5. Memeriksa kondisi interval
    if hasil_a * hasil_b > 0:
        raise ValueError(
            "Tidak ada penyelesaian f(x)=0 pada interval."
        )
    # 6. Memeriksa apakah batas interval merupakan akar
    if hasil_a == 0:
        return a, []
    if hasil_b == 0:
        return b, []
    # 7. Inisialisasi variabel
    eror = abs(hasil_a)
    i = 1
    data_iterasi = []
    # 8. Proses iterasi Biseksi
    while eror > e:
        # Menghitung titik tengah
        x_baru = ((hasil_b * a) - (hasil_a * b)) / (hasil_b - hasil_a)
        # Menghitung nilai fungsi di titik tengah
        hasil_x_baru = float(f.subs(x, x_baru))
        # Memperbarui interval
        if hasil_x_baru == 0:
            a = x_baru
            b = x_baru
        elif hasil_x_baru * hasil_a < 0:
            b = x_baru
            hasil_b = hasil_x_baru
        else:
            a = x_baru
            hasil_a = hasil_x_baru
        # Menghitung error interval
        eror = abs(hasil_x_baru)
        # Menyimpan data iterasi
        data_iterasi.append({
            "iterasi ke-": i,
            "a": a,
            "b": b,
            "x_baru": x_baru,
            "f(x_baru)": hasil_x_baru,
            "eror": eror
        })
        # Menambah nomor iterasi
        i += 1
        # Menghentikan jika ditemukan akar tepat
        if hasil_x_baru == 0:
            break
 
    # 9. Menghitung pendekatan akar
    akar = ((hasil_b * a) - (hasil_a * b)) / (hasil_b - hasil_a)
    # 10. Mengembalikan hasil ke program pemanggil
    return akar, data_iterasi



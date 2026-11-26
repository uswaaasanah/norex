# NOREX

NOREX adalah aplikasi desktop untuk mempelajari metode numerik yang memperkirakan akar real dari fungsi, yaitu nilai `x` yang memenuhi `f(x) = 0`. Antarmuka CustomTkinter memungkinkan pengguna memilih metode, memasukkan parameter, lalu melihat perkiraan akar, tabel iterasi, dan grafik fungsi beserta titik-titik iterasi.

Antarmuka aplikasi menggunakan bahasa Indonesia. Metode yang tersedia adalah **Biseksi**, **Regula Falsi**, **Newton-Raphson**, dan **Secant**.

## Fitur

- Memasukkan fungsi simbolik dengan variabel `x`.
- Memilih salah satu dari empat metode pencarian akar.
- Menentukan nilai awal atau interval serta toleransi.
- Melihat perkiraan akar dan nilai pada setiap iterasi.
- Melihat kurva fungsi dan titik iterasi pada grafik Matplotlib di dalam aplikasi.

## Persyaratan

- Python 3
- Layar desktop dan dukungan Tk (Tkinter tersedia di banyak distribusi Python, tetapi pada beberapa distribusi Linux perlu dipasang secara terpisah).
- Paket Python `customtkinter`, `matplotlib`, `numpy`, dan `sympy`.

Pasang dependensi dengan pip:

```bash
python -m pip install customtkinter matplotlib numpy sympy
```

Berkas `requirements.txt` yang tersedia saat ini mencantumkan `customtkinter`, `matplotlib`, dan `sympyp`. Nama paket terakhir tampaknya salah ketik dari `sympy`. Selain itu, aplikasi menggunakan `numpy`, tetapi paket tersebut belum tercantum di berkas tersebut. Perintah instalasi di atas mencantumkan paket yang diimpor langsung oleh kode.

## Menjalankan aplikasi

Jalankan antarmuka grafis dari direktori utama repositori agar Python dapat menemukan modul-modul solver:

```bash
python Norex.py
```

Aplikasi ini tidak menyediakan antarmuka baris perintah. Modul solver juga dapat diimpor dan dipanggil dari program Python lain; lihat bagian [Modul solver](#modul-solver).

## Menggunakan antarmuka

1. Masukkan fungsi terhadap `x` pada **Masukkan Fungsi f(x)**. Contoh: `x**2 - 2`.
2. Pilih metode pada **PILIH METODE**.
3. Masukkan nilai awal atau batas interval dan toleransi pada kolom yang muncul.
4. Klik **HITUNG**.
5. Lihat perkiraan akar di bagian **Penyelesaian**, periksa tabel **DATA ITERASI**, dan amati grafik fungsi serta titik iterasinya di bagian **GRAFIK**.

Gunakan sintaks ekspresi Python/SymPy: tulis pangkat dengan `**` (contoh: `x**3 - 2*x - 5`) dan tuliskan perkalian secara eksplisit (contoh: `2*x`). Ekspresi harus dapat dibaca oleh SymPy dan menghasilkan bilangan real pada titik-titik yang dikunjungi metode yang dipilih. Grafik mengambil sampel menggunakan NumPy pada rentang yang ditentukan berdasarkan titik iterasi.

### Parameter setiap metode

| Metode pada aplikasi | Nilai yang diperlukan | Penggunaan nilai |
| --- | --- | --- |
| Biseksi | Batas bawah `a`, batas atas `b`, toleransi `e` | Membagi dua interval secara berulang. Nilai fungsi pada kedua ujung harus berbeda tanda, atau salah satu ujung merupakan akar. |
| Regula Falsi | Batas bawah `a`, batas atas `b`, toleransi `e` | Menggunakan garis yang menghubungkan nilai fungsi di kedua ujung untuk memperkirakan titik berikutnya. Implementasi mensyaratkan interval dengan perubahan tanda, atau akar pada salah satu ujung. |
| Newton-Raphson | Nilai awal `a`, toleransi `e` | Menggunakan turunan fungsi dan memulai dari `a`. Kolom `b` tidak digunakan. Turunan harus bukan nol pada setiap titik yang memerlukan pembaruan. |
| Secant | Dua nilai awal `a` dan `b`, toleransi `e` | Menggunakan dua titik terakhir untuk memperkirakan titik berikutnya. Implementasi memeriksa bahwa nilai fungsi pada titik awal mengurung akar, walaupun syarat ini umumnya tidak diperlukan oleh metode secant. |

Toleransi harus lebih besar dari nol. Pada implementasi saat ini, biseksi berhenti ketika lebar interval kurang dari atau sama dengan `e`. Regula Falsi, Newton-Raphson, dan Secant berhenti ketika nilai mutlak fungsi pada titik terbaru kurang dari atau sama dengan `e` (kriteria residu). Ukuran galat yang digunakan berbeda-beda; toleransi bukan jaminan batas jarak antara perkiraan yang dilaporkan dan akar eksak.

Solver tidak membatasi jumlah iterasi. Gunakan nilai awal yang sesuai dan toleransi yang wajar. Metode dapat gagal konvergen atau menemui penyebut/turunan nol maupun ekspresi yang tidak dapat dihitung. Fungsi dapat memiliki beberapa akar, dan hasilnya bergantung pada nilai awal atau interval yang diberikan.

## Modul solver

Setiap modul menyediakan fungsi yang menerima fungsi dalam bentuk teks dan mengembalikan `(akar, iterasi)`. `akar` adalah nilai perkiraan yang dihitung, sedangkan `iterasi` adalah daftar kamus yang berisi data numerik dengan kunci seperti yang dijelaskan di bawah. Modul menggunakan SymPy untuk membaca dan menghitung ekspresi.

| Berkas | Fungsi publik | Parameter | Metode |
| --- | --- | --- | --- |
| [`biseksi2.py`](biseksi2.py) | `biseksi(fungsi, a, b, e)` | Teks ekspresi, batas interval, toleransi | Biseksi; data iterasi mencakup nilai `a` dan `b` yang diperbarui, titik tengah `x_baru`, `f(x_baru)`, dan `eror`. Nilai `eror` adalah lebar interval. |
| [`regulaf1.py`](regulaf1.py) | `regulafalsi(fungsi, a, b, e)` | Teks ekspresi, batas interval, toleransi | Regula Falsi; data iterasi mencakup batas yang diperbarui, titik perkiraan, nilai fungsi, dan residu `eror`. |
| [`newraph1.py`](newraph1.py) | `newraph(fungsi, a, e)` | Teks ekspresi, nilai awal, toleransi | Newton-Raphson; menghitung turunan `f'(x)` secara simbolik. Data iterasi mencakup `x_baru`, `f(x_baru)`, `f'(x_baru)`, dan residu `eror`. |
| [`secant1.py`](secant1.py) | `secant(fungsi, a, b, e)` | Teks ekspresi, dua nilai awal, toleransi | Secant; data iterasi mencakup `x_baru`, `f(x_baru)`, dan residu `eror`. |

Contoh pemanggilan solver secara langsung:

```python
import biseksi2

akar, iterasi = biseksi2.biseksi("x**2 - 2", 1, 2, 1e-6)
print(akar)
print(iterasi[-1] if iterasi else "Salah satu batas awal sudah merupakan akar")
```

Riwayat iterasi dapat kosong jika salah satu batas interval sudah merupakan akar eksak. Newton-Raphson tidak memiliki pemeriksaan awal untuk akar pada batas seperti itu.

## Berkas proyek

- [`Norex.py`](Norex.py) — menjalankan jendela CustomTkinter, meneruskan masukan ke solver yang dipilih, menampilkan tabel iterasi, dan menyematkan grafik Matplotlib.
- [`biseksi2.py`](biseksi2.py) — implementasi metode biseksi.
- [`regulaf1.py`](regulaf1.py) — implementasi metode Regula Falsi.
- [`newraph1.py`](newraph1.py) — implementasi metode Newton-Raphson.
- [`secant1.py`](secant1.py) — implementasi metode secant.
- [`requirements.txt`](requirements.txt) — daftar dependensi; lihat catatan tentang isinya di atas.

## Catatan dan keterbatasan

- Antarmuka menampilkan dialog untuk kesalahan masukan dan ekspresi yang umum terjadi. Namun, konvergensi matematis tidak dijamin untuk sembarang fungsi atau nilai awal.
- Beberapa pemeriksaan menggunakan perbandingan bilangan pecahan secara eksak, misalnya untuk menentukan apakah nilai fungsi tepat sama dengan nol.
- Newton-Raphson dapat gagal jika turunannya nol pada suatu iterasi. Regula Falsi dan Secant juga dapat menemui penyebut nol pada masukan yang degenerat.
- Jumlah iterasi tidak dibatasi, sehingga proses yang tidak konvergen dapat terus berjalan.
- Rentang grafik ditentukan dari nilai iterasi, lalu fungsi dihitung pada rentang tersebut. Fungsi yang memiliki titik singular, diskontinuitas, nilai kompleks, atau luapan numerik mungkin tidak menghasilkan grafik yang berguna.
- Kode aplikasi masih memuat beberapa label dan pesan kesalahan berbahasa Indonesia.

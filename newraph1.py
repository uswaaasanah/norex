import sympy as sp

def newraph (fungsi, a, e):
    x = sp.Symbol ('x')
    f = sp.sympify (fungsi)
    f_aksen = sp.diff (f,x) 
    f_x = float (f.subs(x,a))
    f_aksen_x = float (f_aksen.subs(x,a))
    if f_aksen_x == 0:
        raise ValueError("Pilih nilai titik awal yang lain (bukan titik puncak).") 
    elif e <= 0:
        raise ValueError("Toleransi harus lebih besar dari nol.")
    else :
        eror = abs (f_x)
        i=1
        data_iterasi = []
        while eror > e :
             x_baru = a - (f_x/f_aksen_x)
             f_x_baru = float (f.subs(x, x_baru))
             f_x_aksen_baru = float (f_aksen.subs(x,x_baru))
             a = x_baru
             f_x = f_x_baru
             f_aksen_x = f_x_aksen_baru
             eror = abs (f_x_baru)
             data_iterasi.append ({"iterasi ke-":i, "a": 
                                   a, "x_baru": x_baru, 
                                   "f(x_baru)":f_x_baru , "f'(x_baru)": f_x_aksen_baru, 
                                   "eror": eror})
             i+=1
             if f_x_baru == 0:
                 break
        akar = a
    return akar, data_iterasi 
        
    




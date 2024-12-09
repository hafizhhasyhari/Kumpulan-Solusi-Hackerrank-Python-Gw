"""
Program : MenghitungBiayaParkir
{I.S. : user memasukkan jenis kendaraan (Jenis), nomor polisi (NoPol), jam dan menit masuk serta jam dan menit keluar}
{F.S. : menampilkan lama parkir dan biaya parkir}
"""

import os

# tampilan ke layar :
print("Data Kendaraan Parkir");
print("=====================")
# input jenis kendaraan
Jenis = str(input("Masukkan jenis kendaraan : "));
Jenis = Jenis.upper();

# validasi jenis kendaraan
if ((Jenis == "MOTOR") or (Jenis == "MOBIL")):
    # menginput nomor polisi, jam dan menit masuk, jam dan menit keluar
    NoPol       = str(input("Masukkan nomor polisi    : "));

    # memasukkan jam masuk
    JamMasuk    = int(input("Masukkan jam masuk       : "));
    
    # memasukkan menit masuk
    MenitMasuk  = int(input("Masukkan menit masuk     : "));
    
    # memasukkan jam keluar
    JamKeluar   = int(input("Masukkan jam keluar      : "));
    
    # memasukkan menit keluar
    MenitKeluar = int(input("Masukkan menit keluar    : "));

    # jika MenitKeluar kurang dari MenitMasuk
    if (MenitKeluar < MenitMasuk):
        MenitKeluar = MenitKeluar + 60;
        JamKeluar   = JamKeluar - 1;
    
    # jika JamKeluar kurang dari JamMasuk
    if (JamKeluar < JamMasuk):
        JamKeluar = JamKeluar + 12;

    # menghitung lama parkir
    Jam         = JamKeluar - JamMasuk;
    Menit       = MenitKeluar - MenitMasuk;
    JamParkir   = Jam;

    # jika menit > 0, maka jam parkir tambah 1
    if (Menit > 0):
        JamParkir = JamParkir + 1;

    # menghitung biaya parkir
    if (Jenis == "MOTOR"):
        BiayaParkir = 1500;
        if(JamParkir > 1):
            BiayaParkir = BiayaParkir + (JamParkir - 1) * 500;
    else:
        BiayaParkir = 3000;
        if (JamParkir > 1):
            BiayaParkir = BiayaParkir + (JamParkir - 1) * 1000;
    
    # menampilkan lama parkir dan biaya parkir 
    os.system("pause"); # os ini untuk kita munculkan data setelah dienter
    os.system("cls");

    print("              BIAYA PARKIR");
    print("-"*40);
    print(f"Jenis Kendaraan          : {Jenis.upper()}");
    print(f"Nomor Polisi             : {NoPol}");
    print(f"Masuk(Jam:Menit)         : {JamMasuk}  : {MenitMasuk}");
    if (JamKeluar > 12):
        JamKeluar = JamKeluar - 12;
    if (MenitKeluar >= 60):
        MenitKeluar = MenitKeluar - 60;
        JamKeluar   = JamKeluar + 1;
    print(f"Keluar(Jam:Menit)        : {JamKeluar}  : {MenitKeluar}");
    print(f"Lama parkir              : {Jam} Jam {Menit} Menit");
    print(f"                         : {JamParkir} Jam");
    print(f"Biaya parkir             : Rp{BiayaParkir:,}");
    print("-"*40);
else:
    print();
    print("Anda salah memasukkan jenis kendaraan!");

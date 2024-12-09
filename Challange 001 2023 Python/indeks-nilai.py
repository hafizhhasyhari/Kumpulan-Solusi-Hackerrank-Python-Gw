"""
Program : MenentukanIndexNilai
{I.S. : user memasukkan nilai}
{F.S. : menampilkan indeks yang didapat dari nilai}
"""

# Memasukkan nilai
Nilai = float(input("Masukkan nilai : "));

# menentukan indeks nilai menggunakan nested if
""""
if ((Nilai >= 80) and (Nilai <= 100)):
    Indeks = "A";
elif ((Nilai >= 70) and (Nilai < 80)):
    Indeks = "B";
elif ((Nilai >= 60) and (Nilai < 70)):
    Indeks = "C";
elif ((Nilai >= 50) and (Nilai < 60)):
    Indeks = "D";
else: 
    Indeks = "E";
"""

# menentukan indeks dengan penyederhaan if-elif
if (80 <= Nilai <= 100):
    Indeks = "A";
elif (70 <= Nilai < 80):
    Indeks = "B";
elif (60 <= Nilai < 70):
    Indeks = "C";
elif (50 <= Nilai < 60):
    Indeks = "D";
else:
    Indeks = "E";

# Menampilkan indeks
print(f"Indeks         : {Indeks}");

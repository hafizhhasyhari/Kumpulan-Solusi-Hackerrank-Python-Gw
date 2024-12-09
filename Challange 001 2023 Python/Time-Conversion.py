"""
1 menit = 60 detik
1 detik = 1/60 menit

1 jam = 60 menit * 60 detik/menit
1 jam = 36000 detik

24jam = 36000 * 24 = 
1 menit = 1/60 jam

1 hari = 24 jam
1 jam = 1/24 hari


Program : buatlah algoritma mengkonversi waktu dari satuan detik. Tampilkan ke dalam hari, jam, menit, detik.
Misalkan : 250.000 detik = 2 hari, 21 jam, 26 menit, 40 detik.
"""

# masukkan input detik
jumlahDetik = 250000

# koversi detik ke hari
hari =  jumlahDetik // 86400; # 86400 adalah konversi dari 24 jam ke detik
sisa = jumlahDetik % 86400;
print(f"sisa bagi : {sisa}");
jam = sisa // 3600;
sisa = sisa % 3600;
print(f"sisa bagi : {sisa}");
menit = sisa // 60;

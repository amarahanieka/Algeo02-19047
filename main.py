from functions import *


#file1 = open("contoh.txt", "r")
#teks1 = file1.read()
teks1 = 'naik-naik ke puncak gunung,naik delman, si kancil anak nakal, pamanku dari desa, topi saya bundar, burung kaktua, anak gembala, cangkul-cangkul, abang tukang bakso, hujan rintik-rintik, ibu dan ayah. cicak di dinding, naik kereta api. bintang kecil.  diambil 10 lagu dan di bentuk kelompok'
a = Simplify(teks1)

#file2 = open("contoh1.txt", "r")
#teks2 = file2.read()
teks2 = 'Saingan Trump dari Partai Demokrat, Joe Biden, telah menyegel kemenangan di negara bagian Michigan, demikian menurut laporan Associated Press dan media-media AS lainnya. Dengan demikian, Biden hanya butuh 6 suara elektoral lagi untuk mencapai 270 suara elektoral, total suara yang disyaratkan bagi kandidat untuk melenggang ke Gedung Putih. Sementara itu, di luar TCF Center, yang menjadi lokasi penghitungan surat suara di Detroit, Michigan, pendukung Trump meminta penghitungan suara dihentikan. Hentikan penghitungan teriak para pendukung Trump berulang-ulang. Sekretaris Negara Michigan Jocelyn Benson menyebut gugatan hukum kubu Trump untuk mengakhiri penghitungan suara di negara bagian itu sebagai langkah sembrono, demikian menurut Reuters. Dia kemudian memberikan jaminan bahwa semua surat suara yang sah di Michigan telah ditabulasikan secara akurat dan aman.'
b = Simplify(teks2)
teks3 = "Ayah ibu adalah kakek"
new=Simplify(teks3)

print (new)
n=panjangteks(new)
list=vektor(new)

print(list)



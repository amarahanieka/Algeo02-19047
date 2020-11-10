from functions import *


#file1 = open("testcase.txt", "r")
#teks1 = file1.read()
teks1 = 'naik-naik ke puncak gunung,naik delman, si kancil anak nakal, pamanku dari desa, topi saya bundar, burung kaktua, anak gembala, cangkul-cangkul, abang tukang bakso, hujan rintik-rintik, ibu dan ayah. cicak di dinding, naik kereta api. bintang kecil.  diambil 10 lagu dan di bentuk kelompok'
d1 = Simplify(teks1)

#file2 = open("contoh1.txt", "r")
#teks2 = file2.read()
teks2 = 'Saingan Trump dari Partai Demokrat, Joe Biden, telah menyegel kemenangan di negara bagian Michigan, demikian menurut laporan Associated Press dan media-media AS lainnya. Dengan demikian, Biden hanya butuh 6 suara elektoral lagi untuk mencapai 270 suara elektoral, total suara yang disyaratkan bagi kandidat untuk melenggang ke Gedung Putih. Sementara itu, di luar TCF Center, yang menjadi lokasi penghitungan surat suara di Detroit, Michigan, pendukung Trump meminta penghitungan suara dihentikan. Hentikan penghitungan teriak para pendukung Trump berulang-ulang. Sekretaris Negara Michigan Jocelyn Benson menyebut gugatan hukum kubu Trump untuk mengakhiri penghitungan suara di negara bagian itu sebagai langkah sembrono, demikian menurut Reuters. Dia kemudian memberikan jaminan bahwa semua surat suara yang sah di Michigan telah ditabulasikan secara akurat dan aman.'
d2 = Simplify(teks2)

teks3 = "Ayah ibu adalah kakek"
d3 = Simplify(teks3) 

# Querynya ntar terima inputan
query = "Ayah"
q = Simplify(query)

#Temuin kata-katanya
D1 = vektor(d1)
D2 = vektor(d2)
D3 = vektor(d3)
Q = vektor(q)

#Term hasil concat dari kata-kata yang ada di dokumen sama query.

term = basis(D1+D2+Q)

print(jadiinvektor(D1))
print(jadiinvektor(D2))
print(jadiinvektor(D3))
print(jadiinvektor(Q))

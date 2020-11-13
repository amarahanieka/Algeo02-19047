from functions import *


file1 = open("filetxt/txt1.txt", "r")
judul1 = file1.readline()
teks1 = file1.read()
d1 = Simplify(teks1)

file2 = open("filetxt/txt2.txt", "r")
judul2 = file2.readline()
teks2 = file2.read()
d2 = Simplify(teks2)

file3 = open("filetxt/txt3.txt", "r")
judul3 = file3.readline()
teks3 = file3.read()
d3 = Simplify(teks3)

#buat judul
judulteks = [judul1, judul2, judul3]

# Querynya ntar terima inputan
query = str(input())
q = Simplify(query)

#Temuin kata-katanya
D1 = vektor(d1)
D2 = vektor(d2)
D3 = vektor(d3)
Q = vektor(q)

#Term hasil concat dari kata-kata yang ada di dokumen sama query.
term = basis(Q + D1 + D2 + D3)
D=[Q,D1,D2,D3]
M=[]
i=1
while i < panjang(D):
    M.append(jadiinvektor(D[i],term))
    i+=1

Query=jadiinvektor(Q,term)

#print(M)

#for i in range (panjang(M)):
#    print(similarity(M[i],Query))

#Kumpulan array teksnya supaya nanti bisa dikeluarin
K = [teks1, teks2, teks3]

#Definisiin kamusnya, supaya vektor itu selalu berpasangan sama teks
dict=dictionary(K,M,Query)
judul = title(K, judulteks)

#Sorting berdasarkan similarity
M=sort(M,Query)

#Print berurut yang paling similar
for i in range (panjang(M)):
    for key in K:
        if(dict[key]==M[i]):
            print(similarity(M[i],Query))
            print(judul[key])

            
#Array yang udah terurut, kalimat-kalimatnya, mungkin buat dijadiin tabel di flask
z=[]
for i in range (panjang(M)):
    for key in K:
        if(dict[key]==M[i]):
            z.append(key)
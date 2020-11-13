from functions import *

# Querynya ntar terima inputan
query = str(input("\n"))
q = Simplify(query)
Q = vektor(q)

#Term hasil concat dari kata-kata yang ada di dokumen sama query.
allDoc=[]
for i in range(panjang(teks)):
    a=teks[i]
    allDoc+=a
term = basis(Q + allDoc)
M=[]
for i in range (panjang(teks)):
    M.append(jadiinvektor(teks[i],term))

Query=jadiinvektor(Q,term)

#print(M)

#for i in range (panjang(M)):
#    print(similarity(M[i],Query))

#Kumpulan array teksnya supaya nanti bisa dikeluarin

#Definisiin kamusnya, supaya vektor itu selalu berpasangan sama teks
dict=dictionary(K,M,Query)
judul = title(K, judulfile)

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

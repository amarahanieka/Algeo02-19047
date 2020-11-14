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

#menampilkan tabel term
base=basis(Q)
judultabel=["Term","Query","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11","D12","D13","D14","D15"]
termTable=[[0 for i in range(panjang(judultabel))]for j in range(panjang(base)+1)]
termTable[0]=judultabel
for i in range(panjang(base)):
    termTable[i+1][0]=base[i]
NewQuery=jadiinvektor(Q,base)
for i in range(panjang(base)):
    termTable[i+1][1]=NewQuery[i]
NewM=[]
for i in range (panjang(teks)):
    NewM.append(jadiinvektor(teks[i],base))
TransposeNewM=[[0 for i in range(panjang(teks))] for j in range (panjang(base))]
for i in range(panjang(base)):
    for j in range(panjang(teks)):
        TransposeNewM[i][j]=NewM[j][i]
for i in range(panjang(base)):
    for j in range(panjang(teks)):
        termTable[i+1][j+2]=TransposeNewM[i][j]
for i in range(panjang(base)+1):
    for j in range (panjang(teks)+2):
        print(termTable[i][j],end=" ")
    print("")

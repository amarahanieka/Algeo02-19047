# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# import StopWordRemoverFactory class
# import Sastrawi package
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# bikin jadi kata dasar
def Stem(x):
    a = stemmer.stem(x)
    return a
    # bikin keluar "none"

# ngilangin kata kata ga penting
def Stopword(x):
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    a = stopword.remove(x)
    return a

# ngegabungin
def Simplify(x):
    a = Stopword(x)
    b = Stem(a)
    return b


#menghitung panjang array x
def panjang(x):
    n=0
    for i in x:
        n+=1
    return n

#fungsi vektor berfungsi untuk mengubah teks menjadi vektor kata
def vektor(x):
    list=[]
    string=''
    i=0
    n=panjang(x)
    while (i<n):
        if x[i]!=' ':
            string+=x[i]
        else:
            list.append(string)
            string=''
        if (i==n-1):
            list.append(string)
            string=''
        i+=1
    return list

#fungsi basis sebagai vektor basis untuk membuat term
def basis(x):
    list=[]
    i=0
    while i<panjang(x):
        j=0
        if panjang(list)==0:
            list.append(x[i])
        found=False
        while j<panjang(list):
            if x[i]==list[j]:
                found=True
            j+=1
        if found==False:
            list.append(x[i])
        i+=1
    return list

#Untuk menghitung jumlah elemen array


#Buat vektor

def jadiinvektor(x, term): #Contoh x: D1, D2, query (yang sudah divektorbasiskan)
    #Inisialisasi vektor
    frekuensi = [0 for i in range (panjang(term))]
    #Inisialisasi vektor
    for token in x:
        for i in range (panjang(term)):
            if(token==term[i]):
                frekuensi[i]=frekuensi[i]+1
    return frekuensi


def panjangvektor(x): #x: dokumen yang udah dijadiin vektor
    sumofSquares=0
    for i in x:
        sumofSquares = sumofSquares + (i**2)
    return (sumofSquares)**(1/2)


def dotProduct(x, query): #x : dokumen yang udah dijadiinvektor
    dotprod = 0
    for i in range (panjang(x)):
        dotprod = dotprod + query[i]*x[i]
    return dotprod

def similarity(x, query): #x: dokumen yang udah dijadiinvektor
    sim = dotProduct(x,query)/(panjangvektor(x)*panjangvektor(query))
    return sim

#Ngesort berdasarkan similarity
def sort(M,Query):
    i = 0
    while(i<panjang(M)):
        j=i+1
        while(j<panjang(M)):
            if(similarity(M[i],Query)<similarity(M[j],Query)):
                temp=M[i]
                M[i]=M[j]
                M[j]=temp
            j=j+1
        i=i+1
    return M

#Bikin dictionary buat nyimpen kalimat dari M itu
def dictionary(K,M,Query):
    dict = {}
    i=0
    for key in K:
        dict[key] = M[i]
        i=i+1
    return dict

#Bikin dictionary buat nyimpen nama file dari kalimat itu
def fileteks(K,file):
    dict={}
    i=0
    for key in K:
        dict[key]=file[i]
        i=i+1
    return dict

# Kamus yang lain lagi, isinya title
def title(K,titleteks):
    dict = {}
    i = 0
    for key in K:
        dict[key] = titleteks[i]
        i = i + 1
    return dict

#Dictionary baru buat kalimat pertama

def firstline(K,kalimatpertama):
    dict = {}
    i = 0
    for key in K:
        dict[key] = kalimatpertama[i]
        i = i + 1
    return dict

def hitungkata(K):
    dict={}
    for key in K:
        kata = key.split(" ")
        dict[key] = len(kata)
    return dict

def similar(data,Query,dict,K,judul):
    sim={}
    for key in data:
        for j in K:
            if (key==judul[j]):
                sim[key]=similarity(dict[j],Query)*100
    return sim

def kalper(data,kalimat,K,judul):
    kal={}
    for key in data:
        for j in K:
            if (key==judul[j]):
                kal[key]=kalimat[j]
    return kal

def jumlah(data,K,judul,jumlahkata):
    jum={}
    for key in data:
        for j in K:
            if(key==judul[j]):
                jum[key]=jumlahkata[j]
    return jum

def link(data,linkfile,K,judul):
    li={}
    for key in data:
        for j in K:
            if (key==judul[j]):
                li[key]=linkfile[j]
    return li

# ngitung jumlah kata dalam dokumen termasuk judulnya
# x itu kek readfile di baris 154


#list penyimpanan data
file=["filetxt/txt1.txt","filetxt/txt2.txt","filetxt/txt3.txt","filetxt/txt4.txt","filetxt/txt5.txt","filetxt/txt6.txt","filetxt/txt7.txt","filetxt/txt8.txt","filetxt/txt9.txt","filetxt/txt10.txt","filetxt/txt11.txt","filetxt/txt12.txt","filetxt/txt13.txt","filetxt/txt14.txt","filetxt/txt15.txt"]
judulfile=[0 for i in range(panjang(file))]
kalimatpertama=[0 for i in range (panjang(file))]
teks=[0 for i in range(panjang(file))]
sim=[0 for i in range(panjang(file))]
K=[0 for i in range(panjang(file))]

#pengisian list
for i in range(panjang(file)):
    openfile=open(file[i],"r")
    read=openfile.readline()
    judulfile[i]=read
    readlagi=openfile.readline()
    kalimatpertama[i]=readlagi
for i in range(panjang(file)):
    openfile=open(file[i],"r")
    readfile=openfile.read()
    K[i]=readfile
    d=Simplify(readfile)
    v=vektor(d)
    teks[i]=v


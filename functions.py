# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# import StopWordRemoverFactory class
# import Sastrawi package
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
# import buat count vectorizer aokwokwokw


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

#Buat array urutan similarity
def arraysimilarity(M,query):
    maxsim = []
    for i in range (panjang(M)):
        maxsim.append(similarity(M[i],query))
    sortedarr = sorted(maxsim)
    return sortedarr

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

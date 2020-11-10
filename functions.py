# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# import StopWordRemoverFactory class
# import Sastrawi package
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
# import buat count vectorizer aokwokwokw
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

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

# dijadiin vektor
def jadiinvektor(a):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(a)
    print(vectorizer.get_feature_names())
    print(X.toarray())

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

#fungsi basis sebagai vektor basis untuk membandingkan query dan dokumen
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

def getElmtArray(x):
    element=0
    for i in x:
        element= element+1
    return element

#Menjadikan vektor dari dokumen atau query

def jadiinvektor(x): #Contoh x: D1, D2, query (yang sudah divektorbasiskan)
    global term
    #Inisialisasi vektor
    frekuensi = [0 for i in range (getElmtArray(term))]
    #Inisialisasi vektor
    for token in x:
        for i in range (getElmtArray(term)):
            if(token==term[i]):
                frekuensi[i]=frekuensi[i]+1
    return frekuensi


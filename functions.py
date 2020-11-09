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

#menghitung panjang string
def panjangteks(x):
    n=0
    for i in x:
        n+=1
    return n

def vektor(x):
    list=[]
    string=''
    i=0
    n=panjangteks(x)
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

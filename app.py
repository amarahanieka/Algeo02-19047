from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from functions import *

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
        print(form.errors)
        if request.method == 'POST':
            name = request.form['name']
            print(name)

        if form.validate():
            # Save the comment here.
            flash('Search results for ' + name)

            # file1 = open("testcase.txt", "r")
            # teks1 = file1.read()
            teks1 = 'naik-naik ke puncak gunung,naik delman, si kancil anak nakal, pamanku dari desa, topi saya bundar, burung kaktua, anak gembala, cangkul-cangkul, abang tukang bakso, hujan rintik-rintik, ibu dan ayah. cicak di dinding, naik kereta api. bintang kecil.  diambil 10 lagu dan di bentuk kelompok'
            d1 = Simplify(teks1)
            # file2 = open("contoh1.txt", "r")
            # teks2 = file2.read()
            teks2 = 'Saingan Trump dari Partai Demokrat, Joe Biden, telah menyegel kemenangan di negara bagian Michigan, demikian menurut laporan Associated Press dan media-media AS lainnya. Dengan demikian, Biden hanya butuh 6 suara elektoral lagi untuk mencapai 270 suara elektoral, total suara yang disyaratkan bagi kandidat untuk melenggang ke Gedung Putih. Sementara itu, di luar TCF Center, yang menjadi lokasi penghitungan surat suara di Detroit, Michigan, pendukung Trump meminta penghitungan suara dihentikan. Hentikan penghitungan teriak para pendukung Trump berulang-ulang. Sekretaris Negara Michigan Jocelyn Benson menyebut gugatan hukum kubu Trump untuk mengakhiri penghitungan suara di negara bagian itu sebagai langkah sembrono, demikian menurut Reuters. Dia kemudian memberikan jaminan bahwa semua surat suara yang sah di Michigan telah ditabulasikan secara akurat dan aman.'
            d2 = Simplify(teks2)
            teks3 = "Ayah ibu adalah kakek"
            d3 = Simplify(teks3)

            # Buat nampilin judul

            titleteks1 = "Naik ke puncak gunung"
            titleteks2 = "Saingan Trump"
            titleteks3 = "Ayah ibu"

            titleteks = [titleteks1, titleteks2, titleteks3]

            # Querynya ntar terima inputan
            query = name
            q = Simplify(query)

            # Temuin kata-katanya
            D1 = vektor(d1)
            D2 = vektor(d2)
            D3 = vektor(d3)
            Q = vektor(q)

            # Term hasil concat dari kata-kata yang ada di dokumen sama query.
            term = basis(Q + D1 + D2 + D3)
            D = [Q, D1, D2, D3]
            M = []
            i = 1
            while i < panjang(D):
                M.append(jadiinvektor(D[i], term))
                i += 1

            Query = jadiinvektor(Q, term)

            if (panjangvektor(Query) != 0):
                print(M)

                for i in range(panjang(M)):
                    print(similarity(M[i], Query))

                # Kumpulan array teksnya supaya nanti bisa dikeluarin
                K = [teks1, teks2, teks3]

                # Definisiin kamusnya, supaya vektor itu selalu berpasangan sama teks
                dict = dictionary(K, M, Query)
                judul = title(K, titleteks)

                # Sorting berdasarkan similarity
                M = sort(M, Query)

                # Print berurut yang paling similar
                for i in range(panjang(M)):
                    for key in K:
                        if (dict[key] == M[i]):
                            print(judul[key])

                    # Array yang udah terurut, kalimat-kalimatnya, mungkin buat dijadiin tabel di flask
                    data = []
                    for i in range(panjang(M)):
                        for key in K:
                            if (dict[key] == M[i] and similarity(M[i], Query)) > 0:
                                data.append(judul[key])
                    if (panjang(data) != 0):
                        return render_template("found.html", data=data, form=form)
                    else:
                        return render_template('notfound.html', form=form)
            else:
                return render_template('notfound.html', form=form)
        else:
            flash('Error: All the form fields are required. ')
            return render_template('hello.html', form=form)

@app.route('/nyoba/')
def sample_view():
    return render_template("newtext.html")


if __name__ == "__main__":
    app.run()

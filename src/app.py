from flask import Flask, render_template, flash, request, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from functions import *
from werkzeug.utils import secure_filename
import os

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'filetxt')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['txt'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/search')


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

    @app.route("/search", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
        print(form.errors)
        if request.method == 'POST':
            name = request.form['name']
            print(name)

        if form.validate():
            # Querynya ntar terima inputan
            query = name
            q = Simplify(query)
            Q = vektor(q)

            # Term hasil concat dari kata-kata yang ada di dokumen sama query.
            allDoc = []
            for i in range(panjang(teks)):
                a = teks[i]
                allDoc += a
            term = basis(Q + allDoc)
            M = []
            for i in range(panjang(teks)):
                M.append(jadiinvektor(teks[i], term))

            Query = jadiinvektor(Q, term)

            if (panjangvektor(Query) != 0):
                # Definisiin kamusnya, supaya vektor itu selalu berpasangan sama teks
                dict = dictionary(K, M, Query)
                judul = title(K, judulfile)
                kalimat = firstline(K, kalimatpertama)
                jumlahkata = hitungkata(K)
                linkfile = fileteks(K, file)

                # Sorting berdasarkan similarity
                M = sort(M, Query)

                # Print berurut yang paling similar
                data = []
                for i in range(panjang(M)):
                    for key in K:
                        if (dict[key] == M[i] and similarity(M[i], Query)) > 0:
                            data.append(judul[key])

                # Buat ngeluarin si similarity

                # Array baru yang nge-store similarity sama kalimat
                sim = similar(data, Query, dict, K, judul)
                kal = kalper(data, kalimat, K, judul)
                li = link(data, linkfile, K, judul)
                jum = jumlah(data, K, judul, jumlahkata)
                base = basis(Q)
                judultabel = ["Term", "Query", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11",
                              "D12", "D13", "D14", "D15"]
                termTable = [[0 for i in range(panjang(judultabel))] for j in range(panjang(base) + 1)]
                termTable[0] = judultabel
                for i in range(panjang(base)):
                    termTable[i + 1][0] = base[i]
                NewQuery = jadiinvektor(Q, base)
                for i in range(panjang(base)):
                    termTable[i + 1][1] = NewQuery[i]
                NewM = []
                for i in range(panjang(teks)):
                    NewM.append(jadiinvektor(teks[i], base))
                TransposeNewM = [[0 for i in range(panjang(teks))] for j in range(panjang(base))]
                for i in range(panjang(base)):
                    for j in range(panjang(teks)):
                        TransposeNewM[i][j] = NewM[j][i]
                for i in range(panjang(base)):
                    for j in range(panjang(teks)):
                        termTable[i + 1][j + 2] = TransposeNewM[i][j]
                if (panjang(data) != 0):
                    return render_template("found.html", form=form, termTable=termTable, data=data, sim=sim, kal=kal,
                                           li=li, jum=jum)
                else:
                    return render_template('notfound.html', form=form)
            else:
                return render_template('notfound.html', form=form)
        else:
            flash('Anda tidak memasukkan query apapun.')
            return render_template('hello.html', form=form)

@app.route('/filetxt/txt1.txt/')
def a():
    with open('filetxt/txt1.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt2.txt/')
def b():
    with open('filetxt/txt2.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt3.txt/')
def c():
    with open('filetxt/txt3.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt4.txt/')
def d():
    with open('filetxt/txt4.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt5.txt/')
def e():
    with open('filetxt/txt5.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt6.txt/')
def f():
    with open('filetxt/txt6.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt7.txt/')
def g():
    with open('filetxt/txt7.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt8.txt/')
def h():
    with open('filetxt/txt8.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt9.txt/')
def i():
    with open('filetxt/txt9.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt10.txt/')
def j():
    with open('filetxt/txt10.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt11.txt/')
def k():
    with open('filetxt/txt11.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt12.txt/')
def l():
    with open('filetxt/txt12.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt13.txt/')
def m():
    with open('filetxt/txt13.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt14.txt/')
def n():
    with open('filetxt/txt14.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

@app.route('/filetxt/txt15.txt/')
def o():
    with open('filetxt/txt15.txt', "r") as f:
        content = f.read()
    return render_template("newtext.html", content=content)

if __name__ == "__main__":
    app.run()

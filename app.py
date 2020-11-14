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

                # Sorting berdasarkan similarity
                M = sort(M, Query)

                # Print berurut yang paling similar
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
            flash('Anda tidak memasukkan query apapun.')
            return render_template('hello.html', form=form)

@app.route('/nyoba/')
def sample_view():
    return render_template("newtext.html")


if __name__ == "__main__":
    app.run()

import os
from hashlib import sha1

from flask import Flask, request, render_template, send_file

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "store")


def check_file_exists(hashcode):
    subpath = hashcode[:2] if hashcode and len(hashcode) > 1 else ''
    file = os.path.join(app.config['UPLOAD_FOLDER'], os.path.join(subpath, hashcode)) if subpath else ''
    return file if os.path.isfile(file) else ''


@app.route('/store/list', methods=['GET'])
def list_files():
    listdir = os.listdir(app.config["UPLOAD_FOLDER"])
    response = []
    for subpath in listdir:
        files = os.listdir(os.path.join(app.config["UPLOAD_FOLDER"], subpath))
        for file in files:
            response.append(file)
    return '\n'.join(response)


@app.route("/store/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if request.files and file:
        hashcode = sha1(file.filename.encode()).hexdigest()
        if check_file_exists(hashcode):
            return f"File with name {file.filename} already exists. Hashcode - {hashcode}", 201
        subpath = os.path.join(app.config["UPLOAD_FOLDER"], hashcode[:2])
        if not os.path.isdir(subpath):
            os.mkdir(subpath)
        file.save(os.path.join(subpath, hashcode))
        return hashcode
    return 'Bad request', 400


@app.route('/store/download', methods=['GET'])
def download():
    hashcode = request.args.get('hashcode', default='', type=str)
    file = check_file_exists(hashcode)
    if file:
        return send_file(file, as_attachment=True)
    return f"File with hashcode {hashcode} not found", 400


@app.route('/store/delete', methods=['POST'])
def delete():
    hashcode = request.form.get('hashcode')
    file = check_file_exists(hashcode)
    if file:
        os.remove(file)
        return f'File with hashcode {hashcode} was successfully deleted'
    return f"File with hashcode {hashcode} not found", 400


@app.route("/", methods=["GET"])
def root():
    return render_template("root.html")


if __name__ == '__main__':
    app.run()

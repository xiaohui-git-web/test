from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='./')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<filename>')
def html_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True, port=8100)
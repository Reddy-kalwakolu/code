from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='CODE')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/calculations/<path:filename>')
def plots(filename):
    return send_from_directory(f"{app.static_folder}/plots", filename)

if __name__ == '__main__':
    app.run(debug=True)

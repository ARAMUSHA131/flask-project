import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/open/')
def list_files():
    filenames = os.listdir('open')
    return render_template('open.html', files=filenames)


@app.route('/open/<path:filename>')
def expose_file_from_directory(filename):
    return send_from_directory(
        os.path.abspath('open'),
        filename,
        as_attachment=True
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

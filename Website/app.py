import os
import numpy as np
from PIL import Image
from flask import Flask, render_template, request
app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	file = request.files['image']
	f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
	file.save(f)
	return render_template('index.html#3rdPage')
@app.route('/play', methods = ['POST','GET'])
def convert_sound():
	return
	

if __name__ == "__main__":
    app.run(debug=True)
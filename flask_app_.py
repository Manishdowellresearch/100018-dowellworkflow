# A very simple Flask Hello World app for you to get started with...

from flask import Flask , render_template, request , url_for ,redirect ,flash
from werkzeug.utils import secure_filename
import os
from PIL import Image


app = Flask(__name__, template_folder="/home/dowellproject/mysite/static")

UPLOAD_FOLDER =r'/home/dowellproject//mysite/static/upload'

ALLOWED_EXTENSIONS = {'jpg', 'jpeg','png','JPG','JPEG','PNG'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "secret key"

# limit upload size upto 8mb
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/eSignature')
def signs():
    return render_template('sign.html')


@app.route('/upload')
def upload_form():
	return render_template('upload.html')

@app.route('/uploaded', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		#flash('Image successfully uploaded and displayed below')
		return render_template('upload.html', filename=filename)
	else:
		#flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='upload/' + filename), code=301)







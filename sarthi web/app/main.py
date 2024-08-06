from flask import Flask, request, render_template
from .utils.file_handler import handle_uploaded_file
from .models.transformer_model import generate_code
from .models.image_generator import generate_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        file_path = handle_uploaded_file(file)
        if file_path.endswith('.pdf'):
            code_output = generate_code(file_path)
        else:
            code_output = "Invalid file type. Only PDF is supported."
        
        return code_output

if __name__ == '__main__':
    app.run(debug=True)

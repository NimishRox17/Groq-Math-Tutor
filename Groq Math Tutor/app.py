import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# Load environment variables from .env file
load_dotenv()

from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from utils.ocr import extract_text_from_image
from utils.voice import voice_to_text
from utils.solver import solve_math_problem
import os
from werkzeug.utils import secure_filename
from models import db, MathProblem

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Add this route to serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Add these configurations after creating Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///math_tutor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create tables (add this before running the app)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400
        
        image = request.files['image']
        if image.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        filename = secure_filename(image.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)

        # Extract text from image
        question = extract_text_from_image(filepath)
        
        # Get solution from Groq
        solution = solve_math_problem(question)

        # Save to database with web-accessible path
        math_problem = MathProblem(
            question=question,
            solution=solution,
            input_type='image',
            image_path=url_for('uploaded_file', filename=filename)
        )
        db.session.add(math_problem)
        db.session.commit()

        return jsonify({
            'question': question,
            'solution': solution
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/process-voice', methods=['POST'])
def process_voice():
    try:
        question = voice_to_text()
        solution = solve_math_problem(question)
        
        # Save to database
        math_problem = MathProblem(
            question=question,
            solution=solution,
            input_type='voice'
        )
        db.session.add(math_problem)
        db.session.commit()
        
        return jsonify({
            'question': question,
            'solution': solution
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
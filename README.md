#Groq AI Math Tutor
An intelligent, Groq-powered Math Tutor web application that allows users to input math problems via image uploads or voice commands and receive instant solutions with explanations. The application leverages OCR (Optical Character Recognition) and speech recognition to understand user queries, then uses Groq’s AI model (via an API) to generate real-time feedback and step-by-step solutions. This makes the tool highly useful for students, educators, and learners who want help with understanding and solving math problems interactively.

This project runs on a Flask web backend and a simple HTML/CSS frontend, integrated with several powerful Python libraries and AI technologies.

🔧 Key Technologies & Modules Used:
Frontend:

HTML for structure

CSS for styling (optional, can be customized)

Backend:

Flask for web routing and handling API requests

AI/Processing Modules:

pytesseract for image-to-text OCR

speech_recognition for converting voice to text

Groq API (via OpenAI-compatible call) for solving and explaining math problems

dotenv to securely load API keys

PIL for image handling

Directory & File Structure Highlights:

plaintext
Copy
Edit
groq_math_tutor/
├── app.py               # Main Flask server
├── templates/index.html # Frontend UI
├── static/style.css     # Optional styling
├── utils/
│   ├── ocr.py           # Extract text from images
│   ├── voice.py         # Convert speech to text
│   └── solver.py        # AI logic to solve math
├── .env                 # API key storage
└── requirements.txt     # Dependencies
💡 How It Works (Workflow):
User Input:

User uploads an image or records a voice message containing a math problem.

Input Processing:

Image is processed by pytesseract to extract text.

Voice is converted to text using speech_recognition.

Problem Solving:

Extracted text is passed to Groq API to generate an accurate solution and explanation.

Output:

Solution and step-by-step explanation is returned and displayed on the webpage.

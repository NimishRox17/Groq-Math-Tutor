import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise Exception("GROQ_API_KEY not found in environment variables")

# Initialize Groq client
client = Groq(
    api_key=api_key,
)

def solve_math_problem(question):
    try:
        prompt = f"Solve this math problem step by step: {question}"
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama2-70b-4096"  # Changed to Llama model
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Groq API Error: {str(e)}")

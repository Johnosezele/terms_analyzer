from flask import Flask, render_template, request, jsonify
import nltk
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import openai

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

def simplify_text(text):
    """
    Analyze and simplify the given terms and conditions text.
    Returns a dictionary containing simplified text and key points.
    """
    # Basic text cleaning
    soup = BeautifulSoup(text, 'html.parser')
    clean_text = soup.get_text()
    
    # Break into sentences using NLTK
    sentences = nltk.sent_tokenize(clean_text)
    
    # Identify important sections
    important_sections = []
    keywords = ['agreement', 'privacy', 'rights', 'obligations', 'terminate', 'liability']
    
    for sent in sentences:
        if any(keyword in sent.lower() for keyword in keywords):
            important_sections.append(sent)
    
    # If OpenAI API key is available, use it for advanced analysis
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        openai.api_key = api_key
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that simplifies legal terms into plain English."},
                    {"role": "user", "content": f"Please simplify this text into plain English and highlight key points: {clean_text[:4000]}"}
                ]
            )
            simplified_text = response.choices[0].message['content']
        except Exception as e:
            simplified_text = "OpenAI API error. Falling back to basic analysis."
    else:
        simplified_text = "No OpenAI API key found. Here are the important sections we found:"
        simplified_text += "\n\n" + "\n\n".join(important_sections)
    
    return {
        'simplified_text': simplified_text,
        'important_sections': important_sections,
        'original_length': len(clean_text),
        'num_sentences': len(sentences)
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    analysis = simplify_text(text)
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

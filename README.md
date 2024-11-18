# Terms & Conditions Analyzer

A web application that helps users understand complex terms and conditions by simplifying the language and highlighting important sections.

## Features

- Paste any terms and conditions text
- Get a simplified version in plain English
- Highlight important sections and key points
- View text statistics (length and sentence count)
- Modern, responsive web interface

## Setup

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Install the spaCy English model:
```bash
python -m spacy download en_core_web_sm
```

4. (Optional) Set up OpenAI API for advanced analysis:
   - Create a `.env` file in the project root
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`

3. Paste your terms and conditions text and click "Analyze Text"

## Technologies Used

- Flask (Python web framework)
- spaCy (Natural Language Processing)
- NLTK (Natural Language Toolkit)
- OpenAI API (Optional, for advanced text simplification)
- TailwindCSS (Styling)
- JavaScript (Frontend interactivity)

## Note

This tool is meant to assist in understanding terms and conditions. It should not be considered as legal advice. Always consult with a legal professional for important decisions.

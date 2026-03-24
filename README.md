# Essay Grader – AI-Based Writing Evaluation System

An AI-powered essay grading system that evaluates written content using natural language processing and machine learning techniques. It analyzes grammar, structure, and linguistic features to generate a score and feedback, helping users improve their writing skills.

---

## Features

- Automated essay scoring using machine learning  
- Grammar and language checking using LanguageTool  
- NLP-based text analysis with spaCy  
- Desktop GUI built with PyQt6  
- Modular backend + frontend architecture  
- Real-time feedback generation  

---

## Tech Stack

- NLP: spaCy  
- Grammar Checking: language-tool-python  
- Machine Learning: scikit-learn  
- Frontend: PyQt6  
- Core Language: Python  

---

## Project Structure
```
Essay-Grader/
├── aes_backend.py       # Essay processing, NLP & scoring logic
├── aes_frontend.py      # PyQt6 GUI interface
├── requirements.txt     # Dependencies
└── README.md
```
---

## How It Works

- User inputs an essay through the GUI  
- The frontend sends the essay to the backend  
- The backend:
  - Performs NLP processing using spaCy  
  - Checks grammar using LanguageTool  
  - Extracts features and evaluates using ML model  
- A score and feedback are returned and displayed  

---

## Dependencies

### Python Libraries
```
- language-tool-python==2.8  
- numpy==2.2.3  
- PyQt6==6.8.1  
- scikit-learn==1.6.1  
- spacy==3.7.5  
```
Install all dependencies using:
```
pip install -r requirements.txt
```
---

## How to Run

1. Clone the repository:
```
git clone https://github.com/your-username/Essay-Grader.git
cd Essay-Grader
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the application:
```
python aes_frontend.py
```
---

## Notes

- Ensure spaCy language model is installed before running:
```
python -m spacy download en_core_web_sm
```
- The scoring logic is implemented in aes_backend.py  
- You can tweak feature extraction or improve model accuracy inside the backend  

---

## Future Improvements

- Add deep learning-based essay scoring (BERT / transformers)  
- Improve feedback quality using LLM APIs  
- Add rubric-based grading system  
- Export results as PDF/report  
- Deploy as a web app (Flask / FastAPI)  

---

## Author

Developed by Shivansh (SleepDeprivedShi)

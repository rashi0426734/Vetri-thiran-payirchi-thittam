# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant based on the supplied project specification. It provides:

- Question answering
- Simplified concept explanations
- Quiz generation
- Passage summarization
- Beginner-to-advanced learning recommendations

## Technology

Python, FastAPI, HTML, CSS, JavaScript, Google Gemini API, Uvicorn and Jinja2.

## Project Structure

```text
EduGenie/
├── static/
│   ├── style.css
│   └── app.js
├── templates/
│   └── index.html
├── tests/
│   └── test_api.py
├── .env.example
├── .gitignore
├── ai_client.py
├── config.py
├── explanation_module.py
├── learning_path.py
├── main.py
├── models.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── requirements.txt
└── README.md
```

## Windows Setup

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
copy .env.example .env
```

Open `.env` and put your Gemini API key in `GEMINI_API_KEY`.

Then run:

```powershell
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## API Endpoints

- `POST /qa`
- `POST /explain`
- `POST /quiz`
- `POST /summarize`
- `POST /learn/recommendations`
- `GET /health`

## Security

Never commit `.env` or expose your Gemini API key in screenshots or source control.

## Project Basis

This implementation follows the supplied EduGenie project document's stated architecture, scenarios, five learning functions, FastAPI backend, HTML/CSS frontend, Uvicorn execution model, and milestone structure.

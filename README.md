# Persona-AI

A simple persona chatbot project with a Streamlit frontend and a CLI backend.

## Project Structure

- `app.py` — Streamlit frontend interface for chatting with Ashish Baliyan.
- `main.py` — CLI backend script for running the persona chatbot from terminal.
- `.env` — environment file containing `OPENAI_API_KEY`.

## Prerequisites

- Python 3.10+ installed
- Virtual environment created in `.venv`
- OpenAI API key available in `.env`

## Setup

1. Activate the project virtual environment:

```bash
cd /var/www/html/personaAI
source .venv/bin/activate
```

2. Install dependencies if needed:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install directly:

```bash
pip install openai streamlit python-dotenv
```

3. Ensure `.env` contains your OpenAI key:

```env
OPENAI_API_KEY=your_api_key_here
```

## Frontend (Streamlit)

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open the browser link shown in the terminal, usually `http://localhost:8501`.

## Backend (CLI)

Run the terminal chatbot directly:

```bash
python main.py
```

This starts the command-line persona chatbot and uses the OpenAI API key from `.env`.

## Notes

- The frontend is designed for an interactive browser experience.
- The backend is a simple terminal-based persona chatbot.
- The assistant persona is configured as **Ashish Baliyan**.

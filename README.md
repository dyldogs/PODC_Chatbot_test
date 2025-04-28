# PODC AI Assistant Chatbot

Full-stack chatbot application for Parents of Deaf Children (PODC), built with Flask and OpenAI.

## Project Structure
```
PODC_Chatbot/
├── backend/           # Flask server with OpenAI integration
├── frontend/         # Static web interface
├── render.yaml       # Render deployment configuration
└── README.md        # This file
```

## Quick Start

### Local Development
1. Clone the repository:
```bash
git clone https://github.com/yourusername/PODC_Chatbot.git
cd PODC_Chatbot
```

2. Set up the backend:
```bash
cd backend
pip install -r requirements.txt
# Create .env file with your OpenAI API key
echo OPENAI_API_KEY=your_key_here > .env
python server.py
```

3. Set up the frontend:
- Open `frontend/index.html` in a browser
- For local testing, update API endpoint in `script.js` to `http://localhost:5000`

## Deployment
This project is configured for deployment on Render.com as two services from a single repository:

### URLs
- Frontend: https://podc-chatbot-frontend.onrender.com
- Backend: https://podc-chatbot-backend.onrender.com

### Environment Variables
Required in Render dashboard:
- `OPENAI_API_KEY`: Your OpenAI API key
- `PORT`: Set by Render automatically

## Tech Stack
- **Backend**
  - Python 3.9.18
  - Flask + Flask-CORS
  - OpenAI API
  - Gunicorn (Linux) / Waitress (Windows)
- **Frontend**
  - HTML5
  - CSS3
  - JavaScript
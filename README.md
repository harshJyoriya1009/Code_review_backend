# AI Code Reviewer — Backend + AI Agent

This repository contains the backend API and AI agent integration for the AI Code Review Agent project.

The backend accepts a GitHub repository + file path, sends it to an AI workflow (n8n), and returns a structured JSON response including:
Overall score (0–10)
Summary
Issues list
Suggestions list
Categories (Security / Performance / Code Quality / General)

# 🚀 Features
Django REST API endpoint
✅ Integrates with n8n webhook AI agent 
✅ Handles CORS + OPTIONS preflight 
✅ Normalizes AI output for frontend safety 
✅ Returns clean structured JSON 
✅ Works with Postman + React frontend 

# 🏗️ Tech Stack
Python, 
Django, 
Requests, 
n8n (local AI workflow), 
JSON API, 

# 📌 API Endpoint
Request Body
```bash
{
  "repo_path": "username/repository",
  "file": "script.js"
}
```

Response Example
```bash
{
  "overall_score": 7,
  "summary": "The code is mostly clean but contains some security and performance issues.",
  "issues": [
    {
      "category": "Security",
      "description": "Replace Math.random() with crypto.getRandomValues()."
    }
  ],
  "suggestions": [
    {
      "description": "Use navigator.clipboard.writeText() instead of document.execCommand()."
    }
  ]
}
```

# ⚙️ Setup Instructions
### 1️⃣ Clone the repository
```bash
https://github.com/harshJyoriya1009/Code_review_backend.git
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
```

### 3️⃣ Activate venv
```bash
venv\Scripts\activate
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run Django server
```bash
python manage.py runserver
```

Backend will run at:
http://localhost:8000








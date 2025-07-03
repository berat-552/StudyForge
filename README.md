﻿# StudyForge - AI Study Content Generator

A standalone AI-powered Windows app used by friends and family to generate flashcards from raw text using LLM integration.

---

## 🖥️ Running Locally (Development)

### ✅ Prerequisites

- Python 3.11+
- A [Cohere](https://cohere.com/) API key
- Docker (optional, for containerised backend)
- Git
- Virtual environment set up (recommended)

---

### ⚙️ 1. Clone the repository

```bash
git clone https://github.com/berat-552/StudyForge.git
cd StudyForge
```

### 📦 2. Install dependencies
```bash
python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt
```

### 🔑 3. Set up environment variables
Create a .env file in the project root (you can copy from .env.example):

```bash
copy .env.example .env # command for cmd.exe
```

Then update the .env file with your Cohere API key:

```env
COHERE_API_KEY=your-cohere-key-here
APP_ENV=dev
DEV_API_URL=http://127.0.0.1:8000
PROD_API_URL=https://studyforge-api.onrender.com
```

### 🚀 4. Start the app (Backend + GUI)
Use the batch script to launch everything:

```bash
run-dev.bat
```
This will start the FastAPI backend in a new terminal window. 

Then it will launch the GUI.

When you close the GUI, the backend will keep running in its terminal.

### 🐳 Running with Docker (Alternative Dev Option)
If you want to run the backend in a container:

#### 🛠️ Build the Docker image
```bash
make docker-build
```

#### ▶️ Run the container + launch GUI
```bash
make dev-docker
```
This runs the container in the background and launches the GUI.

When the GUI closes, the container is stopped automatically.

#### 🛑 Manually Stop the Docker Container (if needed)
```bash
make docker-stop
```
#### 🧪 Running Tests
```bash
make test
```

#### 🧹 Format the Code
```bash
make format
```

Check out the [Makefile](./Makefile) for more commands.

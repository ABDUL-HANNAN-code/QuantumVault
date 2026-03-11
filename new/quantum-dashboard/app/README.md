# 🚀 QuantumVault — How to Run This Project

## 💡 What Is This Project?
**QuantumVault** is a futuristic memory/time capsule platform with:
- 🔮 **Quantum Circuits** — Run quantum simulations using Qiskit
- 🕰️ **Time Capsules** — Seal memories to be unlocked at a future date
- 💬 **Real-Time Chat** — WebSocket + SSE powered chat between users
- 🔐 **Vault System** — Encrypted personal data vault
- 🤝 **Friendships & Notifications** — Social features
- 🌐 **Cyberpunk UI** — Dark neon-themed HTML frontend with 3 themes

**Tech Stack:**
- **Backend:** Python FastAPI + MongoDB + Redis + WebSockets
- **Frontend:** Pure HTML/JS/TailwindCSS (no framework needed)
- **Deploy:** Docker Compose (easiest) or Manual (Python)

---

## ✅ Prerequisites — Install These First

### Option A: Docker (Recommended — Easiest)
1. Install **Docker Desktop**: https://www.docker.com/products/docker-desktop
2. That's it! Docker handles MongoDB, Redis, and everything else.

### Option B: Manual Setup
Install all of these:
- **Python 3.11**: https://www.python.org/downloads/
- **MongoDB**: https://www.mongodb.com/try/download/community
- **Redis**: https://redis.io/download (Windows: use Redis for Windows or WSL)
- **Node.js** (only needed if you want to serve frontend): https://nodejs.org

---

## 🐳 Method 1: Run with Docker (Recommended)

### Step 1 — Navigate to the project folder
```bash
cd DB-FINAL-PROJECT/new/quantum-dashboard
```

### Step 2 — Create the `.env` file (already included!)
The `.env` file is already in the project. You can use it as-is for local testing.
If you want to change passwords, open `.env` and edit the values.

### Step 3 — Start everything with one command
```bash
docker compose up --build
```
This will:
- Build the FastAPI backend
- Start MongoDB on port 27017
- Start Redis on port 6379
- Start the API on **http://localhost:8000**

> ⏳ First run takes 3–5 minutes to download images and install packages.

### Step 4 — Open the Frontend
Open the frontend HTML file directly in your browser:
```
DB-FINAL-PROJECT/new/frontend/index.html
```
Just double-click it, or drag it into Chrome/Firefox.

### Step 5 — Explore the API Docs
FastAPI comes with built-in interactive docs:
```
http://localhost:8000/docs
```

### Stop the project
```bash
docker compose down
```

---

## 🐍 Method 2: Run Manually (Without Docker)

Use this if you don't want Docker or are on a slow machine.

### Step 1 — Make sure MongoDB is running
Start MongoDB on your machine (it runs on port 27017 by default).

### Step 2 — Make sure Redis is running
Start Redis on your machine (it runs on port 6379 by default).

### Step 3 — Navigate to the backend folder
```bash
cd DB-FINAL-PROJECT/new/quantum-dashboard
```

### Step 4 — Create a Python virtual environment
```bash
python -m venv venv
```

Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### Step 5 — Install dependencies
```bash
pip install -r requirements.txt
```
> ⚠️ This installs Qiskit which is large (~500MB). Be patient.

### Step 6 — Update the `.env` file for local connection
Open `.env` and change the MongoDB/Redis URLs from container names to localhost:

```env
MONGODB_URL=mongodb://localhost:27017/quantum_dashboard_prod
REDIS_URL=redis://localhost:6379
```

Remove the `REDIS_PASSWORD` line or leave it blank if your local Redis has no password.

Also update `ALLOWED_HOSTS`:
```env
ALLOWED_HOSTS=["localhost", "127.0.0.1", "*"]
```

### Step 7 — Run the backend
```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Step 8 — Open the Frontend
Open `DB-FINAL-PROJECT/new/frontend/index.html` in your browser.

---

## 🔌 How Frontend Connects to Backend

The frontend (`app.js`) talks to the backend via `http://localhost:8000`.

Check `DB-FINAL-PROJECT/new/frontend/app.js` — look for a line like:
```javascript
const API_URL = "http://localhost:8000";
```
If it's pointing somewhere else, change it to `http://localhost:8000`.

---

## 🗂️ Project Structure

```
DB-FINAL-PROJECT/
├── new/
│   ├── frontend/
│   │   ├── index.html          ← Open this in browser
│   │   └── app.js              ← All frontend JS logic
│   └── quantum-dashboard/
│       ├── app/
│       │   ├── main.py         ← FastAPI entry point
│       │   ├── database.py     ← MongoDB connection
│       │   ├── models/         ← Data models (User, Capsule, Quantum...)
│       │   ├── routers/        ← API endpoints (auth, chat, capsules...)
│       │   ├── services/       ← Business logic
│       │   └── utils/          ← Redis, security, helpers
│       ├── docker-compose.yml  ← Run everything with Docker
│       ├── requirements.txt    ← Python packages
│       ├── .env                ← Config & secrets
│       └── init-mongo.js       ← DB initialization script
```

---

## 🐛 Common Issues & Fixes

### ❌ "Cannot connect to MongoDB"
- Docker method: Make sure Docker Desktop is running before `docker compose up`
- Manual method: Start MongoDB service: `mongod --dbpath /data/db`

### ❌ "Redis connection refused"
- Docker method: It starts automatically — check `docker compose ps`
- Manual method: Start Redis: `redis-server`

### ❌ "CORS error" in browser console
Open `app/main.py` — the CORS is already set to `allow_origins=["*"]` so this should not happen. If it does, make sure you're accessing the frontend via `http://` not `file://`. Use VS Code Live Server or:
```bash
python -m http.server 5500
# Then open http://localhost:5500
```

### ❌ Qiskit install fails
Try:
```bash
pip install qiskit==0.45.1 --no-cache-dir
```
Or skip it temporarily by commenting out the `qiskit` import in `app/routers/quantum.py`.

### ❌ Port 8000 already in use
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:8000 | xargs kill
```

---

## 🧪 Test the API is Working

Visit: `http://localhost:8000/health`

You should see:
```json
{
  "status": "healthy",
  "quantum_coherence": "stable",
  "temporal_integrity": "maintained",
  "chat_system": "active",
  "redis_connection": "established"
}
```

Also try the interactive API explorer: `http://localhost:8000/docs`

---

## 🎮 Quick Start — First Things to Do

1. **Register** a new account via the frontend or `/docs`
2. **Login** to get your JWT token
3. **Create a Time Capsule** — set a future unlock date
4. **Run a Quantum Circuit** — try the quantum simulation feature
5. **Add a friend** and test the **real-time chat**

---

## 📝 Summary

| Step | Command |
|------|---------|
| Go to project | `cd DB-FINAL-PROJECT/new/quantum-dashboard` |
| Start (Docker) | `docker compose up --build` |
| Start (Manual) | `uvicorn app.main:app --reload --port 8000` |
| API Docs | http://localhost:8000/docs |
| Health Check | http://localhost:8000/health |
| Frontend | Open `frontend/index.html` in browser |
| Stop (Docker) | `docker compose down` |
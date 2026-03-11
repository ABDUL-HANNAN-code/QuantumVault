<div align="center">

# ⚛️ QuantumVault

### *Preserve Memories Across Time and Space*

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-7.0-47A248?style=for-the-badge&logo=mongodb)](https://www.mongodb.com)
[![Redis](https://img.shields.io/badge/Redis-7.0-DC382D?style=for-the-badge&logo=redis)](https://redis.io)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker)](https://docker.com)
[![Qiskit](https://img.shields.io/badge/Qiskit-0.45.1-6929C4?style=for-the-badge&logo=ibm)](https://qiskit.org)

**A futuristic social platform where users seal memories into time-locked capsules, run quantum circuit simulations, and communicate in real-time  all wrapped in a cyberpunk UI.**

[Features](#-features) • [Tech Stack](#-tech-stack) • [Getting Started](#-getting-started) • [API Docs](#-api-documentation) • [Project Structure](#-project-structure)

</div>

---

## 🌌 What is QuantumVault?

QuantumVault is a **Database Systems final project** that blends cutting-edge technologies into a unique futuristic platform. Users can:

- 🔒 **Lock memories** into time capsules that cannot be opened until a set future date
- ⚛️ **Write and execute** real quantum circuits using Qiskit and OpenQASM
- 💬 **Chat in real-time** with friends using WebSockets and Server-Sent Events
- 🔐 **Store private data** in an encrypted personal vault with permission controls
- 🤝 **Connect with users** through a friends and social activity system
- 🌐 **Switch UI themes** — Dark, Light, and Cyberpunk modes

> **Why it's unique:** Most student projects use simple CRUD. QuantumVault integrates quantum computing simulation, real-time communication protocols, JWT-secured APIs, rate limiting, and a role-based permission system  all in one cohesive platform.

---

## ✨ Features

### 🕰️ Temporal Capsule System
- Create capsules of type: **Memory**, **Message**, **Image**, **File**, or **Quantum State**
- Capsules are **time-locked**  content is hidden until the unlock date arrives
- Tag, describe, and track capsule status: `locked` → `unlocked` → `expired`

### ⚛️ Quantum Circuit Engine
- Write quantum programs in **OpenQASM** syntax
- **Analyze** circuits: get qubit count, gate count, and circuit depth
- **Execute** circuits and receive measurement results with probabilities
- Powered by **Qiskit 0.45**  IBM's quantum computing SDK

### 💬 Real-Time Communication
- **WebSocket** chat for instant bidirectional messaging
- **SSE (Server-Sent Events)** for live notifications and activity feeds
- Chat history persistence in MongoDB
- Connection manager handles multiple concurrent users

### 🔐 Security & Auth
- **JWT Authentication** with configurable expiry
- **bcrypt** password hashing via Passlib
- **Rate limiting** (SlowAPI)  configurable per-minute request caps
- **TrustedHost middleware** protection

### 👥 Social Features
- Send/accept/reject **friend requests**
- View **activity feeds** and user profiles
- **Notification system** with real-time delivery
- Quantum connection level tracking per user

### 🔒 Personal Vault
- Store private items with custom `item_type` and structured data
- **Permission-based access control**  grant vault access to specific users
- Full audit trail via activity logs

### 🎨 Cyberpunk Frontend
- Pure **HTML + Vanilla JS + TailwindCSS** (zero framework dependencies)
- **3 themes**: Dark (default), Light, and Cyberpunk
- Custom fonts: Orbitron + Exo 2
- Fully responsive design

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend Framework** | FastAPI 0.104 |
| **Database** | MongoDB 7.0 (via Motor async driver) |
| **Cache / PubSub** | Redis 7.0 |
| **Quantum Engine** | Qiskit 0.45 + OpenQASM |
| **Auth** | JWT (python-jose) + bcrypt (passlib) |
| **Real-Time** | WebSockets + SSE (sse-starlette) |
| **Rate Limiting** | SlowAPI |
| **Frontend** | HTML5 + Vanilla JS + TailwindCSS CDN |
| **Containerization** | Docker + Docker Compose |
| **Reverse Proxy** | Nginx |
| **Monitoring** | Prometheus |
| **Testing** | Pytest + pytest-asyncio + HTTPX |

---

## 🚀 Getting Started

### Prerequisites

Choose one of these methods:

**Option A — Docker (Recommended)**
- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running

**Option B — Manual**
- Python 3.11+
- MongoDB running locally (port 27017)
- Redis running locally (port 6379)

---

### 🐳 Run with Docker

```bash
# 1. Clone the repository
git clone https://github.com/your-username/quantum-vault.git
cd quantum-vault/new/quantum-dashboard

# 2. Start all services (API + MongoDB + Redis + Nginx)
docker compose up --build

# 3. Open the frontend
# Just open: new/frontend/index.html in your browser
```

> ⏳ First build takes ~5 minutes. Subsequent starts are instant.

---

### 🐍 Run Manually

```bash
# 1. Navigate to backend
cd new/quantum-dashboard

# 2. Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate      # Windows (Git Bash)
source venv/bin/activate           # Mac / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Update .env for local connections
# Change MONGODB_URL to: mongodb://localhost:27017/quantum_dashboard_prod
# Change REDIS_URL to:   redis://localhost:6379

# 5. Start the server
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Then open `new/frontend/index.html` in your browser.

---

### ✅ Verify It's Running

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "quantum_coherence": "stable",
  "temporal_integrity": "maintained",
  "chat_system": "active",
  "redis_connection": "established"
}
```

---

## 📁 Project Structure

```
quantum-vault/
├── new/
│   ├── frontend/
│   │   ├── index.html              # Main UI (open this in browser)
│   │   └── app.js                  # All frontend logic
│   │
│   └── quantum-dashboard/          # Backend (FastAPI)
│       ├── app/
│       │   ├── main.py             # App entry point, middleware, routers
│       │   ├── config.py           # Settings from .env
│       │   ├── database.py         # MongoDB connection
│       │   │
│       │   ├── models/             # Pydantic data models
│       │   │   ├── user.py         # User, UserCreate, UserResponse
│       │   │   ├── capsule.py      # TemporalCapsule, CapsuleType
│       │   │   ├── quantum.py      # QuantumCircuit, QuantumMeasurement
│       │   │   ├── vault.py        # VaultItem
│       │   │   ├── chat.py         # ChatMessage, ChatRoom
│       │   │   ├── friendship.py   # FriendRequest, Friendship
│       │   │   └── notification.py # Notification
│       │   │
│       │   ├── routers/            # API endpoint handlers
│       │   │   ├── auth.py         # /auth — register, login, token
│       │   │   ├── users.py        # /users — profiles, search
│       │   │   ├── capsules.py     # /capsules — CRUD + unlock logic
│       │   │   ├── quantum.py      # /quantum — analyze + execute circuits
│       │   │   ├── vault.py        # /vault — private storage
│       │   │   ├── chat.py         # /chat — message history
│       │   │   ├── websocket.py    # /ws — real-time WebSocket
│       │   │   ├── sse.py          # /sse — Server-Sent Events
│       │   │   ├── friends.py      # /friends — social features
│       │   │   └── notifications.py# /notifications
│       │   │
│       │   ├── services/           # Business logic layer
│       │   │   ├── auth_service.py
│       │   │   ├── chat_service.py
│       │   │   ├── quantum_service.py
│       │   │   ├── connection_manager.py  # WebSocket connections
│       │   │   ├── permission_service.py
│       │   │   └── notification_service.py
│       │   │
│       │   └── utils/
│       │       ├── security.py     # JWT + password hashing
│       │       ├── redis_client.py # Redis connection wrapper
│       │       └── file_utils.py   # Upload handling
│       │
│       ├── tests/                  # Pytest test suite
│       ├── monitoring/             # Prometheus config
│       ├── docker-compose.yml      # Local dev containers
│       ├── docker-compose.prod.yml # Production containers
│       ├── Dockerfile
│       ├── nginx.conf
│       ├── requirements.txt
│       └── .env                    # Environment variables
```

---

## 📡 API Documentation

Once the server is running, visit the **interactive Swagger docs**:

```
http://localhost:8000/docs
```

Or the **ReDoc** version:
```
http://localhost:8000/redoc
```

### Key Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/register` | Create a new account |
| `POST` | `/auth/login` | Login and receive JWT token |
| `GET` | `/users/me` | Get current user profile |
| `POST` | `/capsules/` | Create a new time capsule |
| `GET` | `/capsules/` | List your capsules |
| `POST` | `/quantum/analyze` | Analyze a QASM circuit |
| `POST` | `/quantum/execute` | Execute a quantum circuit |
| `GET` | `/vault/` | View your private vault |
| `POST` | `/friends/request/{user_id}` | Send a friend request |
| `WS` | `/ws/{user_id}` | WebSocket chat connection |
| `GET` | `/sse/events` | Subscribe to live events |
| `GET` | `/health` | Health check |

---

## ⚙️ Environment Variables

The `.env` file controls all configuration:

```env
# MongoDB
MONGODB_URL=mongodb://admin:password@mongodb:27017/quantum_dashboard_prod?authSource=admin
DATABASE_NAME=quantum_dashboard_prod

# Redis
REDIS_URL=redis://redis:6379
REDIS_PASSWORD=your_redis_password

# JWT
JWT_SECRET_KEY=your_super_secret_key_min_32_chars
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60

# Rate Limiting
RATE_LIMIT_PER_MINUTE=120

# CORS
CORS_ORIGINS=["http://localhost:5500", "http://127.0.0.1:5500"]
```

---

## 🧪 Running Tests

```bash
cd new/quantum-dashboard
pytest tests/ -v
```

Test coverage includes:
- `test_api.py`  endpoint integration tests
- `test_models.py`  Pydantic model validation
- `test_integration.py`  full flow tests (auth → capsule → unlock)

---

## 🤝 Team

> Developed as a **Database Systems Final Project**

---

## 📄 License

This project is for educational purposes as part of a university Database Systems course.

---

<div align="center">

*"The past is preserved. The future is quantum."*

⭐ Star this repo if you found it interesting!

</div>



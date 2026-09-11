# 🚀 Sanjay N — Personal Portfolio Website

A full-stack personal portfolio built with:
- **Frontend**: Plain HTML5 / CSS3 / JavaScript (deployed on Vercel)
- **Backend**: Python + Django REST Framework (deployed on Render)
- **Database**: MySQL

---

## 📁 Project Structure

```
portfolio/
├── frontend/               ← Static site (Vercel)
│   ├── index.html
│   ├── css/style.css
│   └── js/main.js
├── backend/                ← Django REST API (Render)
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── portfolio_project/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── api/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── urls.py
│       └── admin.py
├── vercel.json
└── README.md
```

---

## ⚙️ Local Development Setup

### Prerequisites
- Python 3.10+
- MySQL Server (running locally)
- pip

---

### 1. MySQL — Create the Database

Open MySQL shell or MySQL Workbench and run:

```sql
CREATE DATABASE portfolio_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

### 2. Backend Setup (Django)

```bash
# Navigate to backend
cd backend

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment variables
copy .env.example .env
```

Open `.env` and fill in:
```env
SECRET_KEY=any-random-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=portfolio_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Seed with sample data
python manage.py seed_data

# Start the server
python manage.py runserver
```

Backend will be running at: **http://localhost:8000**

---

### 3. Frontend Setup

The frontend is plain HTML — just open the file in your browser:

- Open `frontend/index.html` in your browser
- Or use VS Code Live Server: right-click `index.html` → **Open with Live Server**

> The frontend auto-connects to `http://localhost:8000/api` by default.

---

### 4. API Endpoints (available at `http://localhost:8000/api/`)

| Method | Endpoint           | Description                    |
|--------|--------------------|--------------------------------|
| GET    | `/api/profile/`    | Hero/About profile info        |
| GET    | `/api/projects/`   | All featured projects          |
| GET    | `/api/skills/`     | All skills (grouped by cat)    |
| GET    | `/api/experience/` | All experience entries         |
| GET    | `/api/education/`  | All education entries          |
| POST   | `/api/contact/`    | Submit a contact message       |

---

### 5. Django Admin Panel

Visit **http://localhost:8000/admin/** to manage all your portfolio content:
- Add/edit/delete projects
- Add/edit skills
- Manage experience & education
- Read contact messages

---

## 🌐 Deployment Guide

### Frontend → Vercel

1. Push your project to GitHub
2. Go to [vercel.com](https://vercel.com) → **New Project**
3. Import your GitHub repo
4. Set **Root Directory** to `frontend` (or use the `vercel.json` at root)
5. Click **Deploy** ✅

---

### Backend → Render

1. Go to [render.com](https://render.com) → **New Web Service**
2. Connect your GitHub repo
3. Set **Root Directory**: `backend`
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `gunicorn portfolio_project.wsgi:application`
6. Add **Environment Variables** in Render dashboard:
   - `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS=your-app.onrender.com`
   - All `DB_*` variables pointing to your hosted MySQL

---

### Free MySQL Hosting Options for Render

| Provider | Free Tier | Notes |
|---|---|---|
| [PlanetScale](https://planetscale.com) | 5 GB | MySQL-compatible, great for hobby projects |
| [Clever Cloud](https://clever-cloud.com) | MySQL add-on | Free tier available |
| [FreeSQLDatabase.com](https://freesqldatabase.com) | 5 MB | Basic, for testing |
| [Render PostgreSQL](https://render.com/docs/databases) | Free 90 days | If you switch to PostgreSQL |

---

### After Deploying Backend

Update `frontend/js/main.js`:
```js
// Change this line:
const API_BASE = 'http://localhost:8000/api';
// To your Render URL:
const API_BASE = 'https://your-api.onrender.com/api';
```

And update `backend/.env` `CORS_ALLOWED_ORIGINS` to include your Vercel URL.

---

## 🔧 Customisation

Update your personal info in:
- `frontend/index.html` — name, bio, social links
- `backend/api/views.py` — `PROFILE_DATA` dictionary
- **Django Admin** → add/edit Projects, Skills, Experience, Education

---

## 📄 License

MIT License — Free to use and modify.

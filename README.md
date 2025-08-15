# Tenax - Educational MVP Platform

A modern educational MVP platform built with FastAPI backend and React frontend, designed to help students optimize their learning experience through personalized profiles and smart integrations.

## 🚀 Features

- **Student System Profiles**: Personalized learning profiles with study styles and preferences
- **Modern Tech Stack**: FastAPI + React + PostgreSQL + Vite
- **Database Migrations**: Alembic for version-controlled database schema
- **Type Safety**: Pydantic schemas for data validation
- **API Documentation**: Auto-generated OpenAPI/Swagger docs
- **Development Ready**: Hot reload, CORS configured, and development tools

## 🏗️ Architecture

```
Tenax/
├── backend/           # FastAPI REST API
│   ├── app/
│   │   ├── api/       # API endpoints
│   │   ├── core/      # Core configuration
│   │   ├── database/  # Database configuration
│   │   ├── models/    # SQLAlchemy models
│   │   ├── schemas/   # Pydantic schemas
│   │   └── services/  # Business logic
│   ├── alembic/       # Database migrations
│   └── requirements.txt
├── frontend/          # React + Vite SPA
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── package.json
└── README.md
```

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **PostgreSQL** - Production-ready database
- **Alembic** - Database migration tool
- **Pydantic** - Data validation using Python type hints

### Frontend
- **React 18** - UI library
- **TypeScript** - Type-safe JavaScript
- **Vite** - Fast build tool and dev server
- **Modern CSS** - Responsive design

## 📋 Prerequisites

- Python 3.12+
- Node.js 18+
- PostgreSQL 14+
- Git

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/tenax.git
cd tenax
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your database credentials

# Run database migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### 4. Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📊 Database Schema

### StudentSystemProfile Model

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Primary key (auto-increment) |
| `user_id` | String(255) | User identifier |
| `study_style` | Enum | Learning style (visual, auditory, kinesthetic, mixed) |
| `preferred_times` | JSON | Study time preferences |
| `tools_connected` | JSON | Connected learning tools |
| `goals` | Text | Student learning goals |
| `created_at` | DateTime | Record creation timestamp |
| `updated_at` | DateTime | Last update timestamp |

## 🔗 API Endpoints

### Student Profiles

- `POST /api/v1/student-profiles/` - Create a new student profile
- `GET /api/v1/student-profiles/{id}` - Get student profile by ID
- `GET /api/v1/student-profiles/` - List all student profiles

### Health Check

- `GET /` - Basic health check
- `GET /health` - Detailed health status

## 🧪 Development

### Database Migrations

```bash
# Generate new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### Running Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## 🌍 Environment Variables

Create a `.env` file in the `backend/` directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/tenax_db
```

## 📝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

If you have any questions or need help, please:

1. Check the [documentation](docs/)
2. Search existing [issues](https://github.com/yourusername/tenax/issues)
3. Create a new issue if needed

## 🎯 Roadmap

- [ ] User authentication system
- [ ] Advanced learning analytics
- [ ] Third-party integrations (Notion, Google Calendar)
- [ ] Mobile app
- [ ] AI-powered study recommendations

---

Built with ❤️ for the global education community 
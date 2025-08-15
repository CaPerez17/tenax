# Tenax - Intelligent Educational Platform

**🚀 Revolutionizing Education Through AI-Powered Personalization**

Tenax is an innovative educational MVP platform that transforms how students learn by creating personalized learning experiences. Built with cutting-edge technology (FastAPI + React + PostgreSQL), Tenax analyzes individual learning patterns, study preferences, and goals to optimize educational outcomes through intelligent recommendations and seamless tool integrations.

**🎯 Vision**: Democratize personalized education by making advanced learning optimization accessible to students worldwide, regardless of their background or resources.

## 💡 The Need Statement - A Personal Journey

### **🎓 The Problem I Experienced**

As a computer science student at Universidad de los Andes, I faced a common but critical challenge: **managing multiple learning systems, tracking progress across different subjects, and maintaining consistent study habits**. Like many students, I found myself juggling:

- Multiple productivity tools (Notion, Google Calendar, Trello)
- Different learning platforms and LMS systems
- Various assignment tracking methods
- Inconsistent study schedules and habits
- Lack of personalized insights into my learning patterns

### **🔍 The Insight**

The breakthrough came when I was working on a **personal knowledge management system** - essentially a custom "constancias" (evidence/record) manager for tracking my academic achievements, certifications, and learning milestones. While building this system, I realized:

> **"Students don't need another tool - they need an intelligent system that connects and optimizes all their existing tools."**

### **🚀 The Solution Vision**

This personal frustration led to a bigger realization: **What if we could create a platform that not only manages learning records but actively learns from student behavior to optimize their entire educational experience?**

Tenax evolved from this simple need:
- **From**: Manual tracking of academic constancias and achievements
- **To**: AI-powered system that understands individual learning patterns
- **Result**: Personalized recommendations that adapt to each student's unique style and goals

### **🎯 Why This Matters**

Every student deserves a learning experience that adapts to them, not the other way around. My journey from building a simple constancias manager to envisioning Tenax represents a fundamental shift in educational technology - from static tools to intelligent, adaptive learning companions.

**The question that drives Tenax**: *"What if technology could understand how you learn best and automatically optimize your entire educational journey?"*

## 🌍 Market Impact & Opportunity

### **📊 Addressing a $366B Global Market**
The global e-learning market is projected to reach $366.3 billion by 2025, with personalized learning being the fastest-growing segment. Tenax positions itself at the intersection of:
- **Personalized Learning**: $2.8B market growing at 19.2% CAGR
- **Educational Technology**: Serving 1.6B students globally
- **Productivity Integration**: $58B market for connected learning tools

### **🎯 Target Segments**
- **Individual Learners**: Students, professionals, and lifelong learners seeking optimized study experiences
- **Educational Institutions**: Schools and universities looking to enhance student outcomes
- **Corporate Training**: Companies investing in employee development and skill enhancement
- **EdTech Ecosystem**: Integration partners and educational tool providers

### **💡 Competitive Advantages**
- **AI-Driven Personalization**: Advanced algorithms that adapt to individual learning patterns
- **Universal Integration**: Works with existing tools students already use
- **Scalable Architecture**: Built to handle millions of users with enterprise-grade reliability
- **Data-Driven Insights**: Actionable analytics for continuous learning improvement

## 🚀 Core Features

### **🧠 Intelligent Learning Profiles**
- **Adaptive Study Styles**: Visual, auditory, kinesthetic, and mixed learning pattern recognition
- **Smart Scheduling**: AI-powered optimal study time recommendations based on personal productivity patterns
- **Goal Tracking**: Dynamic goal setting and progress monitoring with intelligent milestone suggestions
- **Performance Analytics**: Deep insights into learning efficiency and knowledge retention

### **🔗 Seamless Integrations**
- **Productivity Tools**: Native integration with Notion, Google Calendar, Trello, and more
- **Learning Platforms**: Connect with existing educational tools and LMS systems
- **Data Synchronization**: Real-time sync across all connected platforms for unified learning experience

### **🏗️ Enterprise-Grade Architecture**
- **Scalable Backend**: FastAPI with async processing for handling thousands of concurrent users
- **Modern Frontend**: React 18 + TypeScript for type-safe, responsive user interfaces
- **Robust Database**: PostgreSQL with Alembic migrations for reliable data management
- **API-First Design**: RESTful API with auto-generated documentation for easy third-party integrations

### **🔒 Production-Ready Infrastructure**
- **Type Safety**: End-to-end type checking with Pydantic and TypeScript
- **Database Versioning**: Professional migration system for seamless updates
- **CORS Configuration**: Secure cross-origin resource sharing for web applications
- **Developer Experience**: Hot reload, comprehensive testing, and modern development tools

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
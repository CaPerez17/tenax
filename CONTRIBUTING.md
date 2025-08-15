# Contributing to Tenax

Thank you for your interest in contributing to Tenax! This document provides guidelines and instructions for contributing to the project.

## 🚀 Quick Start for Contributors

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/tenax.git
cd tenax
```

### 2. Set Up Development Environment

```bash
# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install
```

### 3. Create Environment Variables

```bash
# Copy example environment file
cp backend/.env.example backend/.env
# Edit backend/.env with your database credentials
```

### 4. Set Up Database

```bash
cd backend
# Make sure PostgreSQL is running
# Create database
createdb tenax_db

# Run migrations
alembic upgrade head
```

## 📝 Development Workflow

### Branch Naming Convention

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring
- `test/description` - Test improvements

### Commit Message Format

```
type(scope): brief description

Detailed description of changes (optional)

Closes #issue_number (if applicable)
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(api): add student profile CRUD endpoints

Add complete CRUD operations for student profiles including:
- Create new profile
- Get profile by ID
- List all profiles
- Update profile
- Delete profile

Closes #123
```

## 🧪 Testing

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

### Running Linters

```bash
# Backend
cd backend
flake8 app/
black app/
isort app/

# Frontend
cd frontend
npm run lint
npm run type-check
```

## 📊 Code Quality Standards

### Python (Backend)

- Follow PEP 8 style guide
- Use type hints for all functions
- Write docstrings for all public functions
- Keep functions small and focused
- Use meaningful variable names

### TypeScript (Frontend)

- Use TypeScript strict mode
- Define interfaces for all data structures
- Use functional components with hooks
- Follow React best practices
- Use meaningful component and variable names

### Database

- Use descriptive table and column names
- Always create migrations for schema changes
- Include both `upgrade()` and `downgrade()` functions
- Test migrations on sample data

## 🔄 Pull Request Process

### Before Submitting

1. **Create a new branch** from `main`
2. **Make your changes** following the coding standards
3. **Add tests** for new functionality
4. **Update documentation** if needed
5. **Run all tests** and ensure they pass
6. **Run linters** and fix any issues
7. **Update CHANGELOG.md** if applicable

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
```

### Review Process

1. **Automated checks** must pass (CI/CD pipeline)
2. **Code review** by at least one maintainer
3. **Testing** on staging environment (if applicable)
4. **Approval** from project maintainers
5. **Merge** to main branch

## 🐛 Reporting Issues

### Bug Reports

When reporting bugs, please include:

1. **Clear title** describing the issue
2. **Steps to reproduce** the bug
3. **Expected behavior**
4. **Actual behavior**
5. **Environment details** (OS, Python version, Node version, etc.)
6. **Screenshots** if applicable
7. **Error logs** if available

### Feature Requests

When requesting features, please include:

1. **Clear title** describing the feature
2. **Problem description** - what problem does this solve?
3. **Proposed solution** - how should it work?
4. **Alternatives considered** - what other options did you think about?
5. **Additional context** - mockups, examples, etc.

## 📚 Development Resources

### Architecture Documentation

- [API Documentation](docs/api.md)
- [Database Schema](docs/database.md)
- [Frontend Architecture](docs/frontend.md)

### Useful Commands

```bash
# Generate new migration
cd backend
alembic revision --autogenerate -m "Description"

# Reset database (development only)
alembic downgrade base
alembic upgrade head

# Run development servers
cd backend && uvicorn app.main:app --reload
cd frontend && npm run dev
```

## 🤝 Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect different opinions and approaches

### Getting Help

- Check existing [issues](https://github.com/yourusername/tenax/issues)
- Join our [discussions](https://github.com/yourusername/tenax/discussions)
- Read the [documentation](docs/)

## 📄 License

By contributing to Tenax, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Tenax! 🚀 
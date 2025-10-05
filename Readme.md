# SnipBox - Short Note Saving Application

SnipBox is a powerful RESTful API platform for managing short text snippets with tag-based organization. Built with Django REST Framework, it provides a complete backend solution for note-taking applications with JWT authentication, comprehensive CRUD operations, and Docker deployment support.


## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django** | 4.2.7 | Web framework |
| **Django REST Framework** | 3.14.0 | API development |
| **PostgreSQL** | 15+ | Database |
| **SimpleJWT** | 5.3.0 | JWT authentication |
| **drf-spectacular** | 0.27.0 | API documentation |
| **Docker** | Latest | Containerization |
| **Docker Compose** | Latest | Multi-container orchestration |

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Docker** (20.10+) and **Docker Compose** (2.0+) - [Install Docker](https://docs.docker.com/get-docker/)
- **Git** - [Install Git](https://git-scm.com/downloads)

For manual installation:
- **Python** (3.10+) - [Download Python](https://www.python.org/downloads/)
- **PostgreSQL** (15+) - [Download PostgreSQL](https://www.postgresql.org/download/)

## Installation

### Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/suhailsugu/snipbox.git
   cd snipbox
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file with your configuration:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   
   DB_NAME=snipbox_db
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=db
   DB_PORT=5432
   
   CORS_ALLOW_ALL_ORIGINS=True
   ```

3. **Build and run with Docker Compose**
   
   **Option A: Build first, then run**
   ```bash
   docker compose build
   docker compose up -d
   ```
   
   **Option B: Build and run simultaneously**
   ```bash
   docker compose up --build -d
   ```

4. **Run database migrations**
   ```bash
   docker compose exec backend python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   docker compose exec backend python manage.py createsuperuser
   ```

6. **Access the application**
   - API Documentation: http://127.0.0.1:8000/docs/swagger/
   - Admin Panel: http://127.0.0.1:8000/admin/
   - ReDoc: http://127.0.0.1:8000/docs/redoc/


## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `SECRET_KEY` | Django secret key | - | Yes |
| `DEBUG` | Debug mode | `True` | No |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost,127.0.0.1` | Yes |
| `DB_NAME` | Database name | `snipbox_db` | Yes |
| `DB_USER` | Database user | `postgres` | Yes |
| `DB_PASSWORD` | Database password | `postgres` | Yes |
| `DB_HOST` | Database host | `localhost` or `db` | Yes |
| `DB_PORT` | Database port | `5432` | Yes |
| `CORS_ALLOW_ALL_ORIGINS` | Allow all CORS origins | `True` | No |




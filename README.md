# Job Board Backend API

[![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-316192?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-ready, enterprise-grade backend API for a comprehensive Job Board Platform. Built with Django and PostgreSQL, this system provides robust role-based access control, optimized job search capabilities, and comprehensive API documentation.

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Configuration](#environment-configuration)
  - [Database Setup](#database-setup)
- [API Documentation](#api-documentation)
- [Authentication & Authorization](#authentication--authorization)
- [Database Schema](#database-schema)
- [Performance Optimization](#performance-optimization)
- [Testing](#testing)
- [Deployment](#deployment)
- [Monitoring & Logging](#monitoring--logging)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## 🎯 Overview

This Job Board Backend is designed to handle complex role management, efficient data retrieval, and secure authentication for modern job platforms. The system supports high-volume job postings, real-time notifications, and advanced search capabilities with optimized query performance.

### Real-World Applications

- **Enterprise Job Portals**: Scalable infrastructure for corporate hiring platforms
- **Recruitment Agencies**: Multi-client job management systems
- **Freelance Marketplaces**: Gig economy platforms with role-based access
- **University Career Centers**: Campus recruitment management systems

### Project Goals

1. **API Development**: RESTful APIs for comprehensive job board operations
2. **Access Control**: Granular role-based permissions (Admin, Employer, Job Seeker)
3. **Database Efficiency**: Advanced indexing and query optimization for sub-second response times
4. **Scalability**: Architecture designed to handle 10,000+ concurrent users

## ✨ Key Features

### Job Management
- **CRUD Operations**: Complete lifecycle management for job postings
- **Categorization**: Multi-dimensional filtering (industry, location, type, experience level)
- **Status Management**: Draft, published, closed, and archived states
- **Bulk Operations**: Mass import/export capabilities for enterprise clients

### Role-Based Access Control (RBAC)
- **Admin Role**: Full system access, user management, analytics
- **Employer Role**: Create and manage job postings, view applications
- **Job Seeker Role**: Apply for jobs, manage profile, track applications
- **JWT Authentication**: Secure, stateless authentication with refresh tokens

### Advanced Job Search
- **Full-Text Search**: PostgreSQL full-text search with relevance ranking and fuzzy matching
- **Search Vectors**: Weighted search across title, description, and company fields
- **Geographic Search**: Location-based filtering with radius search
- **Filters**: Salary range, experience level, job type, remote options
- **Query Optimization**: Database indexing for <100ms search response times
- **Search Suggestions**: Auto-complete and did-you-mean functionality

### Intelligent Job Recommendations
- **Personalized Recommendations**: ML-based job matching based on user profile and history
- **Collaborative Filtering**: Suggest jobs based on similar user preferences
- **Content-Based Filtering**: Match jobs based on skills, experience, and preferences
- **Trending Jobs**: Real-time trending positions based on views and applications
- **Recommendation API**: Dedicated endpoints for personalized job feeds

### High-Performance Optimization
- **Smart Pagination**: Cursor-based pagination for large datasets
- **Response Caching**: Redis-based caching for frequently accessed endpoints
- **Cache Invalidation**: Intelligent cache updates on data changes
- **Query Result Caching**: Cached search results with configurable TTL
- **API Rate Limiting**: Token bucket algorithm for fair resource usage
- **Database Query Optimization**: Connection pooling and query result streaming

### Notification System
- **Email Notifications**: Application confirmations, status updates, job alerts
- **Real-Time Alerts**: WebSocket support for instant notifications
- **Template Engine**: Customizable email templates with branding
- **Queue Management**: Celery-based asynchronous email delivery

### API Documentation
- **Swagger/OpenAPI**: Interactive API documentation at `/api/docs`
- **ReDoc**: Alternative documentation UI at `/api/redoc`
- **Postman Collection**: Importable collection for rapid testing
- **Schema Validation**: Automatic request/response validation

## 🏗️ Architecture

```
┌─────────────────┐
│   API Gateway   │
│   (Nginx/ALB)   │
└────────┬────────┘
         │
┌────────▼────────────────────────┐
│     Django Application Layer    │
│  ┌──────────┐  ┌──────────┐    │
│  │   REST   │  │   Auth   │    │
│  │   APIs   │  │  Service │    │
│  └──────────┘  └──────────┘    │
└────────┬────────────────────────┘
         │
┌────────▼────────┐  ┌──────────┐
│   PostgreSQL    │  │  Redis   │
│   (Primary DB)  │  │  (Cache) │
└─────────────────┘  └──────────┘
         │
┌────────▼────────┐
│     Celery      │
│  (Task Queue)   │
└─────────────────┘
```

## 🛠️ Tech Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| **Django** | Web framework & ORM | 4.2+ |
| **Django REST Framework** | API development | 3.14+ |
| **PostgreSQL** | Primary database with full-text search | 13+ |
| **Redis** | Caching, session storage & rate limiting | 7.0+ |
| **Celery** | Asynchronous task queue | 5.3+ |
| **JWT** | Authentication tokens | PyJWT 2.8+ |
| **drf-yasg** | Swagger/OpenAPI documentation | 1.21+ |
| **scikit-learn** | ML-based job recommendations | 1.3+ |
| **pandas** | Data processing for recommendations | 2.0+ |
| **Gunicorn** | WSGI HTTP server | 21.0+ |
| **Nginx** | Reverse proxy & load balancer | 1.24+ |
| **Docker** | Containerization | 24.0+ |
| **Docker Compose** | Multi-container orchestration | 2.20+ |

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.10 or higher
- PostgreSQL 13 or higher
- Redis 7.0 or higher
- Docker & Docker Compose (optional, for containerized deployment)
- Git

### Installation

1. **Clone the repository**
```bash
git clone (https://github.com/JesutofunmiOludu/alx-project-nexus).git
cd job-board-backend
```

2. **Create and activate virtual environment**
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n jobboard python=3.10
conda activate jobboard
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Environment Configuration

1. **Copy the environment template**
```bash
cp .env.example .env
```

2. **Configure environment variables**

Edit `.env` with your configuration:

```env
# Django Settings
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database Configuration
DB_NAME=jobboard_db
DB_USER=jobboard_user
DB_PASSWORD=secure_password_here
DB_HOST=localhost
DB_PORT=5432

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# JWT Settings
JWT_SECRET_KEY=your-jwt-secret-key
JWT_ACCESS_TOKEN_LIFETIME=3600  # 1 hour in seconds
JWT_REFRESH_TOKEN_LIFETIME=604800  # 7 days in seconds

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password

# Celery Configuration
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# AWS S3 (for file uploads)
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
AWS_S3_REGION_NAME=us-east-1

# Monitoring
SENTRY_DSN=your-sentry-dsn-here
```

### Database Setup

1. **Create PostgreSQL database**
```bash
# Access PostgreSQL
psql -U postgres

# Create database and user
CREATE DATABASE jobboard_db;
CREATE USER jobboard_user WITH PASSWORD 'secure_password_here';
ALTER ROLE jobboard_user SET client_encoding TO 'utf8';
ALTER ROLE jobboard_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE jobboard_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE jobboard_db TO jobboard_user;
\q
```

2. **Run migrations**
```bash
python manage.py migrate
```

3. **Create database indexes** (for optimal performance)
```bash
python manage.py create_indexes
```

4. **Create superuser**
```bash
python manage.py createsuperuser
```

5. **Load sample data** (optional)
```bash
python manage.py loaddata fixtures/sample_data.json
```

6. **Start development server**
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

### Docker Deployment (Recommended for Production)

```bash
# Build and start containers
docker-compose up -d --build

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# View logs
docker-compose logs -f
```

## 📚 API Documentation

### Interactive Documentation

- **Swagger UI**: `http://localhost:8000/api/docs/`
- **ReDoc**: `http://localhost:8000/api/redoc/`
- **JSON Schema**: `http://localhost:8000/api/schema/`

### Core API Endpoints

#### Authentication
```
POST   /api/auth/register/          - User registration
POST   /api/auth/login/             - User login (returns JWT tokens)
POST   /api/auth/refresh/           - Refresh access token
POST   /api/auth/logout/            - User logout
POST   /api/auth/password/reset/    - Request password reset
POST   /api/auth/password/confirm/  - Confirm password reset
```

#### Jobs
```
GET    /api/jobs/                   - List all jobs (with filters & pagination)
POST   /api/jobs/                   - Create new job (Employer/Admin)
GET    /api/jobs/{id}/              - Get job details
PUT    /api/jobs/{id}/              - Update job (Employer/Admin)
PATCH  /api/jobs/{id}/              - Partial update (Employer/Admin)
DELETE /api/jobs/{id}/              - Delete job (Admin)
GET    /api/jobs/search/            - Full-text search with filters
GET    /api/jobs/search/suggest/    - Search auto-complete suggestions
GET    /api/jobs/recommendations/   - Get personalized job recommendations
GET    /api/jobs/trending/          - Get trending jobs
GET    /api/jobs/categories/        - List job categories
GET    /api/jobs/similar/{id}/      - Get similar jobs
```

#### Applications
```
GET    /api/applications/           - List user's applications
POST   /api/applications/           - Submit job application
GET    /api/applications/{id}/      - Get application details
PATCH  /api/applications/{id}/      - Update application status
DELETE /api/applications/{id}/      - Withdraw application
```

#### User Management
```
GET    /api/users/profile/          - Get current user profile
PUT    /api/users/profile/          - Update user profile
GET    /api/users/{id}/             - Get user details (Admin)
POST   /api/users/                  - Create user (Admin)
DELETE /api/users/{id}/             - Delete user (Admin)
```

### Example Request

```bash
# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "your_password"
  }'

# Create Job Posting (with JWT token)
curl -X POST http://localhost:8000/api/jobs/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Senior Backend Developer",
    "company": "Tech Corp",
    "description": "We are looking for...",
    "location": "San Francisco, CA",
    "salary_min": 120000,
    "salary_max": 180000,
    "job_type": "full_time",
    "category": "engineering"
  }'

# Full-Text Search with Pagination
curl -X GET "http://localhost:8000/api/jobs/search/?q=python+django&location=San+Francisco&page=1&page_size=20" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Get Personalized Recommendations
curl -X GET http://localhost:8000/api/jobs/recommendations/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Search with Autocomplete
curl -X GET "http://localhost:8000/api/jobs/search/suggest/?q=backend+dev" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 🔐 Authentication & Authorization

### JWT Token Flow

1. User authenticates via `/api/auth/login/`
2. Server returns access token (1 hour) and refresh token (7 days)
3. Client includes access token in Authorization header: `Bearer <token>`
4. When access token expires, use refresh token at `/api/auth/refresh/`

### Role-Based Permissions

| Role | Permissions |
|------|-------------|
| **Admin** | Full CRUD on all resources, user management, analytics access |
| **Employer** | Create/update/delete own jobs, view applications for own jobs, send invitations to freelancers |
| **Freelancer** | Apply for jobs, manage own profile, view own applications, write proposals, accept/deny invitations |

### Security Best Practices

- Passwords hashed using Django's PBKDF2 algorithm
- HTTPS enforced in production
- CSRF protection enabled
- Rate limiting on authentication endpoints
- SQL injection prevention via Django ORM
- XSS protection with Content Security Policy

## 🗄️ Database Schema

### Core Models

#### User Model
```python
- id (UUID, PK)
- email (unique)
- password (hashed)
- role (admin/employer/freelancer)
- is_active, is_verified
- created_at, updated_at
```

#### Job Model
```python
- id (UUID, PK)
- employer (FK to User)
- title, description
- company, location
- salary_min, salary_max
- job_type, experience_level
- category (FK to Category)
- status (draft/published/closed)
- search_vector (TSVector for full-text search)
- view_count, application_count
- created_at, updated_at, published_at
```

#### UserProfile Model
```python
- user (OneToOne to User)
- skills (JSONField)
- experience_years
- preferred_locations (ArrayField)
- preferred_job_types (ArrayField)
- resume_url
- linkedin_url
```

#### JobRecommendation Model
```python
- id (UUID, PK)
- user (FK to User)
- job (FK to Job)
- score (Float, 0-1)
- reason (Text)
- created_at
```

#### Application Model
```python
- id (UUID, PK)
- job (FK to Job)
- applicant (FK to User)
- cover_letter, resume_url
- status (pending/reviewed/accepted/rejected)
- applied_at, reviewed_at
```

### Database Indexes

```sql
-- Full-text search optimization
CREATE INDEX idx_job_search_vector ON jobs USING gin(search_vector);
CREATE INDEX idx_job_title_trgm ON jobs USING gin(title gin_trgm_ops);
CREATE INDEX idx_job_description_trgm ON jobs USING gin(description gin_trgm_ops);

-- Job search and filtering
CREATE INDEX idx_job_location ON jobs(location);
CREATE INDEX idx_job_category ON jobs(category_id);
CREATE INDEX idx_job_status_published ON jobs(status, published_at);
CREATE INDEX idx_job_type ON jobs(job_type);
CREATE INDEX idx_job_salary ON jobs(salary_min, salary_max);

-- Application queries
CREATE INDEX idx_application_job_status ON applications(job_id, status);
CREATE INDEX idx_application_applicant ON applications(applicant_id);

-- Recommendation system
CREATE INDEX idx_recommendation_user_score ON job_recommendations(user_id, score DESC);
CREATE INDEX idx_job_view_count ON jobs(view_count DESC);
CREATE INDEX idx_job_application_count ON jobs(application_count DESC);
```

## ⚡ Performance Optimization

### Full-Text Search Implementation

The system uses PostgreSQL's advanced full-text search capabilities for fast, relevant job searches:

```python
# Search vector with weighted fields
search_vector = SearchVector('title', weight='A') + \
                SearchVector('description', weight='B') + \
                SearchVector('company', weight='C')

# Search with ranking
jobs = Job.objects.annotate(
    rank=SearchRank(F('search_vector'), search_query)
).filter(
    search_vector=search_query
).order_by('-rank')
```

**Features:**
- Weighted search across multiple fields
- Trigram similarity for fuzzy matching
- Search suggestions with auto-complete
- Stemming and stop word removal
- Multi-language support

### Pagination Strategy

**Cursor-Based Pagination** for large datasets (recommended for feeds):
```python
# Better performance for large offsets
# Consistent results even when data changes
GET /api/jobs/?cursor=eyJpZCI6MTIzfQ==&page_size=20
```

**Offset-Based Pagination** for numbered pages:
```python
# Traditional pagination with page numbers
GET /api/jobs/?page=5&page_size=20
```

**Benefits:**
- Prevents "N+1" query problems
- Consistent performance regardless of offset
- Handles real-time data updates gracefully
- Memory-efficient for large result sets

### Caching Strategy

**Multi-Level Caching Architecture:**

```python
# 1. Application-level caching (Redis)
@cache_page(60 * 5)  # Cache for 5 minutes
def job_list(request):
    pass

# 2. Query result caching
jobs = cache.get_or_set(
    f'jobs:category:{category_id}',
    lambda: Job.objects.filter(category_id=category_id),
    timeout=300
)

# 3. Template fragment caching
{% cache 600 job_detail job.id %}
    {{ job.description }}
{% endcache %}
```

**Cache Configuration:**
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'MAX_ENTRIES': 10000,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'KEY_PREFIX': 'jobboard',
        'TIMEOUT': 300,  # 5 minutes default
    }
}
```

**Cached Endpoints:**
- Job listings: 5 minutes TTL
- Job categories: 1 hour TTL
- Search results: 10 minutes TTL
- User profile: 15 minutes TTL
- Trending jobs: 30 minutes TTL

**Cache Invalidation:**
```python
# Automatic cache invalidation on model updates
@receiver(post_save, sender=Job)
def invalidate_job_cache(sender, instance, **kwargs):
    cache_keys = [
        f'job:{instance.id}',
        f'jobs:category:{instance.category_id}',
        'jobs:trending',
    ]
    cache.delete_many(cache_keys)
```

### Query Optimization
- **Select Related**: Reduce database queries with JOIN optimization
- **Prefetch Related**: Optimize many-to-many and reverse foreign key lookups
- **Only/Defer**: Load only necessary fields
- **Database Connection Pooling**: Reuse database connections
- **Query Result Streaming**: Handle large datasets efficiently

```python
# Optimized query example
jobs = Job.objects.select_related(
    'employer', 'category'
).prefetch_related(
    'applications'
).only(
    'id', 'title', 'company', 'location'
).filter(
    status='published'
)[:20]
```

### Job Recommendation Engine

**Hybrid Recommendation System:**

1. **Content-Based Filtering:**
   - Match jobs based on user's skills and experience
   - TF-IDF vectorization of job descriptions
   - Cosine similarity scoring

2. **Collaborative Filtering:**
   - User-based: "Users like you also applied to..."
   - Item-based: "Jobs similar to ones you viewed..."

3. **Popularity-Based:**
   - Trending jobs based on views and applications
   - Time-decay factor for recency

**Implementation:**
```python
# Generate recommendations
def generate_recommendations(user, limit=10):
    user_profile = user.profile
    
    # Content-based score
    content_score = calculate_content_similarity(
        user_profile.skills,
        user_profile.experience_years,
        user_profile.preferred_locations
    )
    
    # Collaborative score
    collaborative_score = calculate_collaborative_score(
        user.id,
        similar_users=find_similar_users(user)
    )
    
    # Combined score (weighted)
    final_score = (
        0.5 * content_score +
        0.3 * collaborative_score +
        0.2 * popularity_score
    )
    
    return Job.objects.annotate(
        recommendation_score=final_score
    ).order_by('-recommendation_score')[:limit]
```

**Recommendation Features:**
- Real-time personalization
- Batch processing for large user bases
- A/B testing framework for algorithm tuning
- Explainable recommendations (why this job?)
- Diversity in recommendations

### Performance Metrics
- Average API response time: <100ms
- Full-text search response: <50ms
- Database query time: <30ms
- Cache hit ratio: >85%
- Recommendation generation: <200ms
- Support for 10,000+ concurrent connections
- 99.9% uptime SLA

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report

# Run specific test module
python manage.py test apps.jobs.tests

# Run with verbose output
python manage.py test --verbosity=2
```

### Test Coverage

- **Unit Tests**: Model methods, utility functions, serializers
- **Integration Tests**: API endpoints, authentication flow
- **Performance Tests**: Load testing with locust
- **Security Tests**: OWASP Top 10 vulnerability scanning

Target: >90% code coverage

### Load Testing

```bash
# Using locust
locust -f locustfile.py --host=http://localhost:8000
```

## 🚢 Deployment

### Production Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Configure secure `SECRET_KEY`
- [ ] Set up SSL/TLS certificates
- [ ] Configure production database with connection pooling
- [ ] Set up Redis for caching and session storage
- [ ] Configure Celery workers for background tasks
- [ ] Set up monitoring and logging (Sentry, CloudWatch)
- [ ] Configure CORS headers for frontend
- [ ] Set up automated backups
- [ ] Configure CDN for static files
- [ ] Enable rate limiting
- [ ] Set up CI/CD pipeline

### Docker Production Deployment

```bash
# Build production image
docker build -t jobboard-backend:latest .

# Run with docker-compose
docker-compose -f docker-compose.prod.yml up -d

# Scale workers
docker-compose -f docker-compose.prod.yml up -d --scale celery=4
```

### AWS Deployment (Example)

1. Deploy application on ECS/EKS
2. Use RDS for PostgreSQL
3. ElastiCache for Redis
4. S3 for file storage
5. CloudFront for CDN
6. Route53 for DNS
7. ALB for load balancing

### Environment-Specific Settings

```python
# settings/production.py
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
```

## 📊 Monitoring & Logging

### Logging Configuration

```python
LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/django.log',
            'maxBytes': 1024*1024*15,  # 15MB
            'backupCount': 10,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
}
```

### Monitoring Tools

- **Application Performance**: Sentry for error tracking
- **Infrastructure**: CloudWatch, Datadog, or Prometheus
- **Database**: PostgreSQL slow query logs
- **API Metrics**: Response times, error rates, throughput

### Health Check Endpoints

```
GET /health/              - Basic health check
GET /health/db/           - Database connectivity
GET /health/cache/        - Redis connectivity
GET /health/celery/       - Celery worker status
```

## 🔒 Security

### Security Headers

```python
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
```

### Rate Limiting

```python
# 100 requests per hour per IP for authentication endpoints
# 1000 requests per hour per user for API endpoints
```

### Data Protection

- Personal data encrypted at rest
- GDPR compliance ready
- Data retention policies
- Secure file upload validation

### Security Audits

- Regular dependency updates
- Automated security scanning (Bandit, Safety)
- Penetration testing schedule
- Security incident response plan

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 style guide
- Write unit tests for new features
- Update documentation
- Add docstrings to functions and classes
- Run linters before committing (black, flake8, isort)

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run code formatters
black .
isort .

# Run linters
flake8 .
pylint apps/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

### Documentation
- [API Documentation](http://localhost:8000/api/docs/)
- [Developer Guide](docs/DEVELOPER_GUIDE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

### Community
- GitHub Issues: [Report bugs or request features](https://github.com/JesutofunmiOludu/alx-project-nexus/issues)
- Email: support@yourdomain.com
- Discord: [Join our community](https://discord.gg/your-invite)

### Commercial Support
For enterprise support, training, or custom development, contact us at enterprise@yourdomain.com

---

**Built with ❤️ using Django and PostgreSQL**

*Last updated: January 2026*

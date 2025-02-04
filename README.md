# Facebook Insights Microservice

A robust microservice for scraping and analyzing Facebook pages, built with FastAPI, MongoDB, and Selenium. This service provides REST API endpoints for retrieving and analyzing Facebook page data, including posts, followers, and engagement metrics.
🌐 **Live Demo:** [https://facebook-insights.netlify.app](https://eloquent-cannoli-b7e5cc.netlify.app/)

## 📋 Table of Contents

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features
- Facebook page data scraping and analysis
- RESTful API endpoints
- Caching with Redis for improved performance
- Image storage using AWS S3
- Pagination and filtering capabilities
- Comprehensive error handling
- Rate limiting and request throttling
- Docker support for easy deployment

## 🛠️ Tech Stack
- **Backend Framework:** FastAPI
- **Database:** MongoDB
- **Caching:** Redis
- **Web Scraping:** Selenium
- **Storage:** AWS S3
- **Container:** Docker
- **Testing:** pytest
- **Documentation:** Swagger/OpenAPI

## 📝 Prerequisites
- Python 3.9+
- MongoDB 4.4+
- Redis 6+
- Docker & Docker Compose (optional)
- AWS Account (for S3 storage)
- Chrome/Chromium (for web scraping)

## 🚀 Installation

### Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/Shashwat-993/facebook-insights-microservice.git
cd facebook-insights-microservice
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```env
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=facebook_insights
REDIS_URL=redis://localhost:6379
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_S3_BUCKET=your_bucket_name
```

### Docker Setup

1. Build and run with Docker Compose:
```bash
docker-compose up --build
```

## ⚙️ Configuration

The application can be configured using environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| MONGODB_URL | MongoDB connection URL | mongodb://localhost:27017 |
| REDIS_URL | Redis connection URL | redis://localhost:6379 |
| AWS_ACCESS_KEY_ID | AWS access key | - |
| AWS_SECRET_ACCESS_KEY | AWS secret key | - |
| AWS_S3_BUCKET | S3 bucket name | facebook-insights |

## 📖 Usage

### Starting the Application

Local development:
```bash
uvicorn app.main:app --reload --port 8000
```

Production:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/page/{username}` | GET | Get page details |
| `/api/v1/pages` | GET | List pages with filters |
| `/api/v1/page/{username}/posts` | GET | Get page posts |
| `/api/v1/page/{username}/followers` | GET | Get page followers |

## 📚 API Documentation

API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Example Request

```python
import requests

# Get page details
response = requests.get("http://localhost:8000/api/v1/page/facebook")
data = response.json()
print(data)

# Get pages with filters
response = requests.get(
    "http://localhost:8000/api/v1/pages",
    params={
        "follower_count_min": 1000,
        "follower_count_max": 1000000,
        "category": "Technology"
    }
)
filtered_pages = response.json()
print(filtered_pages)
```

## 💻 Development

### Project Structure
```
facebook-insights-microservice/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
│   │   └── schemas.py
│   ├── services/
│   │   ├── scraper.py
│   │   ├── cache.py
│   │   └── storage.py
│   └── api/
│       └── v1/
│           └── endpoints.py
├── tests/
├── Dockerfile
└── docker-compose.yml
```

### Running Tests
```bash
pytest tests/
```

### Code Style
This project follows PEP 8 style guide. Use black for formatting:
```bash
black app/
```

## 🚢 Deployment

### Docker Deployment
```bash
# Build the image
docker build -t facebook-insights .

# Run the container
docker run -p 8000:8000 facebook-insights
```

### Production Considerations
- Use proper SSL/TLS certificates
- Implement authentication
- Set up monitoring and logging
- Configure proper database backup
- Implement rate limiting

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Shashwat-993** - *Initial work*

Last updated: 2025-02-04 16:25:06
```

This README.md provides:
1. Clear installation instructions
2. Comprehensive configuration details
3. API documentation
4. Development guidelines
5. Deployment instructions
6. Contributing guidelines

The README is designed to be:
- Easy to understand
- Well-structured
- Developer-friendly
- Comprehensive yet concise
- Properly formatted with markdown

Would you like me to add or modify any specific section?

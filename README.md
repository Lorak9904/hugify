# Hugify: Mental Health Assistance and Education Platform

## Overview

**Hugify** is a Django-based web application developed during a hackathon to provide mental health support, education, and self-care tools for individuals and organizations. The platform aims to make psychological assistance more accessible and promote mental health awareness.

### Features
- **Mood Tracking**: Log and visualize emotional states over time.
- **Mental Health Resources**: Access curated articles and links for self-help and education.
- **Personalized Recommendations**: Get suggestions based on logged moods and emotions.
- **Stress-Reduction Tools**: Interactive exercises and practical tips to manage stress.
- **Organizational Support**: Provide tools for schools, companies, and health organizations to monitor and support mental well-being.

---

## Learning Outcomes

During the development of Hugify, the following skills and experiences were gained:
1. **Django Development**: Building a robust, scalable backend.
2. **Frontend with Bootstrap**: Creating responsive and user-friendly UI components.
3. **Database Management**: Using PostgreSQL for secure and efficient data handling.
4. **RESTful API Integration**: Implementing AI services for emotion analysis.
5. **Deployment**: Hosting the project on Render with static files properly configured.
6. **Team Collaboration**: Collaborating with developers and designers in a fast-paced environment.

---

## Project Structure

mental_health/ ├── mental_api/ # App handling mood logs and AI integrations │ ├── templates/ # HTML templates │ ├── static/ # Static assets (CSS, JS, images) │ ├── urls.py # URL routing for the app │ └── views.py # Logic for serving pages and handling requests ├── mental_health/ # Main project directory │ ├── settings.py # Django settings │ ├── urls.py # Root URL configuration │ └── wsgi.py # WSGI configuration └── manage.py # Django management script




---

## How to Launch Locally

### Prerequisites
- **Python 3.10+**
- **PostgreSQL** (or SQLite for local testing)
- **pip** for managing Python packages

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/hugify.git
   cd hugify


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

```
mental_health/
├── mental_api/          # App handling mood logs and AI integrations
│   ├── templates/       # HTML templates
│   ├── static/          # Static assets (CSS, JS, images)
│   ├── urls.py          # URL routing for the app
│   └── views.py         # Logic for serving pages and handling requests
├── mental_health/       # Main project directory
│   ├── settings.py      # Django settings
│   ├── urls.py          # Root URL configuration
│   └── wsgi.py          # WSGI configuration
└── manage.py            # Django management script
```

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
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate    # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   - For **SQLite** (default):
     No additional setup is required. The app uses SQLite out of the box.
   - For **PostgreSQL**:
     - Install PostgreSQL and create a database:
       ```sql
       CREATE DATABASE hugify;
       ```
     - Update the database credentials in `mental_health/settings.py`:
       ```python
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.postgresql',
               'NAME': 'hugify',
               'USER': 'your_db_user',
               'PASSWORD': 'your_db_password',
               'HOST': 'localhost',
               'PORT': '5432',
           }
       }
       ```

5. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run the Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the App**
   Open your browser and visit `http://127.0.0.1:8000`.

---

## Deployment (Render or Other Platforms)
1. **Collect Static Files**:
   ```bash
   python manage.py collectstatic
   ```
2. **Set Environment Variables**:
   - `SECRET_KEY`: Your Django secret key.
   - `DATABASE_URL`: Your PostgreSQL connection string.

3. Push to a platform like Render, Vercel, or AWS.

---

## Acknowledgments
- **Hackathon Team**: Thanks to the collaborative effort and shared vision.
- **Django and Bootstrap Communities**: For the tools and resources that made this project possible.
- **AI Integrations**: Leveraging Vertex AI for emotion analysis.

---

## Future Development
- Adding AI-driven chatbot for mental health support.
- Enhanced data visualization for mood trends.
- Integration with wearable devices for stress monitoring.
- Expanding organizational tools for better mental health insights.

---

## Contributing
Feel free to fork the repository and submit pull requests to improve Hugify!

---

## License
Hugify is open-source and distributed under the MIT License.

# CRM Project


A full-stack Customer Relationship Management (CRM) system built with Django and Tailwind, containerized with Docker, and deployed to Render.  
Manage leads, track interactions, and view analytics—all in a responsive, secure web app. <br>

Checkout live project here: [CRM Project](https://crm-project-c15v.onrender.com)

---

## 🔍 Features

- **Lead Management**  
  - Create, view, update, and delete sales leads  
  - Assign leads to users, track status through custom pipelines  
- **User Authentication & Authorization**  
  - Sign up, log in/out, password reset  
  - Role-based access (Admin vs. Sales)  
- **Dashboard & Analytics**  
  - Real-time charts of lead counts per stage  
  - Quick search and pagination of lead lists  
- **Responsive UI**  
  - Templates styled with Tailwind CSS & Django Crispy Forms  
  - Mobile-friendly navigation and layouts  
- **Production-Ready**  
  - Static asset handling via `collectstatic` + WhiteNoise  
  - Multi-stage Dockerfile for small, secure images  
  - Automatic migrations and static build at container startup

---

## 🛠️ Tech Stack

- **Backend**: Django 4.x, Django REST Framework  
- **Frontend**: Django Templates, Tailwind CSS, Django Crispy Forms  
- **Database**: PostgreSQL (via `dj-database-url` + `psycopg[binary]`)  
- **Server**: Uvicorn ASGI  
- **Containerization**: Docker (multi-stage build)  
- **Deployment**: Render.com  
- **Security**:  
  - HTTPS enforcement, HSTS, secure cookies  
  - CSRF & XSS protection, clickjacking defense  

---

## 🚀 Quickstart (Local Docker)

1. **Clone & enter repo**  
   ```bash
   git clone https://github.com/hyeladee/crm-project.git
   cd crm-project
   ```

2. **Create .env**
    ```bash
    SECRET_KEY='your-secret-key'
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_URL=sqlite:///db.sqlite3
    ```

3. **Build & run**
    ```bash
    docker build -t crm-app .
    docker run -d -p 8000:8000 --env-file .env crm-app
    ```

4. **Visit**
    <br> Open http://localhost:8000 in your browser.<br>


## ⚙️ Environment Variables
  | Name             | Purpose                                      | Example                         |
  |------------------|----------------------------------------------|---------------------------------|
  | `SECRET_KEY`     | Django secret for crypto/signing             | a1b2c3d4…                       |
  | `DEBUG`          | Toggle debug mode (`True` or `False`)        | False                           |
  | `ALLOWED_HOSTS`  | Comma-separated hostnames                    | `crm.example.com,localhost`     |
  | `DATABASE_URL`   | Full database connection URL                 | `postgres://user:pass@host/db`  |
  | `EMAIL_HOST` etc.| (Optional) SMTP config for production emails | smtp.sendgrid.net               |


## 🔒 Security Notes
- When `DEBUG=False`, the app enforces:
    - `SECURE_SSL_REDIRECT = True`
    - HSTS (`SECURE_HSTS_SECONDS=31536000`)
    - Secure cookies (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`)
    - X-Frame-Options and XSS filters

- CSRF Trusted Origins
    <br> Add your domain to `CSRF_TRUSTED_ORIGINS` in production settings.
    <br>


## 📝 Further Improvements
- Add unit & integration tests (Django TestCase)
- Integrate Sentry for real-time error tracking
- Expose REST API endpoints and document with Swagger/OpenAPI
- Add CSV export, role-based dashboards, or Zapier integrations


## 🤝 Contributing
1. Fork and clone
2. Create a feature branch (`git checkout -b feature/xyz`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push and open a Pull Request


## 📄 License
This project is available under the MIT License.




**Next steps:**  
- Adjust any example values to your actual configuration.  
- Add a `LICENSE` file if desired.  
- Commit and push — now anyone visiting your repo sees a clear, professional overview, live demo, and how to get started.  

Let me know if you’d like any tweaks or additional sections!


<br>Built with ❤️ by hyeladee <br>
[![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-3E6DB0?style=for-the-badge&logo=render&logoColor=white)](https://crm-project-c15v.onrender.com)

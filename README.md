# Accounting Project

A Django-based accounting system that manages clients, transactions, and banking operations.

## Features

- Client management
- Transaction tracking
- Banking operations
- User authentication
- Dashboard interface

## Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd accounting
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-database-url
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Deployment on Koyeb with Neon Database

1. Set up a Neon PostgreSQL database and copy the connection string (DATABASE_URL).
2. Deploy your Django app on Koyeb:
   - Set environment variables in Koyeb:
     - `SECRET_KEY`: your Django secret key
     - `DEBUG`: False
     - `DATABASE_URL`: your Neon PostgreSQL connection string
   - Set your Koyeb app domain in `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` in `settings.py`.
3. Push your code to your repository and connect it to Koyeb for deployment.
4. Koyeb will run your app using the environment variables and Neon database.

## Environment Variables

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to 'True' for development, 'False' for production
- `DATABASE_URL`: Neon PostgreSQL database URL

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request 
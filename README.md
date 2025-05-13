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

## Environment Variables

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to 'True' for development, 'False' for production
- `DATABASE_URL`: PostgreSQL database URL

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request 
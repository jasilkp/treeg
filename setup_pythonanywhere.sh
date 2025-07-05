#!/bin/bash

# PythonAnywhere Setup Script for Django Accounting Project
# Run this script in your PythonAnywhere Bash console

echo "Setting up Django Accounting Project on PythonAnywhere..."

# Navigate to project directory
cd /home/Ableaccounting/accounting

# Create virtual environment if it doesn't exist
if [ ! -d "treeg" ]; then
    echo "Creating virtual environment..."
    python3 -m venv treeg
fi

# Activate virtual environment
echo "Activating virtual environment..."
source treeg/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cat > .env << EOF
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-neon-database-url
DEBUG=False
EOF
    echo "Please edit .env file with your actual values"
fi

# Run Django checks
echo "Running Django checks..."
python manage.py check

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Setup complete! Please configure your web app in the PythonAnywhere dashboard."
echo "Don't forget to:"
echo "1. Update your .env file with real values"
echo "2. Configure your web app in the Web tab"
echo "3. Set up your WSGI file"
echo "4. Configure static files"
echo "5. Reload your web app" 
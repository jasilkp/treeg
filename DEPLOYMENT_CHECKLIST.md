# PythonAnywhere Deployment Checklist

## ✅ Pre-Deployment (Local)
- [ ] Project is working locally
- [ ] All dependencies are in requirements.txt
- [ ] Database migrations are ready
- [ ] Static files are configured
- [ ] Environment variables are documented

## ✅ Step 1: Upload to PythonAnywhere
- [ ] Upload project files to `/home/Ableaccounting/accounting`
- [ ] OR clone from Git repository

## ✅ Step 2: Set Up Environment
- [ ] Open Bash console on PythonAnywhere
- [ ] Navigate to project directory: `cd /home/Ableaccounting/accounting`
- [ ] Create virtual environment: `python3 -m venv treeg`
- [ ] Activate virtual environment: `source treeg/bin/activate`
- [ ] Install dependencies: `pip install -r requirements.txt`

## ✅ Step 3: Configure Environment Variables
- [ ] Create `.env` file in project root
- [ ] Add SECRET_KEY
- [ ] Add DATABASE_URL (Neon database)
- [ ] Set DEBUG=False

## ✅ Step 4: Database Setup
- [ ] Run migrations: `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] Collect static files: `python manage.py collectstatic`

## ✅ Step 5: Configure Web App
- [ ] Go to Web tab on PythonAnywhere
- [ ] Add new web app with Manual configuration
- [ ] Set source code: `/home/Ableaccounting/accounting`
- [ ] Set working directory: `/home/Ableaccounting/accounting`
- [ ] Set virtual environment: `/home/Ableaccounting/accounting/treeg`

## ✅ Step 6: Configure WSGI
- [ ] Click on WSGI configuration file
- [ ] Replace content with pythonanywhere_wsgi.py content

## ✅ Step 7: Configure Static Files
- [ ] Add static files URL: `/static/`
- [ ] Add static files directory: `/home/Ableaccounting/accounting/staticfiles`
- [ ] Add media files URL: `/media/` (if needed)
- [ ] Add media files directory: `/home/Ableaccounting/accounting/media`

## ✅ Step 8: Test Deployment
- [ ] Click Reload button
- [ ] Visit your site: https://Ableaccounting.pythonanywhere.com
- [ ] Test login functionality
- [ ] Test admin panel
- [ ] Check error logs if issues

## ✅ Post-Deployment
- [ ] Set up regular backups
- [ ] Monitor error logs
- [ ] Update dependencies regularly
- [ ] Test all functionality

## 🚨 Common Issues to Check
- [ ] Virtual environment is activated
- [ ] All dependencies are installed
- [ ] Database connection is working
- [ ] Static files are collected
- [ ] Environment variables are set correctly
- [ ] WSGI file is configured properly 
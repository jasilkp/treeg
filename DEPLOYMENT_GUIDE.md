# Django Project Deployment Guide for PythonAnywhere

## Prerequisites
- PythonAnywhere account with username: `Ableaccounting`
- Neon database connection string
- Virtual environment named `treeg` with all dependencies

## Step 1: Upload Your Project to PythonAnywhere

### Option A: Using Git (Recommended)
1. Push your project to GitHub/GitLab
2. On PythonAnywhere, open a Bash console
3. Clone your repository:
```bash
cd /home/Ableaccounting
git clone <your-repository-url>
cd accounting
```

### Option B: Using File Upload
1. Zip your project locally
2. Upload via PythonAnywhere Files tab
3. Extract in `/home/Ableaccounting/accounting`

## Step 2: Set Up Virtual Environment

1. Open a Bash console on PythonAnywhere
2. Navigate to your project:
```bash
cd /home/Ableaccounting/accounting
```

3. Create and activate virtual environment:
```bash
python3 -m venv treeg
source treeg/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Step 3: Configure Environment Variables

1. Create a `.env` file in your project root:
```bash
nano .env
```

2. Add your environment variables:
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-neon-database-url
DEBUG=False
```

## Step 4: Configure Database

1. Run migrations:
```bash
python manage.py migrate
```

2. Create a superuser:
```bash
python manage.py createsuperuser
```

3. Collect static files:
```bash
python manage.py collectstatic
```

## Step 5: Configure PythonAnywhere Web App

1. Go to the **Web** tab on PythonAnywhere
2. Click **Add a new web app**
3. Choose **Manual configuration**
4. Select **Python 3.9** (or your preferred version)

### Configure WSGI File
1. Click on the WSGI configuration file link
2. Replace the content with the content from `pythonanywhere_wsgi.py`

### Configure Virtual Environment
1. In the **Code** section, set:
   - Source code: `/home/Ableaccounting/accounting`
   - Working directory: `/home/Ableaccounting/accounting`
   - WSGI configuration file: `/var/www/Ableaccounting_pythonanywhere_com_wsgi.py`

2. In the **Virtual environment** section, set:
   - `/home/Ableaccounting/accounting/treeg`

## Step 6: Configure Static Files

1. In the **Static files** section:
   - URL: `/static/`
   - Directory: `/home/Ableaccounting/accounting/staticfiles`

2. Add media files (if needed):
   - URL: `/media/`
   - Directory: `/home/Ableaccounting/accounting/media`

## Step 7: Reload Your Web App

1. Click the **Reload** button in the Web tab
2. Your site should now be available at: `https://Ableaccounting.pythonanywhere.com`

## Troubleshooting

### Common Issues:

1. **Import Errors**: Make sure your virtual environment is activated and dependencies are installed
2. **Database Connection**: Verify your Neon database URL is correct
3. **Static Files**: Ensure `collectstatic` was run successfully
4. **Permission Issues**: Check file permissions in your project directory

### Check Logs:
- Error logs are available in the **Web** tab
- Check both error logs and server logs for debugging

## Security Notes

1. Never commit your `.env` file to version control
2. Use strong SECRET_KEY in production
3. Keep DEBUG=False in production
4. Regularly update dependencies

## Maintenance

1. **Regular Updates**: Keep your dependencies updated
2. **Backup**: Regularly backup your database
3. **Monitoring**: Check error logs regularly
4. **Performance**: Monitor your app's performance

## Useful Commands

```bash
# Activate virtual environment
source treeg/bin/activate

# Run Django shell
python manage.py shell

# Check Django status
python manage.py check

# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
``` 
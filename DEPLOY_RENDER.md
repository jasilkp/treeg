# Deploying to Render.com + Neon.tech (100% Free Setup)

This guide walks you through deploying this Django Accounting project on **Render.com** (Web Service) connected to **Neon.tech** (PostgreSQL Database) with **UptimeRobot** for 24/7 zero-cold-start performance.

---

## 📋 Overview of the Setup

- **Web Service**: Render Free Tier (Python 3.12, Gunicorn, WhiteNoise)
- **Database**: Neon.tech Free Tier (Serverless PostgreSQL, 0.5 GB, does not expire)
- **Availability / Keep-Alive**: UptimeRobot (10-minute HTTP ping to `/health/` prevents sleep mode)
- **Total Cost**: **$0.00 / month forever**

---

## Step 1: Create Your Free PostgreSQL Database on Neon.tech

1. Go to **[https://neon.tech](https://neon.tech)** and sign up / log in.
2. Click **Create Project**.
   - **Project Name**: `accounting-db`
   - **Postgres Version**: `16` (or latest)
   - **Region**: Pick the region closest to you or Render (e.g. Singapore, Frankfurt, US East).
3. Once created, in the **Dashboard / Connection Details**, copy the **Connection string** (`Pooled` or `Direct`).
   It will look like:
   ```text
   postgresql://username:password@ep-xyz-pooler.region.aws.neon.tech/neondb?sslmode=require
   ```
4. Save this connection string — this is your `DATABASE_URL`.

---

## Step 2: Push Your Code to GitHub

Ensure all files (including `build.sh`, `render.yaml`, `accounting/settings.py`) are pushed to your GitHub repository:

```bash
git add .
git commit -m "Configure Render.com and Neon deployment"
git push origin main
```

---

## Step 3: Deploy on Render.com

### Option A: Using Render Blueprints (Automatic via `render.yaml`)
1. Go to **[https://render.com](https://render.com)** and log in.
2. Click **New +** → **Blueprint**.
3. Connect your GitHub repository.
4. Render will detect `render.yaml`.
5. Under `DATABASE_URL`, paste your Neon connection string from Step 1.
6. Click **Apply**.

### Option B: Manual Web Service Creation
1. Go to **[Render Dashboard](https://dashboard.render.com)**.
2. Click **New +** → **Web Service** → Connect your GitHub repo.
3. Configure the following:
   - **Name**: `accounting-app`
   - **Region**: Choose closest to your Neon database region.
   - **Branch**: `main` (or `master`)
   - **Runtime**: `Python 3`
   - **Build Command**: `bash build.sh`
   - **Start Command**: `gunicorn accounting.wsgi:application --bind 0.0.0.0:$PORT --log-file -`
   - **Instance Type**: `Free`
4. Under **Environment Variables**, add:
   | Key | Value |
   | :--- | :--- |
   | `DATABASE_URL` | *(Your Neon connection string)* |
   | `SECRET_KEY` | *(A random secure string of 50+ chars)* |
   | `DEBUG` | `False` |
   | `ALLOWED_HOSTS` | `.onrender.com` |
   | `CSRF_TRUSTED_ORIGINS` | `https://*.onrender.com` |
   | `PYTHON_VERSION` | `3.12.9` |
5. Click **Create Web Service**.

---

## Step 4: Create Admin / Superuser Account

Once the deployment finishes and shows `Live`:

1. In Render Dashboard, click your service → navigate to **Shell** (left sidebar).
2. Run:
   ```bash
   python manage.py createsuperuser
   ```
3. Enter your desired username, email, and password.
4. Visit `https://<your-service-name>.onrender.com` and log in!

---

## Step 5: Prevent Cold Starts with UptimeRobot (24/7 Awake)

Because Render's free tier sleeps after 15 minutes of inactivity:

1. Go to **[https://uptimerobot.com](https://uptimerobot.com)** and register for free.
2. Click **Add New Monitor**:
   - **Monitor Type**: `HTTP(s)`
   - **Friendly Name**: `Accounting Render KeepAlive`
   - **URL (or IP)**: `https://<your-service-name>.onrender.com/health/`
   - **Monitoring Interval**: `Every 10 minutes`
3. Click **Create Monitor**.

Now your app will be pinged every 10 minutes, keeping the Render container active 24/7 with zero startup delay!

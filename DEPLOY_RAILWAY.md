# Deploying to Railway (quick guide)

This project is prepared for deployment on Railway. Below are the recommended, minimal steps to deploy the app and configure the environment.

**Prerequisites**
- Push this repository to GitHub (or other Git provider) and connect it to Railway, or use the Railway CLI.
- Ensure `.env` is not committed (it's in `.gitignore`).

**Files in the repo that help deployment**
- [Procfile](Procfile) — starts the web process: `gunicorn accounting.wsgi --log-file -`
- [requirements.txt](requirements.txt) — lists dependencies (Django, gunicorn, whitenoise, dj-database-url, psycopg[binary], ...)
- [runtime.txt](runtime.txt) — Python runtime used by Railway
- [accounting/settings.py](accounting/settings.py) — contains helpers that automatically add Railway hosts and support `DATABASE_URL`.
- `STATICFILES_STORAGE` and `WhiteNoise` middleware are already configured.

**High-level steps (Web UI)**
1. Create a new project in Railway and connect your GitHub repo (or push code and use `railway up`).
2. Add the Postgres plugin from Railway (Project → Plugins → Postgres). Railway will provision a database and set the `DATABASE_URL` environment variable automatically.
3. In Railway project Settings → Variables, add these environment variables:
   - `SECRET_KEY`: set to a securely generated secret (NOT your local `.env` value). Example generator:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

   - `DEBUG`: `False` (string). Do NOT leave `DEBUG=True` in production.
   - (optional) `ALLOWED_HOSTS`: a comma-separated list of hosts to allow (e.g. `your-app.up.railway.app`). The application will also try to pick up `RAILWAY_PUBLIC_DOMAIN` or `RAILWAY_PUBLIC_URL` automatically.

4. Configure the Build Command (Railway settings) to run migrations and collect static files. Example Build Command (single-line):

```bash
python -m pip install --upgrade pip && pip install -r requirements.txt && python manage.py migrate --noinput && python manage.py collectstatic --noinput
```

Or set the Build Command to run the helper script:

```bash
bash scripts/railway_build.sh
```

5. Ensure the Start Command is derived from `Procfile` (Railway reads `Procfile`) or set it explicitly to:

```bash
gunicorn accounting.wsgi --log-file -
```

6. Deploy. Railway will build, run migrations and collect static (if you configured the Build Command). Once deployed, Railway assigns a public domain like `https://<project>.up.railway.app`.

7. After deployment, if your site is not accessible, set `ALLOWED_HOSTS` or `RAILWAY_PUBLIC_URL` in Railway environment variables to the assigned domain.

**Running management commands on Railway**
- Use Railway CLI: `railway run python manage.py createsuperuser` or `railway run python manage.py migrate`.
- Or use Railway web UI → New Command (Project) to run commands.

**Optional: Railway CLI (local deploy)**
- Install: `npm install -g railway` or see Railway docs.
- From project root:

```bash
railway login
railway init   # link or create a project
railway up     # deploy current directory (you can configure environment variables afterward)
```

**Security notes**
- Never commit `SECRET_KEY` or `.env` to GitHub.
- Use a strong `SECRET_KEY` and set `DEBUG=False` for production.

**Troubleshooting**
- If `collectstatic` fails due to missing files referenced by static manifests, fix or remove the references or ensure the static assets exist.
- Use the Railway logs (Project → Deployments → Logs) to inspect errors during build or run.

---

If you want, I can:
- Add a `railway_build.sh` helper script (recommended) — I can create that now.
- Walk through connecting this repo to Railway and the exact env vars you should set.
- Create a GitHub Actions workflow for automatic deploys.

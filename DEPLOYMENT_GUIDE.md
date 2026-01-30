# DevLanka Hub - Render.com Deployment Guide
# ==========================================

## Prerequisites ✅
- [x] Render.com account created
- [x] PostgreSQL database created on Render
- [x] Data migrated to Render database
- [x] GitHub repository ready

---

## Step 1: Prepare Your Code for Deployment

### 1.1 Create requirements.txt
Make sure you have all Python dependencies listed:

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
python-dotenv==1.0.0
pydantic==2.5.0
pydantic-settings==2.1.0
email-validator==2.1.0
```

### 1.2 Verify main.py
Your FastAPI app should be in: `app/main.py`

---

## Step 2: Create Web Service on Render

### 2.1 Go to Render Dashboard
1. Click **"New +"** button
2. Select **"Web Service"**

### 2.2 Connect GitHub Repository
1. Click **"Connect a repository"**
2. Select your **DevLanka** repository
3. Click **"Connect"**

### 2.3 Configure Web Service

**Name:** `devlanka-hub`

**Region:** `Oregon` (same as your database)

**Branch:** `main` (or your default branch)

**Root Directory:** Leave empty (unless your code is in a subdirectory)

**Environment:** `Python 3`

**Build Command:** Leave empty (or use `pip install -r requirements.txt`)

**Start Command:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

**Instance Type:** `Free`

---

## Step 3: Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

Add these 7 variables:

### Variable 1: DATABASE_URL
```
postgresql://devlanka_user:41xICrnnLOmliOcksmgqgp5pTZZMfNFK@dpg-d5uatqq4d50c738ufim0-a.oregon-postgres.render.com/devlanka
```

### Variable 2: SECRET_KEY
```
R1vzSzIHGNduxIQNH99jKmwGaeniTZUtp_vQgYLnHsc
```

### Variable 3: MAIL_USERNAME
```
randidudamsith96@gmail.com
```

### Variable 4: MAIL_PASSWORD
```
qntauxpfqznijnpu
```

### Variable 5: MAIL_FROM
```
randidudamsith96@gmail.com
```

### Variable 6: MAIL_PORT
```
587
```

### Variable 7: MAIL_SERVER
```
smtp.gmail.com
```

---

## Step 4: Deploy!

1. Click **"Create Web Service"**
2. Wait for deployment (5-10 minutes)
3. Watch the logs for any errors

---

## Step 5: Verify Deployment

### 5.1 Check Service URL
Your service will be available at:
```
https://devlanka-hub.onrender.com
```

### 5.2 Test API Endpoints
```bash
# Health check
curl https://devlanka-hub.onrender.com/

# API docs
https://devlanka-hub.onrender.com/docs
```

### 5.3 Update Frontend API URLs
In your HTML files, update API_BASE:
```javascript
const API_BASE = 'https://devlanka-hub.onrender.com/api';
```

---

## Step 6: Deploy Frontend (Static Site)

### Option A: Same Web Service (Serve HTML from FastAPI)
Already done if your templates are in `app/templates/`

### Option B: Separate Static Site on Render
1. New → Static Site
2. Connect same repository
3. Publish Directory: `app/templates`
4. Build Command: (leave empty)

---

## Troubleshooting 🔧

### Issue: Service won't start
- Check logs for errors
- Verify DATABASE_URL is correct
- Ensure all dependencies in requirements.txt

### Issue: Database connection failed
- Verify DATABASE_URL includes `.oregon-postgres.render.com`
- Check database is in same region as web service

### Issue: 502 Bad Gateway
- Service is sleeping (free tier)
- Wait 30-60 seconds for cold start

---

## Important Notes ⚠️

### Free Tier Limitations:
- ✅ Service sleeps after 15 minutes inactivity
- ✅ 750 hours/month limit
- ✅ Cold start: 30-60 seconds
- ✅ Database: 1GB storage, 90 days retention

### Keep Service Alive:
Use a cron job or uptime monitor:
- UptimeRobot (free)
- Cron-job.org (free)
- Ping every 14 minutes

---

## Your Deployment URLs 🌐

**Backend API:**
```
https://devlanka-hub.onrender.com
```

**API Documentation:**
```
https://devlanka-hub.onrender.com/docs
```

**Frontend:**
```
https://devlanka-hub.onrender.com/index.html
```

---

## Next Steps 🚀

1. ✅ Deploy web service
2. ✅ Test all API endpoints
3. ✅ Update frontend API URLs
4. ✅ Test user registration/login
5. ✅ Add custom domain (optional)
6. ✅ Set up uptime monitoring

---

## Support 💬

If you encounter issues:
1. Check Render logs
2. Verify environment variables
3. Test database connection
4. Check FastAPI startup logs

Good luck with your deployment! 🎉

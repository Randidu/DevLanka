# 🚀 DevLanka - Render Free Hosting Guide

මෙන්න DevLanka project එක Render.com හි **Free Tier** එකේ deploy කරන step-by-step guide එක.

## 📋 අවශ්‍ය දේවල් (Prerequisites)
1. GitHub Account එකක්.
2. Render.com Account එකක්.
3. ඔබේ Project code එක GitHub repository එකකට push කර තිබීම.

---

## Step 1: GitHub Repository සකස් කිරීම

ඔබේ project එකේ `Procfile` එකක් සහ `requirements.txt` එකක් තිබීම අනිවාර්යයි (අපි ඒවා දැනටමත් හදලා තියෙන්නේ).

1. සියලුම changes commit කර push කරන්න:
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

---

## Step 2: Render හි Web Service එකක් සාදා ගැනීම

1. [Render Dashboard](https://dashboard.render.com/) එකට යන්න.
2. උඩ තියෙන **"New +"** button එක click කර **"Web Service"** තෝරන්න.
3. **"Build and deploy from a Git repository"** තෝරන්න.
4. ඔබේ GitHub repository එක connect කරන්න (list එකෙන් select කරන්න).

### ⚙️ Settings සැකසීම:

*   **Name:** `devlanka-hub` (හෝ ඔබට කැමති නමක්)
*   **Region:** `Singapore` (ලංකාවට ළඟම server එක)
*   **Branch:** `main`
*   **Root Directory:** (හිස්ව තබන්න - Leave blank)
*   **Runtime:** `Python 3`
*   **Build Command:** `pip install -r requirements.txt`
*   **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
*   **Instance Type:** **Free** (Free tier එක select කරන්න)

---

## Step 3: Database (PostgreSQL) සාදා ගැනීම (Optional but Recommended)

DevLanka project එක database එකක් use කරන නිසා Render හි free PostgreSQL database එකක් සාදාගත යුතුය.

1. Dashboard එකේ **"New +"** -> **"PostgreSQL"** තෝරන්න.
2. **Name:** `devlanka-db`
3. **Database:** `devlanka`
4. **User:** `devlanka_user`
5. **Region:** Web Service එක දාපු region එකම තෝරන්න (Singapore).
6. **Instance Type:** **Free**
7. **Create Database** click කරන්න.

### 🔗 Database එක Web Service එකට Connect කිරීම:

Database එක හැදුනු පසු, එහි **Internal Database URL** එක copy කරගන්න.

1. ඔබේ **Web Service** එකේ Dashboard එකට යන්න.
2. **Environment** tab එකට යන්න.
3. **Add Environment Variable** click කරන්න:
   *   **Key:** `DATABASE_URL`
   *   **Value:** (කලින් copy කරගත් Internal Database URL එක paste කරන්න)
   *   Note: URL එකේ `postgres://` තිබේ නම් එය `postgresql://` ලෙස වෙනස් කිරීම වඩා හොඳයි (Python library compatibility සඳහා).

---

## Step 4: Environment Variables (ENV)

ඔබේ Web Service එකේ **Environment** tab එකේ පහත variables add කරන්න:

| Key | Value | Note |
|-----|-------|------|
| `PYTHON_VERSION` | `3.9.0` | නිර්දේශිතයි |
| `SECRET_KEY` | (Your Secret Key) | Security සඳහා |
| `ALGORITHM` | `HS256` | JWT Algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` | Token time |

Save Changes click කරන්න.

---

## Step 5: Deploy කිරීම 🚀

*   Environment variables save කළ පසු Render ස්වයංක්‍රීයව deploy වීම අරඹයි.
*   **Logs** tab එකේ ඔබට process එක බලාගත හැක.
*   Deploy වී අවසානයේ "Live" ලෙස කොළ පැහැයෙන් දිස්වේ.
*   ඔබේ URL එක (උදා: `https://devlanka-hub.onrender.com`) වෙත ගොස් check කරන්න.

---

## ⚠️ Free Tier Limitations (වැදගත්)

Render Free Tier එකේ Web Services:
1.  **Sleep Mode:** විනාඩි 15ක් කිසිම traffic එකක් නැති වුනොත් service එක sleep වෙනවා. ඊළඟට කෙනෙක් log වෙද්දී මුලින්ම load වෙන්න තත්පර 30-50ක් විතර යන්න පුළුවන් (Cold Start).
2.  **Usage Limits:** මාසෙකට යම් පැය ගණනක් සහ bandwidth සීමාවක් තිබේ (නමුත් demo project එකකට හොඳටම ප්‍රමාණවත්).

---

### 🎉 සුභ පැතුම්! ඔබේ Site එක දැන් Live! 🌍
Launch කළාට පසු, Admin panel එකට ගොස් database එකට data (categories, etc.) add කරගන්න.

# Deployment Guide for Omkara Parashakti Website

## Step 1: Create a GitHub Repository
1. Log in to your [GitHub account](https://github.com).
2. Click the **+** icon in the top-right corner and select **New repository**.
3. Name the repository (e.g., `omkara-parashakti`).
4. **Select Public** (Required for free GitHub Pages).
   *   *Note: If you have a GitHub Pro (Paid) account, you can select **Private**.*
5. Do **not** check "Add a README", ".gitignore", or "license" (we already have files).
6. Click **Create repository**.

## Step 2: Push the Code
Once the repository is created, you will see a URL ending in `.git` (e.g., `https://github.com/YOUR_USERNAME/omkara-parashakti.git`).

**Provide this URL to me**, and I will run the necessary commands to upload your code.

## Step 3: Enable GitHub Pages
1. Go to your repository on GitHub.
2. Click on **Settings** (top tab).
3. Scroll down to the **Pages** section (on the left sidebar).
4. Under **Source**, select `Deploy from a branch`.
5. Under **Branch**, select `master` (or `main`) and `/ (root)`.
6. Click **Save**.

## Step 4: Visits Your Site!
GitHub will generate a link (usually `https://YOUR_USERNAME.github.io/omkara-parashakti/`).

## Step 5: Configure GoDaddy DNS (Crucial)

To make `omkaraparashakti.com` show your site, you need to add **4 "A" records** and **1 "CNAME" record** in GoDaddy.

1.  Log in to [GoDaddy](https://dcc.godaddy.com/domains).
2.  Select your domain **omkaraparashakti.com**.
3.  Scroll down to **DNS Records** (or select "Manage DNS").
4.  **Add/Edit these specific records:**

    ### A Records (Points your domain to GitHub)
    | Type | Name | Value | TTL |
    | :--- | :--- | :--- | :--- |
    | A | @ | 185.199.108.153 | 600 Seconds (or default) |
    | A | @ | 185.199.109.153 | 600 Seconds (or default) |
    | A | @ | 185.199.110.153 | 600 Seconds (or default) |
    | A | @ | 185.199.111.153 | 600 Seconds (or default) |

    ### CNAME Record (Points www to your domain)
    | Type | Name | Value | TTL |
    | :--- | :--- | :--- | :--- |
    | CNAME | www | omkaraparashakti.com | 1 Hour (or default) |

    *(Delete any other existing "A" records with Name "@" or "Parked" to avoid conflicts)*.

## Step 6: Verify in GitHub
1.  Go to your repository **Settings** > **Pages**.
2.  Under **Custom domain**, ensure `omkaraparashakti.com` is listed.
3.  Wait for the "DNS Check" to pass (can take 15 mins to 24 hours).
4.  Check **Enforce HTTPS**.

Your site will be live at [https://omkaraparashakti.com](https://omkaraparashakti.com).

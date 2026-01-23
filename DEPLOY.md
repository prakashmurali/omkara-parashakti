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

## Step 5: Using a Custom Domain (Optional)
**Yes! You can completely hide the `github.io` name.**

1.  **Buy your domain** (e.g., from GoDaddy, Namecheap, etc.).
2.  **Configure DNS**:
    *   Log in to your domain provider.
    *   Find "DNS Management".
    *   Add a **CNAME** record:
        *   Host: `www`
        *   Value: `YOUR_USERNAME.github.io`
3.  **Configure GitHub**:
    *   Go to Repository **Settings** > **Pages**.
    *   Under **Custom domain**, type your domain (e.g., `www.yourtemple.com`).
    *   Click **Save**.
    *   Check the box **Enforce HTTPS** (this gives you the secure lock icon 🔒).

Now, when users visit `www.yourtemple.com`, they will see your site, and "GitHub" will not appear anywhere in the address bar.

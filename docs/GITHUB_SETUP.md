# Uploading Image Editor Pro to GitHub

Follow these steps to put your project on GitHub.

## 1. Create a GitHub account (if needed)

- Go to [github.com](https://github.com) and sign up or log in.

## 2. Create a new repository on GitHub

1. Click **"New"** (or the **+** in the top right → **New repository**).
2. Choose a **Repository name** (e.g. `image-editor-pro` or `photoshop-clone`).
3. Add a **Description** (optional), e.g. "PyQt6 image editor with layers and filters".
4. Choose **Public**.
5. **Do not** check "Add a README", "Add .gitignore", or "Choose a license" (you already have these).
6. Click **Create repository**.

## 3. Initialize Git and push from your machine

Open a terminal in the project folder (`Version_1`) and run:

```powershell
# Initialize Git (only needed once)
git init

# Stage all files
git add .

# First commit
git commit -m "Initial commit: Image Editor Pro - Photoshop clone start"

# Rename branch to main (if your default is master)
git branch -M main

# Add your GitHub repo as remote (replace YOUR_USERNAME and YOUR_REPO with your values)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git push -u origin main
```

**Example** if your GitHub username is `jane` and the repo is `image-editor-pro`:

```powershell
git remote add origin https://github.com/jane/image-editor-pro.git
git push -u origin main
```

## 4. If GitHub asks you to authenticate

- **HTTPS:** When you run `git push`, GitHub may ask for your username and a **Personal Access Token** (not your password). Create one at: GitHub → Settings → Developer settings → Personal access tokens.
- **SSH:** If you use SSH keys, use the SSH URL instead:  
  `git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO.git`

## 5. Optional: Update README clone URL

After the repo exists, edit `README.md` and replace:

```text
git clone https://github.com/yourusername/image-editor-pro.git
```

with your real URL, e.g.:

```text
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

---

After this, your Photoshop clone start is on GitHub and you can share the repo link or continue development from there.

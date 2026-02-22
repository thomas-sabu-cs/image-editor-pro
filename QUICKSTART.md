# Quick Start Guide

Get started with Image Editor Pro in 5 minutes!

## Easiest way to run (Windows)

**Double-click `run.bat`** in File Explorer, or in a terminal run:

- **Command Prompt:** `run.bat`
- **PowerShell:** `.\run.bat` (the `.\` is required in PowerShell)

This uses the virtual environment automatically and installs dependencies if needed, so you don't get "module not found" errors. If `.venv` doesn't exist yet, the script will create it and install dependencies, then start the app.

---

## Installation (if you prefer the manual steps)

### Step 1: Open a terminal in the project folder

- **Windows:** Open PowerShell or Command Prompt, then run:
  ```powershell
  cd "C:\Users\YourUsername\AI-Build-Week\02-Photoshop-Clone\Version_1"
  ```
  (Replace with your actual path to the `Version_1` folder.)

### Step 2: Create a virtual environment (recommended)

This keeps the app’s dependencies separate from the rest of your system:

```powershell
# Create the environment (use .venv or venv)
python -m venv .venv

# Activate it (required so "python" and "pip" use this environment)
.\.venv\Scripts\Activate.ps1
```

If you get an error about running scripts, run this once (as Administrator if needed):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Command Prompt (cmd) instead of PowerShell:**
```cmd
.venv\Scripts\activate.bat
```

### Step 3: Install dependencies (PyQt6, Pillow, NumPy)

With the virtual environment **activated** (you should see `(.venv)` in the prompt):

```powershell
pip install -r requirements.txt
```

This installs PyQt6 and the other packages the app needs.

### Step 4: Run the application

```powershell
python main.py
```

---

**If "PyQt6" or other modules are not recognized:**  
Make sure you activated the virtual environment (Step 2) in the **same** terminal where you run `pip install` and `python main.py`. If you open a new terminal, run the activate command again before running the app.

## First Steps

### 1. Open an Image
- Click `File > Open Image` (or press `Ctrl+O`)
- Select an image file from your computer
- The image will load in the canvas

### 2. Add a New Layer
- Click the `+` button in the Layers panel
- Or press `Ctrl+Shift+N`
- Name your layer (e.g., "Drawing")

### 3. Draw Something
- Select the **Brush** tool in the Tools panel
- Choose a color by clicking "Choose Color"
- Adjust the brush size (try 20px)
- Click and drag on the canvas to draw

### 4. Apply a Filter
- Select a layer in the Layers panel
- Go to `Filter > Blur` (or any other filter)
- Adjust the settings in the dialog
- Click OK to apply

### 5. Save Your Work
- **Save as Image**: `File > Save Image` (Ctrl+S) - exports final PNG/JPG
- **Save as Project**: `File > Save Project` (Ctrl+Shift+S) - saves as .iep with all layers

## Essential Shortcuts

- `Ctrl+Z` - Undo
- `Ctrl+Y` - Redo
- `Ctrl+J` - Duplicate layer
- `Ctrl++` - Zoom in
- `Ctrl+-` - Zoom out

## Need More Help?

- **Full User Guide**: See `docs/USER_GUIDE.md`
- **Architecture Details**: See `docs/ARCHITECTURE.md`
- **Contributing**: See `CONTRIBUTING.md`

## Testing

Run basic tests to verify everything works:

```bash
python test_basic.py
```

You should see:
```
All tests passed! ✓
```

## Troubleshooting

### "Module not found" error
Run: `pip install -r requirements.txt`

### Application won't start
- Check Python version: `python --version` (should be 3.8+)
- Run from terminal to see error messages

### Performance issues
- Try smaller canvas sizes
- Reduce number of layers
- Close other applications

---

**Enjoy creating with Image Editor Pro!** 🎨

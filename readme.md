# How to Download the Data

This project uses the **HyperspectralVectors** dataset hosted on Hugging Face.

## Quick Start

### Option 1: Automatic Download (Recommended)

Choose the script for your operating system:

#### 🐧 Linux / WSL

```bash
chmod +x download_data.sh
./download_data.sh
```

#### 🪟 Windows

Double-click or run in Command Prompt:

```bash
download_data.bat
```

Or use PowerShell:

```powershell
.\download_data.bat
```

#### 🍎 macOS

```bash
chmod +x download_data.sh
./download_data.sh
```

#### 🔄 Cross-Platform (All OS)

Use the Python script (requires Python 3.6+):

```bash
python download_data.py
```

Or:

```bash
python3 download_data.py
```

### Option 2: Manual Download

If you prefer to download files manually, you can get them from:

**Hugging Face Repository:** https://huggingface.co/datasets/alfiwillianz/HyperspectralVectors

Download these files and place them in the `data/` folder:

- `df_field_b.csv`
- `df_field_g.csv`
- `df_screenh_b.csv`
- `df_screenh_g.csv`

## Directory Structure

After downloading, your project structure should look like:

```
HSI/
├── data/
│   ├── df_field_b.csv
│   ├── df_field_g.csv
│   ├── df_screenh_b.csv
│   └── df_screenh_g.csv
├── LTSM/
├── BiLTSM/
├── VAE/
├── VAE-Lite/
├── CNN/
└── ...
```

## Dataset Information

The dataset contains hyperspectral data with four CSV files:

| File | Description |
|------|-------------|
| `df_field_b.csv` | Field data with blue channel |
| `df_field_g.csv` | Field data with green channel |
| `df_screenh_b.csv` | Screen/greenhouse data with blue channel |
| `df_screenh_g.csv` | Screen/greenhouse data with green channel |

Each file contains:
- **Spectral bands**: Hyperspectral features (numeric columns)
- **y**: Class labels
- **plant**: Plant group/sample identifier

## Verification

After downloading, verify the files exist:

**Linux/macOS:**
```bash
ls -lh data/
```

**Windows (PowerShell):**
```powershell
Get-ChildItem data/
```

**Windows (Command Prompt):**
```cmd
dir data\
```

You should see all 4 CSV files listed with their file sizes.

## Troubleshooting

### Linux/macOS

**Permission denied when running script**
```bash
chmod +x download_data.sh
./download_data.sh
```

**curl not found**
- Install curl: `sudo apt-get install curl` (Ubuntu/Debian) or `brew install curl` (macOS)
- Use Python alternative: `python download_data.py`

### Windows

**Script fails to run**
- Try using PowerShell instead of Command Prompt
- Ensure PowerShell execution policy allows scripts:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

**"Python not found" error**
- Download and install Python from https://www.python.org/downloads/
- Ensure "Add Python to PATH" is checked during installation

**Download script timeout**
- Use Python script instead: `python download_data.py`
- Manually download from Hugging Face

### All Platforms

**Connection issues**
- Check your internet connection
- Try the Hugging Face repository directly: https://huggingface.co/datasets/alfiwillianz/HyperspectralVectors
- Use VPN if access is restricted

**Disk space**
- Ensure you have at least 500 MB of free disk space
- Check available space with `df -h` (Linux/macOS) or `dir` (Windows)

## Using the Data in Notebooks

All notebooks in the subdirectories (LTSM, BiLTSM, VAE, VAE-Lite, CNN) are configured to load data from `../data/`:

```python
data_dir = "../data/"
file_path = f"../data/{filename}"
```

Once the data is downloaded to the root `data/` folder, all notebooks will automatically access it correctly.

## Summary

| Method | Windows | macOS | Linux | Pros | Cons |
|--------|---------|-------|-------|------|------|
| **Batch (.bat)** | ✅ | ❌ | ❌ | Fast, native | Windows only |
| **Shell (.sh)** | ❌ | ✅ | ✅ | Fast, native | Unix only |
| **Python (.py)** | ✅ | ✅ | ✅ | Universal | Requires Python |
| **Manual** | ✅ | ✅ | ✅ | Reliable | Manual effort |

**Recommended:** Use the platform-specific script (.bat for Windows, .sh for Mac/Linux) or Python for maximum compatibility.

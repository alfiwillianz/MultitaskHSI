@echo off
REM ==============================================
REM Download HyperspectralVectors dataset from HF
REM Windows Batch Script
REM ==============================================

setlocal enabledelayedexpansion

set "DATA_DIR=data"
set "REPO_URL=https://huggingface.co/datasets/alfiwillianz/HyperspectralVectors/resolve/main"

REM Create directory if not exists
if not exist "%DATA_DIR%" mkdir "%DATA_DIR%"
cd "%DATA_DIR%"

echo 📡 Downloading HyperspectralVectors dataset from Hugging Face...

REM Download CSV files
for %%f in (
  "df_field_b.csv"
  "df_field_g.csv"
  "df_screenh_b.csv"
  "df_screenh_g.csv"
) do (
  echo ⬇️  Downloading %%~f ...
  powershell -Command "Invoke-WebRequest -Uri '!REPO_URL!/%%~f' -OutFile '%%~f'"
  if errorlevel 1 (
    echo ❌ Failed to download %%~f
    cd ..
    exit /b 1
  )
)

echo ✅ All files downloaded to: %cd%
cd ..
pause

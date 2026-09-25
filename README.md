# War Dogs Artillery Calculator

A simple artillery distance calculator for War Dogs, built with Python and PySide6.
Enter your position and the enemy position, and it computes the distance between them.

## Download

Prebuilt Windows binaries are available on the
[Releases page](../../releases) — download `WarDogsCalculator.exe`, no
Python installation required.

## Run from source

Requires Python 3.10+.

```bash
python -m venv env
env\Scripts\activate            # Windows (use source env/bin/activate on Linux/macOS)
pip install -r requirements.txt
python main.py
```

## Build the exe

```bash
pip install pyinstaller
python -m PyInstaller WarDogsCalculator.spec
```

The finished executable will be in `dist/`.

## Project layout

| Path | Purpose |
|---|---|
| `main.py` | GUI (PySide6) |
| `calculator.py` | Distance calculation logic |
| `assets/` | Icons used by the app and the exe |
| `WarDogsCalculator.spec` | PyInstaller build configuration |
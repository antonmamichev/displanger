rem https://pyinstaller.org/en/stable/usage.html

cd c:/repository/displanger/
python -m PyInstaller --onefile --noconsole --name displanger --add-data "src/assets/flags;assets/flags" src/main.py
.\.venv\Scripts\activate
pip install --upgrade pip
pip install -r requeriments.txt
reflex init
reflex export --frontend-only
rm -rf public
rar x frontend.zip public\
rm -f frontend.zip
deactivate

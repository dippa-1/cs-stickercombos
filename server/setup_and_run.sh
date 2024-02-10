# Set up
python -m venv .venv
. .venv/bin/activate
pip install .
pip install gunicorn

# Serve
gunicorn -w 4 'server:app'

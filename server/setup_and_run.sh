cd /home/dominik/prod/cs-stickercombos/server
# Set up
python -m venv .venv
. .venv/bin/activate
pip install .
pip install gunicorn

# Serve
gunicorn -b 0.0.0.0:8000 -w 4 'server:app'


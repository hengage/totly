
set -o errexit  # exit on error

pip install -r requirements.txt
pip install gunicorn

python manage.py collectstatic --no-input
python manage.py migrate
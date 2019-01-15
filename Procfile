release: python manage.py migrate --no-input
web: newrelic-admin run-program gunicorn personal_blog.wsgi --log-file -

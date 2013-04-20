web: python pytraining/manage.py collectstatic --noinput; newrelic-admin run-program gunicorn_django pytraining.settings.production -b 0.0.0.0:$PORT

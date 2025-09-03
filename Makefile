mig:
	uv run python manage.py makemigrations
	uv run python manage.py migrate
sup:
	uv run python manage.py createsuperuser




model change:
Delete migration record in django_migration where app=<name> (optional)
python manage.py makemigrations chinese
python manage.py sqlmigrate chinese <migration-name> (optional)
python manage.py migrate chinese
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose run web python manage.py startapp products
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py shell
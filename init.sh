#To config NGINX
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart

#To config Gunicorn
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/gunicorn_django.conf /etc/gunicorn.d/test_django
sudo service gunicorn restart

#To config MySQL
sudo service mysql restart
sudo mysql -u root -e "CREATE DATABASE django_app"
sudo mysql -u root -e "CREATE USER 'django_root' IDENTIFIED BY 'root'"
sudo mysql -u root -e "GRANT ALL ON django_app.* TO 'django_root'"
sudo ln -s /home/box/web/etc/mysql.conf /etc/mysql/my.cnf

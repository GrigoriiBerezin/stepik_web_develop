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

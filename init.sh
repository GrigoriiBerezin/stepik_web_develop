#To config NGINX
sudo ln -s /home/grishamagic/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#To config Gunicorn
sudo mkdir /etc/gunicorn.d
sudo ln -s /home/grishamagic/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo gunicorn -c /etc/gunicorn.d/test /home/grishamagic/web/hello:application_func &

#To config MySQL
sudo /etc/init.d/mysql start 

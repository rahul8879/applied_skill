[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/project/applied_skill
ExecStart=/home/ubuntu/project/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          applied_skill.wsgi:application

[Install]
WantedBy=multi-user.target


server {
    listen 80;
    server_name 16.16.74.174 ;

    location = /favicon.ico { access_log off; log_not_found off; }
    

    location / {
        include    proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
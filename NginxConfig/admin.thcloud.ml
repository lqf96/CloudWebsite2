# Cloud Website Admin Configuration
server {
    # Port 80 (HTTP) & 443 (HTTPS)
    listen [::]:80;
    listen [::]:443 ssl;
    # Server name
    server_name admin.thcloud.ml;
    
    # SSL certificate & key
    ssl_certificate /home/lqf/server/certs/admin.thcloud.ml.crt;
    ssl_certificate_key /home/lqf/server/certs/admin.thcloud.ml.key;
    # Diffie-Hellman params
    ssl_dhparam /home/lqf/server/certs/dhparams.pem;
    
    # SSL cipher settings
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA:ECDHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA:ECDHE-RSA-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES256-GCM-SHA384:AES128-GCM-SHA256:AES256-SHA256:AES128-SHA256:AES256-SHA:AES128-SHA:DES-CBC3-SHA:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!MD5:!PSK:!RC4";
    ssl_prefer_server_ciphers on;
    
    # SSL session resumption settings
    ssl_session_cache shared:SSL:15m;
    ssl_session_timeout 15m;
    
    # Force HTTPS
    if ($scheme = 'http')
    {
        rewrite ^(.*) https://$host$1 permanent;
    }
    
    # Index redirection
    rewrite ^/?$ https://$host/admin/;

    # Backend API
    location /admin/
    {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Cookie $http_cookie;
    }
    
    # Site static content
    location /static/
    {
        alias /home/lqf/sites/thcloud.ml/CloudWebsite/AdminStatic/;
        try_files $uri $uri/ =404;
        expires 8d;
    }
}

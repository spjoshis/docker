# Setup
1. Run docker-compose up -d
2. Connect to ssh `docker exec -it odoo_mytyre /bin/bash`
3. When you setup connect the ssh and run below command
   1. `apt-get install wget libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libssl-dev libpq-dev libjpeg-dev -y`
   2. `pip3 install -r ./requirements.txt`
   3. `apt-get install nodejs npm -y`
   4. `npm install -g rtlcss`
   5. `apt-get install xfonts-75dpi -y`
   6. `wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb`
   7. `dpkg -i wkhtmltox_0.12.6-1.bionic_amd64.deb`
   8. `cp /usr/local/bin/wkhtmltoimage /usr/bin/wkhtmltoimage`
   9. `cp /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf`
   10. `./odoo-bin -c /etc/odoo-server.conf`
4. Run odoo application
   `./odoo-bin -c /etc/odoo-server.conf -d admin --db-filter=admin --addons-path=/mnt/extra-addons,addons`
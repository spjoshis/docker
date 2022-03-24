FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get upgrade -y

RUN adduser -system -home=/opt/odoo -group odoo

RUN apt-get install wget libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libssl-dev libpq-dev libjpeg-dev -y
RUN apt-get install nodejs npm xfonts-75dpi -y

RUN mkdir /var/lib/odoo
WORKDIR /var/lib/odoo

COPY src/requirements.txt /home/requirement.txt
RUN pip3 install psycopg2-binary
RUN pip3 install -r ./requirements.txt

RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb
RUN dpkg -i wkhtmltox_0.12.6-1.bionic_amd64.deb
RUN cp /usr/local/bin/wkhtmltoimage /usr/bin/wkhtmltoimage
RUN cp /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf

RUN mkdir /var/log/odoo
RUN chown odoo:odoo /var/log/odoo

#RUN chown -R odoo:odoo /var/lib/odoo/*
COPY config/odoo.conf /etc/odoo-server.conf

#RUN su - odoo -s /bin/bash
#RUN /var/lib/odoo
RUN ./odoo-bin -c /etc/odoo-server.conf
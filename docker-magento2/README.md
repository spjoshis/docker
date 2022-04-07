Docker Setup: https://www.mageplaza.com/kb/setup-magento-2-on-docker.html

Magento Setup:
php bin/magento setup:install \
--admin-firstname=John \
--admin-lastname=Doe \
--admin-email=brjoshi.up@gmail.com \
--admin-user=admin \
--admin-password='SomePassword123' \
--base-url=https://local.domain.com/ \
--base-url-secure=https://local.domain.com/ \
--backend-frontname=admin \
--db-host=mysql \
--db-name=magento \
--db-user=root \
--db-password=root \
--use-rewrites=1 \
--language=en_US \
--currency=USD \
--timezone=America/New_York \
--use-secure-admin=1 \
--admin-use-security-key=1 \
--session-save=files \
--use-sample-data


https://yegorshytikov.medium.com/how-to-use-react-js-with-magento-2-ed5e9f3cf9fe
https://github.com/Genaker/Luma-React-PWA-Magento-Theme


------------------
Commands:

bin/magento module:disable Magento_TwoFactorAuth
bin/magento cache:flush
bin/magento deploy:mode:show
bin/magento deploy:mode:set developer

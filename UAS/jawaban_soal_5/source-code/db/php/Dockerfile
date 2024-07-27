# source-code/db/php/Dockerfile
FROM php:7.4-fpm
WORKDIR /var/www/html
RUN docker-php-ext-install pdo pdo_mysql
COPY php.ini /usr/local/etc/php/php.ini
COPY www.conf /usr/local/etc/php-fpm.d/www.conf

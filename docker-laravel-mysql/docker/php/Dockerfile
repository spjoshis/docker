FROM php:8.1.3-fpm

RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-install pdo_mysql exif gd

# Download and install composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Create system user to run Composer and Artisan Commands
RUN useradd -G www-data,root -u 1000 -d /home/web-user web-user
RUN mkdir -p /home/web-user/.composer && \
    chown -R web-user:web-user /home/web-user

# Set working directory
WORKDIR /var/www

USER web-user

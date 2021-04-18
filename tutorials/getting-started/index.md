
# Getting started with Magic

There are multiple ways to use Magic, depending upon whether or not you just want to try it out locally
on your development machine, use the Docker images to more rapidly getting up to speed, or deploy it
to your production server. In this section we'll walk you through all of your options, starting with
the easiest method, to start out with Magic on your development machine.

## Using the Docker image on your development machine

The easiest way to get started is to [download the docker-compose.yml file](https://github.com/polterguy/magic/releases/download/v9.1.3/docker-compose.yml), assuming you have [Docker](https://www.docker.com/products/docker-desktop) installed, and then execute the following in a terminal window where you saved the file.
This is the exact same process for both Windows, Mac and Linux - And can also be extended
to install Magic in your server or cloud of choice. Notice, you'll need to have
[Docker installed](https://www.docker.com/products/docker-desktop) on your development machine if you want to
follow this approach.

```
docker-compose up
```

Then when the Docker containers have started, open your browser and go to [http://localhost:5555](http://localhost:5555),
and use the default configuration settings for MySQL, choose a root password, type your name and email address when
you generate a key pair, and Magic should work out of the box without having to mess with anything.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/2gos7BvNFkI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Manual code setup

If you don't want to use Docker, you can also configure your development environment locally on your
development machine using the code directly. If so you will first of all need the following components.

1. [Visual Studio](https://visualstudio.microsoft.com/downloads/) or [VS Code](https://code.visualstudio.com/download) + [DotNet CLI and SDK](https://dotnet.microsoft.com/download)
2. [NodeJS](https://nodejs.org/en/download/)
3. [Angular](https://angular.io/cli)
4. [MySQL](https://dev.mysql.com/downloads/mysql/) or [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)

In the video below I go through the manual setup process.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/CULMDMDPwws" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Deploy Magic to a VPS - BETA

**Notice** - This part is not entirely done quite yet, and you might have to fiddle with the `docker-compose.yml`
file a bit to make it work adequately. However, the basics of this file should be more or less done ...

The easiest way to deploy Magic into production, is to use the following docker-compose file.
Copy the content below into a file named `docker-compose.yml`, replace `servergardens.com` with your own
domain, replace thomas@servergardens.com with your own email address, make sure your server has Docker installed,
and execute `docker-compose up -d`. Then create two DNS A records for _"api"_ and _"magic"_ pointing
to your server's IP address, and after your Docker images have been started you can find the frontend
at `https://magic.your-domain.com`.

```bash
# Docker file to couple frontend, backend, MySQL database,
# nGinx reverse proxy, and LetsEncrypt instances into one.

# Replace the xxxxx.com parts with your own domain
# Then create two DNS A records pointing to the IP address of
# your server. Content of DNS records should be 'api' and 'magic'.

version: "2"

services:

  # This is the internet facing reverse proxy that routes
  # requests to either the frontend or the backend.
  # This is the only thing that's actually exposed to the internet.
  nginx-proxy:
    image: jwilder/nginx-proxy
    container_name: nginx-proxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - conf:/etc/nginx/conf.d
      - vhost:/etc/nginx/vhost.d
      - dhparam:/etc/nginx/dhparam
      - certs:/etc/nginx/certs:ro
      - /var/run/docker.sock:/tmp/docker.sock:ro
      - /usr/share/nginx/html
    networks:
      - proxy
    restart: always

  # This is the container that is responsible for retrieving
  # and renewing SSL certificates from LetsEncrypt
  letsencrypt:
    image: jrcs/letsencrypt-nginx-proxy-companion
    container_name: nginx-proxy-le
    volumes_from:
      - nginx-proxy
    volumes:
      - certs:/etc/nginx/certs:rw
      - /var/run/docker.sock:/var/run/docker.sock:ro
    networks:
      - proxy
    restart: always

  # This is our MySQL database
  db:
    image: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: ThisIsNotAGoodPassword
    volumes:
      - database:/var/lib/mysql
    networks:
      - proxy

  # Our Magic backend
  backend:
    image: servergardens/magic-backend:latest
    restart: unless-stopped
    depends_on:
      - db
      - letsencrypt
      - nginx-proxy
    volumes:
      - magic_files:/magic/files/modules/magic
      - crypto_keys:/magic/files/modules/system/crypto/keys
    environment:

      # REPLACE THESE NEXT 3 PARTS WITH YOUR OWN DOMAIN/EMAIL
      - VIRTUAL_HOST=api.servergardens.com
      - LETSENCRYPT_HOST=api.servergardens.com
      - LETSENCRYPT_EMAIL=thomas@servergardens.com
    networks:
      - proxy

  # Our Magic frontend (dashboard)
  frontend:
    image: servergardens/magic-frontend:latest
    restart: unless-stopped
    depends_on:
      - backend
    environment:

      # REPLACE THESE NEXT 3 PARTS WITH YOUR OWN DOMAIN/EMAIL
      - VIRTUAL_HOST=magic.servergardens.com
      - LETSENCRYPT_HOST=magic.servergardens.com
      - LETSENCRYPT_EMAIL=thomas@servergardens.com
    networks:
      - proxy

volumes:
  conf:
  vhost:
  dhparam:
  certs:
  database:
  magic_files:
  crypto_keys:

networks:
  proxy:
    external:
      name: nginx-proxy
```

## Support

If you have a support request of private nature, you can send me an
email at [thomas@servergardens.com](mailto:thomas@servergardens.com). If you want to submit a
feature request or a bug report, you can do such through the project's
[GitHub Issues](https://github.com/polterguy/magic/issues).

## License

Magic is 100% Open Source and free to use, also in proprietary and closed source applications.
The only exception is if you improve the frontend dashboard, or improve one of its plugins,
at which point you must make your improvements publicly available for others to use.

## Donate

If you want to buy me a cup of coffee, saying thx for the great work, I would appreciate
a [donation](https://servergardens.com/buy/).

* [Documentation](/documentation/)


## Using the Docker image on your development machine

The simplest way to get started is to [download the docker-compose.yml file](https://github.com/polterguy/magic/releases/download/v8.9.3/docker-compose.yml), assuming you have [Docker](https://www.docker.com/products/docker-desktop) installed, and then execute the following in a terminal window where you saved the file.
This is the exact same process for both Windows, Mac and Linux - And can also be extended
to install Magic in your server or cloud of choice.

```
docker-compose up
```

Then when the Docker containers have started, open your browser and go to [http://localhost:5555](http://localhost:5555), and use the default configuration settings for MySQL. Type
your name and email address when you generate a key pair, and Magic should work out of the box
without having to mess with anything.

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

## Deploy Magic to your Cloud

The simples way to deploy Magic into production, is to use the following docker-compose file.
Copy the content below into a file named `docker-compose.yml`, replace `xxxxx.com` with your own
domain, make sure your server has Docker installed, and execute `docker-compose up -d`. Then create
two DNS A records for _"api"_ and _"magic"_ pointing to your server's IP address, and after your
Docker images have been started you can find the frontend at `https://magic.your-domain.com`.

```bash
# Docker file to couple frontend, backend, MySQL database,
# nGinx reverse proxy, and LetsEncrypt instances into one.

# Replace the xxxxx.com parts with your own domain
# Then create two DNS A records pointing to the IP address of
# your server. Content of DNS records should be 'api' and 'magic'.

version: "2"

services:

  # This is the internet facing reverse proxy that routes
  # requests to either the frontend or the backend
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
    restart: always

  # This is our MySQL database
  db:
    image: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: ThisIsNotAGoodPassword
    volumes:
      - database:/var/lib/mysql

  # Our Magic backend
  backend:
    image: servergardens/magic-backend:latest
    restart: unless-stopped
    depends_on:
      - db
      - letsencrypt
      - nginx-proxy
    volumes:
      - files:/magic/files
    environment:
      - VIRTUAL_HOST=api.xxxxx.com
      - LETSENCRYPT_HOST=api.xxxxx.com
      - LETSENCRYPT_EMAIL=thomas@servergardens.com

  # Our Magic frontend (dashboard)
  frontend:
    image: servergardens/magic-frontend:latest
    restart: unless-stopped
    depends_on:
      - backend
    environment:
      - VIRTUAL_HOST=magic.xxxxx.com
      - LETSENCRYPT_HOST=magic.xxxxx.com
      - LETSENCRYPT_EMAIL=thomas@servergardens.com

volumes:
  conf:
  vhost:
  dhparam:
  certs:
  database:
  files:
```

### Licensing Magic

2 days after you install Magic on your cloud, _Magic will stop working_ unless you have
a valid license for Magic. To obtain a valid license click the navbar button in Magic
in the top/left corner, and select the _"Configuration"_ menu item. Choose the _"License"_
tab, and paste in your license key in the textarea at the middle of the screen. Click _"Apply"_
and you're fully licensed.

If you don't have a valid license key for Magic, you can click the _"obtain a valid license"_
hyperlink, that will allow you to purchase one.

![Getting licensed](https://servergardens.files.wordpress.com/2021/02/magic-license.png)

**Notice** - If Magic have already stopped working, you have to manually paste in your
license using your cloud vendor's SSH interface into your appsettings.json file on your
server. Please contact us at [license@servergardens.com](mailto:license@servergardens.com)
for information about how to fix Magic at this point, and to obtain a valid license. Once
the license have been successfully applied, your screen should resemble the following.

![license applied](https://servergardens.files.wordpress.com/2021/02/license-applied.png)

If you have troubles, or need professional support, please contact us
as [info@servergardens.com](mailto:info@servergardens.com).

# Support

If you have a support request of private nature, or a license inquiry, you can send us
email at [post@servergardens.com](mailto:post@servergardens.com). If you want to submit a
feature request or a bug report, you can do such through the project's
[GitHub Issues](https://github.com/polterguy/magic/issues).
Magic comes with professional support for Enterprise Licensed customers. Contact us for more
information about how to obtain an Enterprise License.

* [post@servergardens.com](mailto:post@servergardens.com)

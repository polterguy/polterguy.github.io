---
title: Deploy Magic
description: This article explains how to deploy Magic to a server once you're ready to put Magic into production
header:
  image: /assets/images/wizard-deploying-magic.webp
---

**Warning** - Magic Cloud is open source, and if you're a skilled software developer, you might be able to install it yourself on your own server - However, there is a reason why AINIRO.IO can make a living out of hosting it. Deploying and managing your own Magic installation is not for the faint at heart, the same way deploying and managing your own website is challenging. If you prefer a simpler solution, we do host Magic for a fee at AINIRO.IO.

* [Contact us](https://ainiro.io/contact-us)

## Deployment Guide

This guide helps you deploy Magic unto a VPS or a private server. The guide has been tested with
Ubuntu 20.04 (LTS) x64, but _might_ work with other Debian based distributions. You will need a
VPS instance somewhere, which you can buy at for instance [DigitalOcean](https://www.digitalocean.com/).
You will also need a domain and point _two_ DNS A records to your server's IP address. Typically
these would resemble the following.

* __api.yourdomain.com__
* __magic.yourdomain.com__

We suggest you don't buy the cheapest VPS droplet from DigitalOcean, but chose at least the one
that will cost you $12 per month. Their cheapest droplet simply doesn't have enough memory to
run Magic optimally. 2GB of memory should be enought to host the backend and the frontend
dashboard.

## Cloning docker-compose file

First use SSH to login to your VPS instance. This is typically achieved using something such as the following
on *Nix based systems.

```
ssh root@123.123.123.123
```

The IP address above needs to be the IP address of your VPS. After you've executed the above, you'll be
asked for your root password on your VPS instance. Notice, if you are using Windows you can use
[Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/), and/or
if you're using DigitalOcean you can use their web based terminal interface as an alternative. When you have
logged into your VPS you can clone magic.deploy into your VPS server using the following command.

```
git clone https://github.com/polterguy/magic.deploy.git
```

If the above gives you an error, you might need to install git using the following
command and then run the above command again afterwards.

```
apt install git
```

When you have successfully cloned this repository, you need to start docker-compose.

The `docker-compose.yml` file needs to be manually edited to provide your
email address, frontend domain, and backend domain, before you execute the docker-compose command.
You can do this with the following command.

```
nano docker-compose.yml
```

And then look through the file for the following YAML nodes.

```yaml
- VIRTUAL_HOST=magic-api.ainiro.io
- LETSENCRYPT_HOST=magic-api.ainiro.io
- LETSENCRYPT_EMAIL=thomas@ainiro.io

...

- VIRTUAL_HOST=magic.ainiro.io
- LETSENCRYPT_HOST=magic.ainiro.io
- LETSENCRYPT_EMAIL=thomas@ainiro.io
```

In total there are _6 entries_ you need to change, and the email address needs to be a valid email
address you own. The domain needs to be a sub-domain you own where you want to run your Magic
installation. When you are done editing the docker-compose.yml file, hold down the CTRL key and
click X, then type _"Y"_ when Nano asks you if you want to save the file after you have edited the
file, and save it with its existing filename. When you are done execute the following command in
your terminal. This installs docker for you, in addition to docker compose.

```
apt install docker docker-compose
```

After you have installed docker and docker compose, you have to create a virtual docker network.
This is necessary to make sure your containers have a virtual network to communicate with each other.

```
docker network create nginx-proxy
```

This command will create a docker proxy network Magic needs to be able to connect
all the docker images within your docker-compose file with each other. When you have created the
above network, you can start your docker containers using the following command.

```
docker-compose up -d
```

## Internals

The above `docker-compose up -d` command will start 4 docker containers.

* `proxy` - The nGinx proxy that internally routes requests to either your backend or your frontend
* `acme` - The container responsible for retrieving and renewing LetsEncrypt SSL certificates for you
* `backend` - The main Magic backend container
* `frontend` - The main Magic dashboard frontend container

In addition to the above containers, docker will also create several volumes for you. These volumes
are required to persist changes to the file system for your containers, such that if your containers
are stopped for some reasons, and/or you update Magic later, you will keep your changes. The most
important volumes that Magic itself relies upon are as follows.

* __magic_etc_files__ - Where Magic stores its _"etc"_ files
* __magic_modules_files__ - Where Magic stores its _"modules"_ files
* __magic_config_files__ - Where Magic stores its _"appsettings.json"_ file
* __magic_data_files__ - Where Magic stores its SQLite database files

The rest of the volumes are documented in either of the following two container projects that Magic's
internal deployment depends upon.

* [nGinx Proxy](https://github.com/nginx-proxy/nginx-proxy)
* [Acme companion](https://github.com/nginx-proxy/acme-companion)

The first project above creates the nGinx proxy that _"routes"_ requests to the correct container
according to the host name specified in your HTTP requests. The second is to install a LetsEncrypt
SSL certificate key pair for both your backend and frontend, ensuring you've got encrypted HTTPS
communication to both your backend and your frontend.

## Configuring Magic

You can now visit your frontend domain and setup Magic. As you click the login button, you have to
provide Magic with your backend API URL. This is achieved by simply pasting in your backend API URL
into the top textbox and click the tab key on your keyboard. If your domain was _"yourdomain.com"_, and
you created your DNS records as illustrated above, your API backend URL would be the following.

```
https://magic-api.yourdomain.com
```

To configure Magic login with _"root/root"_. Then provide Magic with a root
password, and follow the wizard to the end. This process is similar to the process you follow as you
configure Magic locally on your development machine. This should resemble the following.

![Initially configuring Magic](/images/setup-magic.jpeg)

## Securing your VPS

You might want to install a firewall on your Linux server to further secure your installation. This can be done
by executing the following commands in order of appearance.

```
apt install ufw; ufw allow 80; ufw allow 443; ufw allow 22; ufw enable;
```

The above will install _"Uncomplicated FireWall"_ on your server, for then to shut off all ports except
port 80, 443 and 22. 22 is needed to allow for SSH into your server. In addition, you would probably benefit
from making sure your operating system is updated with the latest patches as released by whomever is
distributing your particular Linux installation.

## Updating Magic

Updating Magic should be fairly straight forward and only requires that you tear down your containers,
pull the Magic images from docker hub, and restart your containers using the following.

```
docker-compose down
docker pull servergardens/magic-frontend
docker pull servergardens/magic-backend
docker-compose up -d
```

## Copyright and maintenance

The projects is copyright Thomas Hansen 2023 - 2024, and professionally maintained by [AINIRO.IO](https://ainiro.io).

---
title: Deploy Magic
description: How to deploy Magic to a server once you're ready to put Magic into production
header:
  image: /assets/images/wizard-deploying-magic.webp
---

Notice, this guide requires that you have obtained a single server license or a Kubernetes cluster license, and that you have access to Magic's source code somehow, and/or its Docker images. You can [contact Thomas](mailto:thomas@ainiro.io) to obtain such a license and get access.

This guide helps you deploy Magic unto a VPS or a private server. The guide has been tested with Ubuntu 20.04 (LTS) x64, but _might_ work with other Debian based distributions. You will need a VPS instance somewhere first. You will also need a domain and point _two_ DNS A records to your server's IP address. Typically these would resemble the following.

* __api.YOURDOMAIN.COM__
* __magic.YOURDOMAIN.COM__

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

If the above gives you an error, you might need to install git using the following command and then run the above command again afterwards. You will also obviously need to have read only access to the _"magic.deploy"_ GitHub repository.

```
apt install git
```

When you have successfully cloned this repository, you need to start docker-compose, but this file needs to be edited before you can start it.

The `docker-compose.yml` file needs to be manually edited to provide your email address, frontend domain, and backend domain, before you execute the docker-compose command. You can do this with the following command.

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

In total there are _6 entries_ you need to change, and the email address needs to be a valid email address you own. The domain needs to be a sub-domain you own where you want to run your Magic installation, and you will need to setup both of these sub-domains as A records with your DNS provider. If you have created your own Docker images from Magic's source code, you will need to edit the following parts of your docker-compose file to use your own images.

* image: servergardens/magic-backend:latest
* image: servergardens/magic-frontend:latest

When you are done editing the docker-compose.yml file, hold down the CTRL key and click X, then type _"Y"_ when Nano asks you if you want to save the file after you have edited the file, and save it with its existing filename. Then you will have to install Docker and docker-compose on your VPS. This can be achieved with the following terminal command.

```
apt install docker docker-compose
```

After you have installed docker and docker compose, you will need to login to Docker Hub with a username and password combination that can access your images. This can be accomplished using the following.

```bash
docker login
```

This ensures your machine persists your Docker hub credentials, and attaches these as you try to retrieve the docker images required to get Magic up running. Then you have to create a virtual docker network. This is necessary to make sure your containers have a virtual network to communicate with each other.

```
docker network create nginx-proxy
```

This command will create a docker proxy network Magic needs to be able to connect
all the docker images within your docker-compose file with each other. When you have created the
above network, you can start your docker containers using the following command.

```
docker-compose up -d
```

If you want to debug the containers, you can drop the `-d` argument, which will ensure dockers writes errors to the console as it proceeds. Notice, the default docker-compose file will take care of SSL automatically using Acme and LetsEncrypt. If you want to use your own SSL certificates here instead, you're on your own.

## Internals

The above `docker-compose up -d` command will start 4 docker containers.

* `proxy` - The nGinx proxy that internally routes requests to either your backend or your frontend
* `acme` - The container responsible for retrieving and renewing LetsEncrypt SSL certificates for you
* `backend` - The main Magic backend container
* `frontend` - The main Magic dashboard frontend container

In addition to the above containers, docker will also create several volumes for you. These volumes are required to persist changes to the file system for your containers, such that if your containers are stopped for some reasons, and/or you update Magic later, you will keep your changes. The most important volumes that Magic itself relies upon are as follows.

* __magic_etc_files__ - Where Magic stores its _"etc"_ files
* __magic_modules_files__ - Where Magic stores its _"modules"_ files
* __magic_config_files__ - Where Magic stores its _"appsettings.json"_ file
* __magic_data_files__ - Where Magic stores its SQLite database files

Notice, there are two dynamic folders that Magic will _not_ create volumes for, these are your _"system"_ and _"misc"_ folders. These folders will contain system files the middleware itself depends upon to function, and might be updated as we publish new releases. You should _not change_ files in these folders, since once you restart your container, and/or update Magic, all your changes here will be overwritten. These folders and files will be marked as red (warning) in Hyper IDE if you display your system folders to prevent accidental editing.

The rest of the volumes are documented in either of the following two container projects that Magic's internal deployment containers depends upon.

* [nGinx Proxy](https://github.com/nginx-proxy/nginx-proxy)
* [Acme companion](https://github.com/nginx-proxy/acme-companion)

The first project above creates the nGinx proxy that _"routes"_ requests to the correct container according to the host name specified in your HTTP requests. The second is to install a LetsEncrypt SSL certificate key pair for both your backend and frontend, ensuring you've got encrypted HTTPS communication to both your backend and your frontend.

## Configuring Magic

You can now visit your frontend domain and setup Magic. When you login you have to provide Magic with your backend API URL. This is achieved by providing your backend API URL before you login. If your domain was _"yourdomain.com"_, and you created your DNS records as illustrated above, your API backend URL would be the following.

```
https://api.YOURDOMAIN.COM
```

To configure Magic login with _"root"_/_"root"_. Then provide Magic with a root password, and follow the wizard to the end. This process is similar to the process you follow as you configure Magic locally on your development machine. This should resemble the following.

![Screenshot of initially configuring Magic after installing it on your VPS](/images/setup-magic.jpeg)

## Securing your VPS

You might want to install a firewall on your Linux server to further secure your installation. This can be done by executing the following commands in order of appearance.

```
apt install ufw; ufw allow 80; ufw allow 443; ufw allow 22; ufw enable;
```

The above will install _"Uncomplicated FireWall"_ on your server, for then to shut off all ports except port 80, 443 and 22. 22 is needed to allow for SSH into your server. In addition, you would probably benefit from making sure your operating system is updated with the latest patches as released by whomever is distributing your particular Linux installation.

## Updating Magic

Updating Magic should be fairly straight forward and only requires that you tear down your containers, pull the Magic images from docker hub, and restart your containers using the following commands from the same directory where you'we got your docker-compose file.

```
docker-compose down
docker pull servergardens/magic-frontend
docker pull servergardens/magic-backend
docker-compose up -d
```

## Additional parts

If you want to use something else besides LetsEncrypt, you will have to figure out how to do this yourself. We will of course assist, but we don't have documentation for anything besides LetsEncrypt.

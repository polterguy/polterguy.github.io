---
title: Getting Started
description: This article is about how to get started with Magic Cloud using Docker, and start leveraging its Low-Code and No-Code features in your own systems
header:
  image: /assets/images/getting-started.webp
  image_description: Baby Wizard waving his magic wand over his magic hat to practice his spell casting
---

The easiest way to get started with Magic is to [signup for a cloudlet at AINIRO.IO](https://ainiro.io). However, if you want to install Magic on your own server, this is very much possible. The easiest way to do this is to use the Docker images.

## Using Docker

Below is a docker-compose file you can use that downloads the images and starts the correct containers.

```yaml
version: "3.3"
services:
  magic_backend:
    image: servergardens/magic-backend:latest
    container_name: magic_backend
    restart: always
    ports:
      - "4444:4444"
    volumes:
      - magic_files_etc:/magic/files/etc
      - magic_files_data:/magic/files/data
      - magic_files_config:/magic/files/config
      - magic_files_modules:/magic/files/modules
  magic_frontend:
    image: servergardens/magic-frontend:latest
    container_name: magic_frontend
    depends_on:
      - backend
    restart: always
    ports:
      - "5555:80"
volumes:
  magic_files_etc:
  magic_files_data:
  magic_files_config:
  magic_files_modules:
```

The above file will spawn the frontend at port 5555 and the backend at port 4444. The above file creates volumes for all the important folders, that contains files you typically change as you're using Magic. The _"/misc/"_ and _"/system/"_ folders should not have volumes, since these should be changed when you update your image.

Once your containers are up running you need to use your browser to navigate to `localhost:5555`, and login to your backend. Your backend can be found at `localhost:4444`, and its username is _"root"_ and its password is _"root"_. Once you've logged in, you'll be asked to setup Magic. This will resemble the following.

![Initially configuring Magic](/images/setup-magic.jpeg)

After you've provided a root password, your name, and your email address, you will be redirected to the main dashboard and you can start using Magic.

## Deploy to production

If you want to deploy Magic to production we have created a detailed description [here](/deploy/). To deploy Magic requires a lot of technical knowledge, and to maintain it requires knowledge about security, CDNs, etc. 

Unless you're a highly skilled and professional software developer, and you're willing to spend dozens of hours installing Magic, we do _not_ encourage you to do this. There's a reason we charge $198 per month as a starting price for a cloudlet at AINIRO.IO.

If you don't have these skills, [AINIRO.IO](https://ainiro.io) can do it for you, in exchange for a monthly fee, at which point you get professional support, installation, maintenance, upgrades, and everything else required to create and maintain Magic. However, if you cannot afford our services, and you're willing to do everything yourself, you can use the above link to deploy Magic to your own server.

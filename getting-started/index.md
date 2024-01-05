---
title: Getting Started
description: This article is about how to get started with Magic Cloud and start leveraging its Low-Code and No-Code features
header:
  image: /assets/images/getting-started.png
---

The easiest way to get started with Magic is to [signup for a cloudlet at AINIRO.IO](https://ainiro.io). However, if you want to install Magic on your own server, this is very much possible. The second easiest way to get started is to use the Docker images.

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

---
title: Getting Started
description: This article is about how to get started with Magic Cloud using Docker, and start leveraging its Low-Code and No-Code features in your own systems
header:
  image: /assets/images/getting-started.webp
  image_description: Baby Wizard waving his magic wand over his magic hat to practice his spell casting
---

The easiest and least expensive way to get started with Magic is to [signup for a cloudlet at AINIRO.IO](https://ainiro.io/buy). However, if you have purchased a single server license, or a Kubernetes license, you have been given access to its source code - At which point you can install Magic locally on your own development machine. The easiest way to get started with the source code is to use Docker.

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

Notice, the above images are private and only clients having purchased a license can access these images. You also might want to consider creating your own images and push to for instance Docker hub as private images for your organisation, instead of using our images. Magic contains Docker files and GitHub workflows to easily allow you to create your own images. If you do, you will have to change the images in the above docker-compose file.

The above file will spawn the frontend at port 5555 and the backend at port 4444. The above file creates volumes for all the important folders, that contains files you typically change as you're using Magic. The _"/misc/"_ and _"/system/"_ folders should not have volumes, since these should be changed when you update your image.

Once your containers are up running you need to use your browser to navigate to `localhost:5555`, and login to your backend. Your backend can be found at `localhost:4444`, and its username and password is _"root"_ and _"root"_. Once you've logged in, you'll be asked to setup Magic. This will resemble the following.

![Screenshot of how to initially configure Magic](/images/setup-magic.jpeg)

After you've provided a root password, your name, and your email address, you will be redirected to the main dashboard and you can start using Magic.

## Using the source code version

If you've got an enterprise license plan, you should have been given read only access to Magic's source code. Clone the repository, make sure you've got .Net Core version 8 installed, the latest version of NodeJS, and Angular, and enter the _"backend"_ and _"frontend"_ folders with two terminal windows, and execute the following commands in the respective terminals.

1. `dotnet run`
2. `ng serve`

After some few minutes you should be able to access the dashboard from `localhost:4200`, and login to your cloudlet using `http://localhost:5000` as your backend URL. The intial username and password combination is the same; _"root"_ and "_root"_.

## Deploy to production

If you want to deploy Magic to production we have created a detailed description [here](/deploy/). To deploy Magic requires a lot of technical knowledge, and to maintain it requires knowledge about security, CDNs, etc - However, help with this is an integrated part of our Single Server license plan and Kubernetes Cluster license plans.

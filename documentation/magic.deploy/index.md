
# Magic Deploy

This guide helps you deploy Magic unto a VPS or a private server. The guide depends upon Docker,
hence you'll need to have [Docker installed](https://docs.docker.com/engine/install/). Make sure you've
got Docker before you proceed. The guide has been tested with Ubuntu 20.04 (LTS) x64, but might work with
other Debian based distributions.

You will also need to point _two_ DNS A records to your server's IP address. Typically these would
resemble the following.

* __api.yourdomain.com__ - The Magic backend 
* __magic.yourdomain.com__ - The Magic frontend/dashboard

## Start

First clone the entire project into your VPS server using the following command.

```
git clone https://github.com/polterguy/magic.deploy.git
```

**Notice** - If the above gives you an error, you might need to install git using the following
command and then run the above command again afterwards.

```
sudo apt install git
```

When you have successfully cloned this repository, change into the `magic.deploy` folder
using the following command.

```
cd magic.deploy
```

**Notice** - The `docker-compose.yml` file needs to be manually edited to provide it with your
email address, frontend domain, and backend domain before you execute the docker-compose command.
You can do this with the following command.

```
nano docker-compose.yml
```

And then look through the file for the following YAML nodes.

```
- VIRTUAL_HOST=api.servergardens.com
- LETSENCRYPT_HOST=api.servergardens.com
- LETSENCRYPT_EMAIL=thomas@servergardens.com
```

In addition to these YAML nodes.

```
- VIRTUAL_HOST=magic.servergardens.com
- LETSENCRYPT_HOST=magic.servergardens.com
- LETSENCRYPT_EMAIL=thomas@servergardens.com
```

In total there are _6 entries_ you need to change, and the email address needs to be a valid email
address you own. The domain needs to be a sub-domain you own where you want to run your Magic
installation. When you are done editing the docker-compose.yml file, hold down the CTRL key and
click X, then choose Y when Nano asks you if you want to save the file after you have edited the
file. When you are done editing the _"docker-compose.yml"_ file, you can execute the following
command in your terminal.

```
sudo docker network create nginx-proxy
```

If the above gives you an error, you might need to install docker using `sudo apt install docker`.

This command will create the your Docker proxy network, which Magic will need to be able to connect
all the docker images within your docker-compose file. When you have created the above network, you
can start your docker containers using the following command.

```
sudo docker-compose up -d
```

If the above gives you an error, you might need to install docker-compose using `sudo apt install docker-compose`.

The above will start 5 docker containers.

* `nginx-proxy` - The nGinx proxy that internally routes requests to either your backend or your frontend
* `letsencrypt` - The container responsible for retrieving and renewing LetsEncrypt SSL certificates for you
* `db` - Your MySQL database, used to create the _"magic"_ database, which Magic internally depends upon
* `backend` - The main Magic backend container
* `frontend` - The main Magic dashboard frontend container

You can now visit your frontend domain, and setup Magic, assuming you've pointed your DNS A records to
the IP address of your virtual server. Notice, to configure Magic login with _"root/root"_ and do _not_
change the database connection string, but choose _mysql_ as your database type, and provide Magic with
a root password, and just follow the wizard to the end. This process is similar to the process you followed
as you configured Magic locally on your development machine.

**Notice** - The _"appsettings.json"_ file will be mounted as an external file reference by Docker, and
this file will contain your Magic settings. _Do not delete this file_ since it's crucial for Magic to
work. However, be careful with the file, since it contains your database connection strings, JWT secret,
and other _highly sensitive information_. _Do not send this file on email or share it with anybody_ unless
you absolutely trust the other party.

## Installing a generated Angular frontend

Once you have generated an Angular frontend, you can just as easily install this on the same VPS. This
is possible since the generated frontend also contains a _"docker-compose.yml"_ file. The simplest way
to do this is to import your Angular frontend into for instance [GitHub](https://github.com) as for
instance a private repository, and then clone your repository locally on your VSP server. To retrieve
the generated frontend on your VPS, assuming your username on GitHub is _"foo"_ and the project name is
_"bar"_, you could run the following command.

```
git clone https://github.com/foo/bar.git
```

Then you need to change into your _"bar"_ directory with the following command.

```
cd bar
```

Notice, at this point you will have to _manually edit the "docker-compose.yml" file_ the same
way you did for the main Magic docker-compose file. In this file you will find the following
section.

```
- VIRTUAL_HOST=sakila.servergardens.com
- LETSENCRYPT_HOST=sakila.servergardens.com
- LETSENCRYPT_EMAIL=thomas@servergardens.com
```

You might want to edit the container's name too, which you can find at the top of this file.
The above values needs to be exchange with your own domain, and your own email address. Once you've edited
this file using for instance `nano docker-compose.yml`, you can start your docker container using the
following command.

```
docker-compose up -d
```

At this point you should have your frontend up running on the sub-domain you chose as you edited the file,
assuming you have added a DNS A record pointing to the IP address of your server.

## Securing your VPS

You might want to install a firewall on your Linux server to further secure your installation. This can be done
by executing the following commands in order of appearance.

```
sudo apt install ufw
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 22
sudo ufw enable
```

The above will install _"Uncomplicated FireWall"_ on your server, for then to shut off all ports except
port 80, 443 and 22. 22 is needed to allow for SSH into your server. In addition, you would probably benefit
from making sure your operating system is updated with the latest patches as released by whomever is
distributing your particular Linux installation.

## Too complicated?

We can [do this for you](https://servergardens.com), including hosting your app, making sure it is
correctly secured. Of course, this is a service we charge for, but at least that way you get to sleep
better at night, realising you've got the mastros in regards to this taking care of your server farm.

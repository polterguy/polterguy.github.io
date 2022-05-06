
# How to deploy Magic to your VPS

This guide helps you deploy Magic unto a VPS or a private server. The guide has been tested with
Ubuntu 20.04 (LTS) x64, but _might_ work with other Debian based distributions. You will need a
VPS instance somewhere, which you can buy at for instance [DigitalOcean](https://www.digitalocean.com/).
You will also need a domain and point _two_ DNS A records to your server's IP address. Typically
these would resemble the following.

* __api.yourdomain.com__
* __magic.yourdomain.com__

We suggest you don't buy the cheapest VPS droplet from DigitalOcean, but chose at least the one
that will cost you $12 per month. Their cheapest droplet simply doesn't have enough memory to
run Magic optimally. 2GB of memory should be enought to host Magic, MySQL, and the frontend
dashboard.

## Installing Magic

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

When you have successfully cloned this repository, change into the `magic.deploy` folder
using the following command.

```
cd magic.deploy
```

The `docker-compose.yml` file needs to be manually edited to provide your
email address, frontend domain, and backend domain, before you execute the docker-compose command.
You can do this with the following command.

```
nano docker-compose.yml
```

And then look through the file for the following YAML nodes.

```yaml
- VIRTUAL_HOST=magic-api.aista.com
- LETSENCRYPT_HOST=magic-api.aista.com
- LETSENCRYPT_EMAIL=th@aista.com

...

- VIRTUAL_HOST=magic.aista.com
- LETSENCRYPT_HOST=magic.aista.com
- LETSENCRYPT_EMAIL=th@aista.com
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

The above `docker-compose up -d` command will start 5 docker containers.

* `proxy` - The nGinx proxy that internally routes requests to either your backend or your frontend
* `acme` - The container responsible for retrieving and renewing LetsEncrypt SSL certificates for you
* `db` - Your MySQL database, used to create the _"magic"_ database that Magic internally depends upon
* `backend` - The main Magic backend container
* `frontend` - The main Magic dashboard frontend container

In addition to the above containers, docker will also create several volumes for you. These volumes
are necessary to persist changes to the file system for your containers, such that if your containers
are stopped for some reasons, and/or you update Magic later, you will keep your changes. The most
important volumes that Magic itself relies upon are as follows.

* __database__ - Where MySQL store its database files
* __etc_magic_folder__ - Where Magic stores its _"etc"_ files
* __modules_magic_folder__ - Where Magic stores its _"modules"_ files
* __config_magic_folder__ - Where Magic stores its _"appsettings.json"_ file

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

To configure Magic login with _"root/root"_ and choose _mysql_ as your database type. Do _not_ change
any parts of the connection string unless you know what you're doing. Then provide Magic with a root
password, and follow the wizard to the end. This process is similar to the process you follow as you
configure Magic locally on your development machine.

## Installing a generated Angular frontend

Once you have installed Magic you probably want to check out its capabilities in regards to Low-Code
and No-Code, which is easily achieved by going to the SQL menu item in your dashboard, click the Load
button, choose _"sakila"_, and then click execute. This creates a database for you called sakila.
For the record, you can of course choose any existing database you have, or an alternative create
database MySQL script you've got.

After you've done the above you can go back to your dashboard in Magic and choose the _"CRUD"_
menu item. Then click the little spiral arrow to refresh your server side cache, and once the page
reloads choose the database you just created and click _"Crudify all tables"_. Then choose the _"Frontend"_
tab at the top of your page, give your app a name, choose the _"angular"_ template, choose a _"Deployment domain"_
being the URL where you want to deploy your frontend, and click _"Generate"_.
After a couple of seconds you should be given a ZIP file as a download. If you don't get a ZIP file,
make sure you disable popup blockers in your browser and click _"Generate"_ once more.

If you want to crudify your own database here, you can easily do so by adding a connection string
to an existing database through the _"Config"_ menu item, and then choose your own connection string's
name as you crudify your backend. If you do this you can choose any Microsoft SQL Server, MySQL, or
PostgreSQL database connection string.
Once you have generated an Angular frontend, you can easily install this on the same VPS. This
is possible since the generated frontend also contains a _"docker-compose.yml"_ file. The easiest way
to do this is to upload your generated ZIP file to your VPS container using for instance the following
from your local development machine. Yet again, use your VPS' IP address here.

```
scp foo.zip root@123.123.123:~
```

Then login to your VPS through your terminal, unzip the file and change into the unzipped folder with
something such as the following.

```
unzip foo.zip
cd foo
```

If you get an error when executing the above unzip command, you can install unzip on your VPS using the
following command and rerun the above commands afterwards.

```
apt install unzip
```

When you have unzipped your Angular frontend you can start your docker container using the following
command in your VPS from within your unzipped Angular frontend folder.

```
docker-compose up -d
```

The above assumes you have configured a DNS A record pointing to your virtual machine with
the URL of where you want to deploy your frontend, and that you used this URL as you generated
your frontend - In addition to that you _generated your app on your Magic VPS instance_. The last part
is important since by default a generated Angular frontend will use the same API URL as the URL
you are using to generate your frontend. At this point you should have your frontend up running on
the sub-domain you chose as you generated your frontend. Now simply visit this URL in your browser,
and after some 5 minutes of negotiating a new SSL certificate from LetsEncrypt your Angular app
should work. Use your default Magic _"root"_ credentials to login to your generated Angular frontend.

## Securing your VPS

You might want to install a firewall on your Linux server to further secure your installation. This can be done
by executing the following commands in order of appearance.

```
apt install ufw
ufw allow 80
ufw allow 443
ufw allow 22
ufw enable
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
docker pull aistamagic/magic-frontend
docker pull aistamagic/magic-backend
docker-compose up -d
```

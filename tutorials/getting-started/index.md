
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

As of version 8.9.4 Magic contains a _"docker-compose.yml"_ file that almost completely
automates the process of deploying Magic to your Cloud vendor of choice. The rest of this
section describes how to setup Magic using [DigitalOcean](https://www.digitalocean.com),
but the process would be very similar with any Cloud vendor such as Azure or AWS.

### Create a "Droplet" at DigitalOcean

First visit [DigitalOcean](https://www.digitalocean.com) and sign up for their services,
and create a _"droplet"_. A droplet is a virtual server, and you can create one
for as little as $5 per month. They also provide you with free credits once you sign up,
so you don't have to pay _anything_ initially to deploy your Magic server. See the screenshot
below for an example of such a droplet. Make sure you choose Ubuntu as your server. We're using
Ubuntu version 20.04, but the process should be similar with other versions of Ubuntu.

![Create Droplet](https://servergardens.files.wordpress.com/2021/02/create-droplet.png)

Choose a region for your droplet, preferably geographically close to where you intend to access it from,
and then make sure you choose a root password for your droplet. This password should be very
hard to guess, for security reasons, since it provides full access to your server.

![Create root password for droplet](https://servergardens.files.wordpress.com/2021/02/create-root-password.png)

Choose a hostname and click the create button at the bottom.

![Create droplet](https://servergardens.files.wordpress.com/2021/02/hostname-create.png)

### Installing Docker in your droplet

When the droplet has been created, you can click on it, and click the _"Console"_ link in
the top/right corner of the page

![Open the droplet terminal](https://servergardens.files.wordpress.com/2021/02/open-console.png)

This will open a terminal window in your browser, giving you access to SSH into your droplet. Type
_"root"_ as your username, and your root password afterwards to login to the server.

![droplet root login](https://servergardens.files.wordpress.com/2021/02/droplet-terminal-login.png)

Afterwards install docker by typing the following into your terminal window.

```
snap install docker
```

Your screen should now look like the following.

![install docker](https://servergardens.files.wordpress.com/2021/02/install-docker.png)

### Installing Magic on your droplet using Docker

Click enter once the installation process is done, and type the following into your terminal

```
curl -L "https://gist.githubusercontent.com/polterguy/f16f74fdffae67f762715ba5d60f9177/raw/8d8fb79a4c80ad2bfb04a46d1c07cdad29ea2661/gistfile1.txt" -o "docker-compose.yml"
```

This will download a default _"docker-compose.yml"_ file for you, which you'll have to
modify before you can mount. Type the following into your terminal once the above download is done.

```
sudo nano docker-compose.yml
```

Use your arrow keys to move your cursor down to the section where it says `ALLOWED_DOMAINS`
and modify the `domain` and `api-domain` values here to the frontend and backend
DNS A record you intend to use for your Magic server. For instance, if you own the domain
_"example.com"_ you might want to use _"magic.example.com"_ for the Magic frontend, and
_"api.example.com"_ for your Magic backend. You can see how I edited the file myself in the
screenshot below.

![Modifying docker file](https://servergardens.files.wordpress.com/2021/02/adding-domains.png)

**Notice** - There are four places in total you have to edit this file. Change the domains in
both the `ALLOWED_DOMAINS` part, in addition to the `SITES` part. It is _crucial that you keep all other parts of this file exactly as it is._

For reference purposes, this is how my file ended up looking like.

```
version: "3.3"

services:

  db:
    image: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: ThisIsNotAGoodPassword
    volumes:
      - database:/var/lib/mysql

  backend:
    image: servergardens/magic-backend:latest
    depends_on:
      - db
    restart: always
    ports:
      - 4444:80
    volumes:
      - files:/files
      - settings:/appsettings.json

  frontend:
    image: servergardens/magic-frontend:latest
    depends_on:
      - backend
    restart: always

  nginx:
    image: valian/docker-nginx-auto-ssl
    restart: always
    ports:
      - 80:80
      - 443:443
    volumes:
      - ssl_data:/etc/resty-auto-ssl
    environment:
      ALLOWED_DOMAINS: '(magic.servergardens.com|api.servergardens.com)'
      SITES: 'magic.servergardens.com=frontend:80;api.servergardens.com=backend:4444'

volumes:
  database:
  files:
  settings: 
  ssl_data: 
```

When you have changed your file, click CTRL+X and click "Y" once asked if you want to save
your file, for then to click enter to use the existing filename.

You can now start your Magic docker containers, using the following command.

```
docker-compose up -d
```

After a couple of minutes your screen should look like the following.

![docker-compose up](https://servergardens.files.wordpress.com/2021/02/docker-compose-up.png)

Magic has now been successfully started on your droplet server. What this actually does,
is to create 4 Docker containers on your droplet.

* MySQL database
* Magic frontend
* Magic backend
* nGinx proxy server

The nGinx proxy server is there to route requests according to the hostname specified
in HTTP invocations, to either your Magic frontend or your Magic backend. All requests
coming in to your droplet's IP address with the hostname of _"magic.servergardens.com"_
will be routed to the frontend Angular parts of Magic. All requests with _"api.servergardens.com"_
will be routed to my Magic backend. Your exact domain would of course be different, depending
upon which domain you want to use Magic with. However, the logic is the same. The nGinx server
will also _automatically install an SSL certificate on your server_ using LetsEncrypt, so
this should be a fairly secure setup.

The only part of these 4 Docker containers that is actually exposed outside of your virtual
network and accessible over the internet, is the nGinx server - Hence your MySQL password
is not really that important, unless you intend to expose your MySQL server instance later
over the internet. Hence, all settings from the docker-compose file can be fairly securely
used as is, assuming you chose a _strong root password when you created your droplet_.

### Modifying your DNS record

This step is different depending upon where you host your domain, but the process is similar,
and implies creating _two_ DNS A records, one for your frontend domain, and another for
your backend domain. For me using WordPress to host my domain, this looks like the following.

![WordPress DNS A records](https://servergardens.files.wordpress.com/2021/02/api-frontend-dns-a-records.png)

At this point you need to copy your droplet's *public* IP address. If you go back to your
main DigitalOcean page for your droplet, you will typically see your server's public IP
address in the top left corner, such as the following screenshot illustrates.

![droplet public IP address](https://servergardens.files.wordpress.com/2021/02/public-ip-address.png)

Copy your droplet's public IP address, and create a DNS record using your domain provider's
DNS interface. For me using WordPress this looks like the following.

![DNA A record](https://servergardens.files.wordpress.com/2021/02/dns-a-record.png)

**Notice** - You have to create _two_ DNS A records. One for your backend and one for your
frontend. These must match the domains you used in the beginning as you edited your _"docker-compose.yml"_
file. Below you can see how I did it using WordPress.

![Magic DNS records](https://servergardens.files.wordpress.com/2021/02/api-frontend-dns-a-records.png)

**Notice** - At this point, it might take some time for your DNS entry to kick in, depending
upon your domain hosting provider, and your domain's Time To Live (TTL) settings. Once the
changes have gone through though, you can access your Magic server with the frontend domain
name you chose during the above setup process. For me, this is
[magic.servergardens.com](https://magic.servergardens.com).

If you are restless you can speed up the domain propagations by flushing your local machine's
DNS cache. For me on my Mac this implies running the following command in a terminal window.

```
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
```

Once the DNS entry has kicked in, you can access your site using your frontend's URL. If you want
to test my server you can go [magic.servergardens.com](https://magic.servergardens.com)

The first time you visit your server, it will take some time, since the nGinx proxy container
will generate an SSL certificate from LetsEncrypt, to ensure you have an encrypted HTTPS channel
for both your backend and your frontend. The nGinx proxy server will also automatically take
care of renewals of your certificate, and provide sane defaults for you, when installing
the certificate.

### Configuring Magic

The first time you access your Magic server, you will have to configure it. Click the login button
in the top right corner (the lock), and type the API URL into the textbox at the top. For me this
is the following URL.

```
https://api.servergardens.com
```

It's important that you _only_ type the domain parts, and not additional slashes or anything.
Then use _"root"_ as your username and _"root"_ as your password, and click the login button.
After logging in for the first time, you will have to configure Magic. This implies choosing which
database instance to use, and provide Magic with a root password. The docker-compose file above
only includes MySQL, so even though Magic supports both MySQL and SQL Server out of the box,
you'll have to choose MySQL as your database type at this point. Leave the MySQL connection
string _exactly as is_, choose a root password, repeat it, and click the next button.

**Notice** - It is _crucial_ that you choose a _very strong root password for Magic_, since
the root password grants anyone _full access_ to your Magic server.

![Configuring database](https://servergardens.files.wordpress.com/2021/02/configuring-magic.png)

Then you will have to crudify your Magic database, which basically creates your backend, wrapping
your Magic database. Please don't modify anything at this point, unless you are 100% certain of
the consequences - Just click the next button once more.

![Crudifying database](https://servergardens.files.wordpress.com/2021/02/crudify-magic.png)

Then type your name and email address in at the top of the form, and leave everything else
as is. This will create a cryptography key pair for your Magic server, allowing you to
use the cryptography features in it later. If you want to, you can modify the _"seed"_
parts, but this should not be necessary.

![Key pair](https://servergardens.files.wordpress.com/2021/02/name-and-email.png)

Then you can optionally run all assumptions in the system, which will sanity check your system.

![running assumptions](https://servergardens.files.wordpress.com/2021/02/run-assumptions.png)

Notice how I had to edit one of my assumptions to make it execute successfully. You can see how
in the screenshot below.

![Editing assumption](https://servergardens.files.wordpress.com/2021/02/edit-assumption.png)

Notice how I changed the `http://localhost:55247` parts with `https://api.servergardens.com`
being the URL of my backend API to make the assumption succeed. Then I saved the assumption,
and rerun it, at which point it succeeded.

And you are done :)

You can now move onwards to for instance crudifying your Babelfish or Sakila database if you wish.

### Licensing Magic

2 days after you install Magic on your cloud, _Magic will stop working_ unless you have
a valid license for Magic. To obtain a valid license click the navbar button in Magic
in the top/left corner, and select the _"Configuration"_ menu item. Choose the _"License"_
tab, and paste in your license key in the textarea at the middle of the screen. Click _"Apply"_
and you're fully licensed.

If you don't have a valid license key for Magic, you can click the _"obtain a valid license"_
hyperlink, that will allow you to purchase one.

![Getting licensed](https://servergardens.files.wordpress.com/2021/02/magic-license.png)

# Support

If you have a support request of private nature, or a license inquiry, you can send us
email at [post@servergardens.com](mailto:post@servergardens.com). If you want to submit a
feature request or a bug report, you can do such through the project's
[GitHub Issues](https://github.com/polterguy/magic/issues).
Magic comes with professional support for Enterprise Licensed customers. Contact us for more
information about how to obtain an Enterprise License.

* [post@servergardens.com](mailto:post@servergardens.com)

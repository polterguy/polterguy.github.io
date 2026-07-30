---
title: Getting Started
description: This article is about how to get started with Magic Cloud using Docker, and start leveraging its Low-Code and No-Code features in your own systems
header:
  image: /assets/images/hero/getting-started.png
  og_image: /assets/images/hero/getting-started-og.png
  image_description: Getting started with Magic
---

The easiest way to get started with Magic is to [signup for a cloudlet at AINIRO.IO](https://ainiro.io/buy). However, if you want to run it locally you can use either Docker or the source code. The easiest way to get started is to use Docker.

## Using Docker

The fastest way to run Magic locally is with [Docker](https://www.docker.com/). Once Docker is installed, paste the command below into your terminal — it pulls a ready-made `docker-compose` file and starts both containers for you.

<div class="hl-terminal" markdown="0">
  <div class="hl-terminal-bar">
    <span class="hl-dot hl-dot-red"></span>
    <span class="hl-dot hl-dot-yellow"></span>
    <span class="hl-dot hl-dot-green"></span>
    <button class="hl-copy" type="button" onclick="hlCopyCmd(this)">Copy</button>
    <span class="hl-terminal-label">terminal</span>
  </div>
  <div class="hl-terminal-body"><code id="hl-cmd">curl -fsSL https://hyperlambda.dev/docker-compose.yaml | docker compose -f - up</code></div>
</div>

<script>
function hlCopyCmd(btn){
  var cmd = document.getElementById('hl-cmd').textContent;
  navigator.clipboard.writeText(cmd).then(function(){
    var label = btn.textContent;
    btn.textContent = 'Copied!';
    btn.classList.add('hl-copied');
    setTimeout(function(){ btn.textContent = label; btn.classList.remove('hl-copied'); }, 1600);
  });
}
</script>

<style>
.hl-terminal{
  margin:1.6em 0;
  border:1px solid rgba(216,185,138,.25);
  border-radius:12px;
  background:#1c140c;
  overflow:hidden;
  box-shadow:0 10px 30px rgba(0,0,0,.45);
  font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace;
}
.hl-terminal-bar{
  display:flex;align-items:center;gap:.55em;
  padding:.7em .9em;
  background:#241a10;
  border-bottom:1px solid rgba(216,185,138,.15);
}
.hl-dot{width:12px;height:12px;border-radius:50%;display:inline-block;flex:0 0 auto;}
.hl-dot-red{background:#ff5f57;}
.hl-dot-yellow{background:#febc2e;}
.hl-dot-green{background:#28c840;}
.hl-copy{
  margin-left:.45em;
  border:1px solid rgba(216,185,138,.35);
  background:transparent;color:#ece6da;
  font-family:inherit;font-size:.78em;font-weight:600;
  padding:.28em .85em;border-radius:999px;cursor:pointer;
  transition:background .15s,border-color .15s,color .15s;
}
.hl-copy:hover{background:rgba(216,185,138,.16);border-color:#d8b98a;}
.hl-copy.hl-copied{background:#d8b98a;border-color:#d8b98a;color:#17110b;}
.hl-terminal-label{margin-left:auto;color:#8a7f70;font-size:.8em;letter-spacing:.02em;}
.hl-terminal-body{
  padding:1em 1.1em;
  overflow-x:auto;
  color:#ece6da;font-size:.92em;line-height:1.6;
  white-space:pre;
}
.hl-terminal-body::before{content:"$ ";color:#d8b98a;font-weight:700;}
.hl-terminal-body code{background:none;border:none;color:inherit;padding:0;font-size:inherit;font-family:inherit;}
</style>

This spins up the frontend at port 5555 and the backend at port 4444, and creates volumes for all the folders whose files you typically change as you use Magic. The _"/misc/"_ and _"/system/"_ folders deliberately have no volumes, since those are meant to be replaced when you update your image.

Once your containers are up and running, navigate your browser to `localhost:5555`, and login to your backend at `localhost:4444`, using _"root"_ as both the username and password. Once you've logged in, you'll be asked to setup Magic. This will resemble the following.

![Screenshot of how to initially configure Magic](/images/setup-magic.jpeg)

After you've provided a root password, your name, and your email address, you will be redirected to the main dashboard and you can start using Magic.

## Using the source code version

Clone [the Magic repository](https://github.com/polterguy/magic){:target="_blank"}, make sure you've got .Net version 10 installed and the latest version of NodeJS, and enter the _"backend"_ and _"frontend"_ folders with two terminal windows, and execute the following commands in the respective terminals.

1. `dotnet run`
2. `npm install && npm run dev`

After some few minutes you should be able to access the dashboard from `localhost:4201`, and login to your cloudlet using `http://localhost:5000` as your backend URL. The initial username and password combination is the same; _"root"_ and _"root"_.

## Deploy to production

If you want to deploy Magic to production we have created a detailed description [here](/deploy/). To deploy Magic requires a lot of technical knowledge, and to maintain it requires knowledge about security, CDNs, etc - However, we're here to [help you for a fee](https://ainiro.io/contact-us) if needed.

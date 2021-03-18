
Once your site is finished (or finished "enough" to start public testing) you're going to need to host it somewhere more public and accessible than your personal development computer.


Before you can host a website externally you're first going to have to:
    Make a few changes to your project settings.
    Choose an environment for hosting the Django app.
    Choose an environment for hosting any static files.
    Set up a production-level infrastructure for serving your website.


## What is a production environment?

The production environment is the environment provided by the server computer where you will run your website for external consumption. 

The environment includes:
    Computer hardware on which the website runs.
    Operating system (e.g. Linux, Windows).
    Programming language runtime and framework libraries on top of which your website is written.
    Web server used to serve pages and other content (e.g. Nginx, Apache).
    Application server that passes "dynamic" requests between your Django website and the webserver.
    Databases on which your website is dependent.

    Note: Depending on how your production is configured you might also have a reverse proxy, load balancer, etc.


The server computer could be located on your premises and connected to the Internet by a fast link, but it is far more common to use a computer that is hosted "in the cloud". 
The remote server will usually offer some guaranteed level of computing resources (e.g. CPU, RAM, storage memory, etc.) and Internet connectivity for a certain price.


This sort of remotely accessible computing/networking hardware is referred to as Infrastructure as a Service (IaaS). Many IaaS vendors provide options to preinstall a particular operating system, onto which you must install the other components of your production environment. Other vendors allow you to select more fully-featured environments, perhaps including a complete Django and web-server setup.


Note: Pre-built environments can make setting up your website very easy because they reduce the configuration, but the available options may limit you to an unfamiliar server (or other components) and may be based on an older version of the OS. Often it is better to install components yourself, so that you get the ones that you want, and when you need to upgrade parts of the system, you have some idea of where to start!


Other hosting providers support Django as part of a Platform as a Service (PaaS) offering. In this sort of hosting you don't need to worry about most of your production environment (web server, application server, load balancers) as the host platform takes care of those for you (along with most of what you need to do in order to scale your application). That makes deployment quite easy, because you just need to concentrate on your web application and not all the other server infrastructure.


## Choosing a hosting provider:
There are well over 100 hosting providers that are known to either actively support or work well with Django (you can find a fairly exhaustive list at DjangoFriendly hosts). These vendors provide different types of environments (IaaS, PaaS), and different levels of computing and network resources at different prices.

Some of the things to consider when choosing a host:
    How busy your site is likely to be and the cost of data and computing resources required to meet that demand.
    Level of support for scaling horizontally (adding more machines) and vertically (upgrading to more powerful machines) and the costs of doing so.
    Where the supplier has data centres, and hence where access is likely to be fastest.
    The host's historical uptime and downtime performance.
    Tools provided for managing the site — are they easy to use and are they secure (e.g. SFTP vs FTP).
    Inbuilt frameworks for monitoring your server.
    Known limitations. Some hosts will deliberately block certain services (e.g. email). Others offer only a certain number of hours of "live time" in some price tiers, or only offer a small amount of storage.
    Additional benefits. Some providers will offer free domain names and support for SSL certificates that you would otherwise have to pay for.
    Whether the "free" tier you're relying on expires over time, and whether the cost of migrating to a more expensive tier means you would have been better off using some other service in the first place!


## Getting your website ready to publish

The Django skeleton website created using the django-admin and manage.py tools are configured to make development easier. Many of the Django project settings (specified in settings.py) should be different for production, either for security or performance reasons.
Tip

It is common to have a separate settings.py file for production, and to import sensitive settings from a separate file or an environment variable. This file should then be protected, even if the rest of the source code is available on a public repository.

The critical settings that you must check are:
    DEBUG. This should be set as False in production (DEBUG = False). This stops the sensitive/confidential debug trace and variable information from being displayed.
    SECRET_KEY. This is a large random value used for CSRF protection etc. It is important that the key used in production is not in source control or accessible outside the production server. The Django documents suggest that this might best be loaded from an environment variable or read from a server-only file. 


## Why Heroku?

Heroku is one of the longest running and popular cloud-based PaaS services. It originally supported only Ruby apps, but now can be used to host apps from many programming environments, including Django!

We are choosing to use Heroku for several reasons:
    Heroku has a free tier that is really free (albeit with some limitations).
    As a PaaS, Heroku takes care of a lot of the web infrastructure for us. This makes it much easier to get started, because you don't worry about servers, load balancers, reverse proxies, or any of the other web infrastructure that Heroku provides for us under the hood.
    While it does have some limitations these will not affect this particular application. For example:
        Heroku provides only short-lived storage so user-uploaded files cannot safely be stored on Heroku itself.
        The free tier will sleep an inactive web app if there are no requests within a half hour period. The site may then take several seconds to respond when it is woken up.
        The free tier limits the time that your site is running to a certain amount of hours every month (not including the time that the site is "asleep"). This is fine for a low use/demonstration site, but will not be suitable if 100% uptime is required.
        Other limitations are listed in Limits (Heroku docs).
    Mostly it just works, and if you end up loving it, scaling your app is very easy.

While Heroku is perfect for hosting this demonstration it may not be perfect for your real website. Heroku makes things easy to set up and scale, at the cost of being less flexible, and potentially a lot more expensive once you get out of the free tier.


## this notes are not completed yet 
revisite the the website



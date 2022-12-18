# GEDServer
Server for gamification of evacuation drills.

This project is not complete, and for it to be useful in the GED project it needs further development. However, it has all the basic functions.

#### Front-end features
* Login system
* Managment screen for adding and removing sessions
* Able to download all the data for a session
* Send POST requests to server to store location data

## Installation
It is highly reccommended that you learn the basics of Docker and Docker Compose. I recommend reading and following along with the excelent [guide by Michael Herman](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) of which this project is based on.

This project also assumes you are running on Linux, if you are running on another platform you may need to adjust the installation process to use equivalent commands.

### Running the development build
To start the server, run `docker compose --file docker-compose.yml up --build --detach` inside the project directory. This will require an internet connection as the dependencies need to be downloaded.

The server can now be accessed on [localhost:8000](http://localhost:8000), see the usage section for further instruction.

To stop the server use `docker compose --file docker-compose.yml down -v`, or alternatively without the `-v` argument to preserve database data.

To view logs for debuging, use `docker compose --file docker-compose.yml logs -f`

If you change the variables in `.env.dev`, then make sure the corresponding `environment` lines in `docker-compose.yml` also change. If you are setting up the server so that others have access to it, use the production build as the development build is unsafe for such a task. 


### Running the production build
**Make sure** that you change the passwords in `.env.prod` and `.env.prod.db` as those are just *example files*. You may also need to change `DJANGO_ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` to include the server's own public domain/ip (full scheme for `CSRF_TRUSTED_ORIGINS`, can be found in settings.py), if you want others to be able to access the site. 

The server is set up by default to respond on [localhost:8000](http://localhost:8000), however you may reconfigure this as you please.


All the previous commands stay the same, except replace `docker-compose.yml` with `docker-compose.prod.yml`

## Usage
Once the server is up and running, you need to make an account to be able to make sessions in the server. Use `docker compose --file [DEV OR PRODUCTION FILE] exec web ./manage.py create_session_user [USERNAME] [PASSWORD]` to do this. Be aware that if you did this previously and then shut down the server with the `-v` flag, you will have to do this step again. You can make as many accounts as you need, but they have no permission differences and will be able to see all the same sessions as everyone else.

Once the account is created, browse to `[IP][PORT]/profile/` and log in using the details you provided. You should be directed to the session management screen, where there is a text box and a submit button to add a new session. This will add a new listing and you'll be able to see the session's key, download its data, and delete it. This key is needed when you want to send location data to the server.

### Storing location data in a session
Send POST requests to `[IP][PORT]/locdata/` using the same format oulined in `posttest.sh`. You can also send them via the browser at the same address as long as you follow the formatting rules. You can check that the server has received the data by downloading the data at the profile page.


## Other useful commands
If you want to inspect the structure of the database manually, you can attatch to a psql shell while the server is running with `docker compose --file docker-compose.yml exec db psql --username=django_user --dbname=django_dev` for example.

Another useful ability is to attatch to a live python shell, also useful for inspecting the database. You can do this with `docker compose --file docker-compose.yml exec web ./manage.py shell`

If you are unsure whether the server is running or not, use `docker compose ps -a`




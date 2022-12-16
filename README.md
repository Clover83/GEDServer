# GEDServer
Server for gamification of evacuation drills.

This project is not complete, and for it to be useful in the GED project it needs further development. However, it has a functional web form system for adding datapoints to the database, provided that you initialize the database manually first. The big thing missing is an admin web interface to add thesee database entries more easily.

## Installation
It is highly reccommended that you learn the basics of Docker and Docker Compose, as well as the other software used in the project. I recommend reading and following along with the excelent [guide by Michael Herman](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) of which this project is based on.

This project also assumes you are running on Linux, if you are running on another platform you may need to adjust the installation process to use equivalent commands.

### Running the development build
To start the server, run `docker compose --file docker-compose.yml up --build --detach` inside the project directory.

The server can now be accessed on [localhost:8000](http://localhost:8000), send the post requests to [localhost:8000/locdata](http://localhost:8000/locdata). You can run `posttest.sh` to see server response. Be aware when implementing your own requests that you need to take the CSRF cookie into account.

To stop the server use `docker compose --file docker-compose.yml down -v`, or alternatively without the `-v` argument to preserve database data.

To view logs for debuging, use `docker compose --file docker-compose.yml logs -f`

If you change the variables in `.env.dev`, then make sure the corresponding `environment` lines in `docker-compose.yml` also change.


### Running the production build
**Make sure** that you change the passwords in `.env.prod` and `.env.prod.db` as those are just *example files*. You may also need to change `DJANGO_ALLOWED_HOSTS` to include the server's own public domain/ip, if you want others to be able to access the site. 

The server is set up by default to respond on [localhost:1337](http://localhost:1337), however you may reconfigure this as you please.


All the previous commands stay the same, except replace `docker-compose.yml` with `docker-compose.prod.yml`

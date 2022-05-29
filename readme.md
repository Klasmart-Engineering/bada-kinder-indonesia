# Bada Kinder Indonesia #

This project is built with django and strapi.

## What is this repository for? ##

* This repository is bada kinder with local flavor of Indonesia's team.


## How do I get set up? ##

### Before you begin ###
Follow these steps to install the necessary tools:

* Install Docker Community Edition (CE) on your workstation. Depending on the OS, you may need to configure your Docker instance to use 4.00 GB of memory for all containers to run properly. Please refer to the Resources section if using Docker for Windows or Docker for Mac for more information.

* Install Docker Compose v1.29.1 and newer on your workstation.

* Node JS LTS version.

* Older versions of docker-compose do not support all the features required by docker-compose.yaml file, so double check that your version meets the minimum version requirements.

### Configuration ###
* Clone this repo.
* Set values for `.env` file and `bada-kinder-cms/.env` (Ask Indonesian Tech Team for both `.env` values).
* Go to the root dir of this project.
* Run: `docker-compose build` for initial start.
* Run: `docker-compose up`.
* Run: `docker ps` to make sure all container is ready.
* Also if you want to start the dockers in the next time (after shutdown your pc) run `docker-compose up`
* Open second terminal.
* Change directory to `bada-kinder-cms`.
* Run: `yarn`.
* Run: `yarn develop`.

### Dependencies ###
* django
* strapi
* postgres

## Who do I talk to? ##

* Indonesian Tech Team
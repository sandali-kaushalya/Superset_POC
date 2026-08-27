# MSc Thesis — BI Tool Evaluation & Proof of Concept

<p align="center">
  <strong>Evaluation of Modern Business Intelligence Tools for Reporting</strong><br>
  Master's Thesis 
</p>

<p align="center">
  <a href="https://github.com/sandali-kaushalya/MSC_Thesis">
    <img src="https://img.shields.io/badge/Repository-GitHub-black?logo=github" alt="GitHub Repository">
  </a>
  <img src="https://img.shields.io/badge/Metabase-Evaluation-blue" alt="Metabase">
  <img src="https://img.shields.io/badge/Apache%20Superset-Evaluation-orange" alt="Apache Superset">
  <img src="https://img.shields.io/badge/MariaDB-Database-blue" alt="MariaDB">
  <img src="https://img.shields.io/badge/Docker-Deployment-2496ED?logo=docker" alt="Docker">
</p>

---
## 📖 Overview

This repository contains the materials developed for a Master's thesis investigating the suitability of modern **Business Intelligence (BI) tools** as an alternative or addition to the existing **JasperReports Server** reporting environment.

The study focuses on improving reporting through interactive dashboards, self-service data exploration, visualisations, and flexible reporting capabilities while continuing to use the existing database environment.

---
# Apache Superset Docker Setup

This repository contains the Docker-based setup used to run **Apache Superset** for the thesis project.

## Requirements

Install:

* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* [Git](https://git-scm.com/downloads)

Make sure Docker Desktop is running before starting Superset.

## Project Structure

```text
superset/
├── docker-compose.yml
├── Dockerfile
├── superset_config.py
├── docker/
├── superset/
├── superset-frontend/
├── README.md
└── ...
```

> The exact files may differ depending on the Superset version and customizations in this project.

## 1. Clone the Repository

```bash
git clone https://github.com/sandali-kaushalya/MSC_Thesis.git
cd MSC_Thesis
```

## 2. Start Superset

If the repository contains a `docker-compose.yml` file, start the services with:

```bash
docker compose up -d
```

Check the running containers:

```bash
docker ps
```

The setup should include services such as:

* `superset_app`
* `superset_worker`
* `superset_worker_beat`
* `superset_db`
* `superset_cache`

## 3. Open Superset

After the containers have started, open:

[http://localhost:8088](http://localhost:8088)

The Superset web interface should appear.

## 4. Check Container Status

Run:

```bash
docker compose ps
```

You can also check all Docker containers:

```bash
docker ps -a
```

## 5. View Superset Logs

To view the application logs:

```bash
docker logs superset_app
```

To follow the logs:

```bash
docker logs -f superset_app
```

For the Celery worker:

```bash
docker logs superset_worker
```

For the Celery beat service:

```bash
docker logs superset_worker_beat
```

## 6. Stop Superset

To stop the services without deleting them:

```bash
docker compose stop
```

To start them again:

```bash
docker compose start
```

## 7. Shut Down the Environment

To stop and remove the containers:

```bash
docker compose down
```

> `docker compose down` normally removes the containers and network but does not remove named volumes unless `-v` is specified.

**Do not use `docker compose down -v` unless you intentionally want to remove the persistent database volumes.**

## 8. Database

This setup uses PostgreSQL for the Superset application metadata database.

The database service is:

```text
superset_db
```

The database stores Superset metadata such as:

* Users
* Dashboards
* Charts
* Datasets
* Saved queries
* Database connections
* Superset configuration

Do not commit database passwords, credentials, or private database backups to a public GitHub repository.

## 9. Redis

Redis is used by Superset for asynchronous tasks and caching.

The Redis service is:

```text
superset_cache
```

Check Redis with:

```bash
docker logs superset_cache
```

## 10. MariaDB / Thesis Data Warehouse

If the project uses the separate MariaDB container for the thesis data warehouse, the container may be:

```text
saga-dw
```

The container exposes MariaDB through:

```text
localhost:3355
```

The Superset application can use this database as a data source.

**Do not publish database passwords or sensitive thesis data in this repository.**

## 11. Metabase

If Metabase is also part of the thesis environment, it runs separately from Superset.

The Metabase service may be available at:

[http://localhost:3000](http://localhost:3000)

Start the existing Metabase container with:

```bash
docker start metabase
```

Check it with:

```bash
docker ps
```

## 12. Restart Superset

If a container needs to be restarted:

```bash
docker compose restart
```

To restart only the application:

```bash
docker compose restart superset_app
```

## 13. Rebuild After Configuration Changes

If you modify the Dockerfile or other image configuration:

```bash
docker compose down
docker compose build
docker compose up -d
```

## 14. Troubleshooting

### Superset is not available on port 8088

Check whether the application is running:

```bash
docker ps
```

Check the logs:

```bash
docker logs superset_app --tail 100
```

### Worker keeps restarting

Check:

```bash
docker logs superset_worker --tail 100
```

For the beat service:

```bash
docker logs superset_worker_beat --tail 100
```

### Check all services

```bash
docker compose ps
```

### Check Docker resources

```bash
docker system df
```

## 15. Updating the GitHub Repository

After making changes:

```bash
git add .
git commit -m "Update Superset setup"
git push
```

Repository:

[MSC_Thesis](https://github.com/sandali-kaushalya/MSC_Thesis)

## Important Security Notes

Before making the repository public, make sure it does **not** contain:

```text
.env
database passwords
API keys
access tokens
secret keys
private certificates
database dumps
private customer/user data
```

Use a `.env.example` file to document required environment variables without publishing their actual values.

Example:

```text
DATABASE_USER=your_username
DATABASE_PASSWORD=your_password
DATABASE_HOST=your_database_host
DATABASE_NAME=your_database
```

Never commit the real password or secret key.

## Environment

This project was developed using Docker and Apache Superset. The exact behavior may depend on the Docker image, Superset version, configuration files, and database environment included with the project.

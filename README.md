 CloudReady — Dockerized Cloud Monitoring App

 ## About the Project

CloudReady is a beginner-level cloud computing project built using Python, Flask, and Docker. It provides a simple web application with a health-check endpoint to check whether the application is responding.

## Technologies Used

* Python
* Flask
* Docker
* GitHub

## Features

* Displays project information through a web endpoint.
* Provides a health-check endpoint.
* Runs inside a Docker container.
* Uses a Dockerfile to build the Docker image.

## Project Structure

```text
Cloudready/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Run Locally

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

Open http://localhost:5000 in your browser.

## Run with Docker

Build the Docker image:

```bash
docker build -t cloudready .
```

Run the container:

```bash
docker run -d -p 5000:5000 --name cloudready-container cloudready
```

Open http://localhost:5000 to view the application.

For the health check, visit http://localhost:5000/health.

Expected health-check response:

```json
{
  "status": "OK"
}
```

## What I Learned

* Building a Python web application using Flask.
* Creating Docker images and running containers.
* Testing application endpoints.
* Uploading source code to GitHub.

## Current Status

The application has been built and tested locally using Docker. Deployment to AWS or another cloud platform has not yet been completed.

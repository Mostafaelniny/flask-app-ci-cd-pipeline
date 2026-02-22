



#  Flask App CI/CD Pipeline

This repository demonstrates how to build a **CI/CD pipeline** for a Dockerized Python Flask application using **Jenkins** running inside a container.

Whenever you push code to GitHub, Jenkins will:
1. Pull the latest code  
2. Build a Docker image  
3. Push the image to Docker Hub  
4. Deploy the latest container

This project simulates a real-world DevOps workflow with automated CI/CD. :contentReference[oaicite:1]{index=1}

![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?logo=linux)
![Git](https://img.shields.io/badge/Git-VersionControl-orange?logo=git)

---

##  Table of Contents

1. [About the Project](#about-the-project)  
2. [Project Architecture](#project-architecture)  
3. [Prerequisites](#prerequisites)  
4. [Installation & Setup](#installation--setup)  
5. [CI/CD Pipeline Overview](#cicd-pipeline-overview)  
6. [Usage](#usage)  
7. [Screenshots](#screenshots)  
8. [Future Improvement Ideas](#future-improvement-ideas)  
9. [Author](#author)

---

##  About the Project

This project contains:
- A simple **Flask web application**  
- A **Dockerfile** to containerize the app  
- A **Jenkinsfile** that defines a CI/CD pipeline  
- Integration with **Docker Hub** for image storage  
- Automated build and deployment on code push

It’s a practical example of how CI/CD pipelines work in real DevOps environments. :contentReference[oaicite:2]{index=2}

---

##  Project Architecture

- GitHub (Code)     ↓ (Push)
- Jenkins (CI/CD Pipeline in Docker Container)    ↓
- Docker Build → Image          ↓
- Docker Hub (Registry)         ↓
- Deployment (Run Container)

---

##  Prerequisites

Before you begin, ensure you have the following installed:

✔ Docker  
✔ Docker Compose  
✔ Jenkins (in container)  
✔ Docker Hub account  
✔ Git & GitHub account  

---

##  Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Mostafaelniny/flask-app-ci-cd-pipeline.git
cd flask-app-ci-cd-pipeline
```

### 2. Build the Flask Docker Image
```bash 
docker build -t yourdockerhubusername/flask-app
```

### 3. Run the container locally
```bash
docker run -d -p 5000:5000 yourdockerhubusername/flask-app
```
**Visit:** `http://localhost:5000` to verify.

### 4.



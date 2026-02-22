



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
5. [Pipeline Configuration (Start the Build)](#pipeline-configuration-start-the-build)
6. [Screenshots](#screenshots)  
7. [Future Improvement Ideas](#future-improvement-ideas)  
8. [Author](#author)
9. [Repository Links](#repository-links)

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

### 4. Run Jenkins using the docker-compose.yml file 
```bash
docker-compose up -d
```
- **Verify Jenkins is Running**    `docker ls`
- **Access Jenkins**               `http://localhost:8080`
- **Get Initial Admin Password**   `docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword`


---
##  Pipeline Configuration (Start the Build)

 
### 1)Install Required Plugins
Go to:

Manage Jenkins → Manage Plugins → Install:

- Git
- Pipeline
- Docker Pipeline
- Credentials Binding

**Restart Jenkins after installation.**





### 2)Configure Docker Hub Credentials

Configure Docker Hub Credentials

Go to:

Manage Jenkins → Credentials → Global → Add Credentials

Add:
- Kind: Username with password
- ID: dockerhub-creds
- Username: Your Docker Hub username
- Password: Your Docker Hub password

**and add another one for Git Credentials**




### 3)Create Pipeline Job
1. Click New Item
2. Select Pipeline
3. Choose:  `Pipeline script from SCM`
4. Configure:
- SCM: Git
- Repository URL:  `https://github.com/Mostafaelniny/flask-app-ci-cd-pipeline.git` 
- Branch: main
- Script Path: Jenkinsfile
  
**Save.**




### 4)Start the Build
- Click  `Build Now`
- Monitor progress in: `Build → Console Output`
- A successful build will show:  `Successfully built
                                  Successfully pushed
                                  Finished: SUCCESS`


---
## Screenshots


---

## Future Improvement Ideas

- ✔ Add automated tests (PyTest)
- ✔ Use multi-stage Dockerfile for smaller image
- ✔ Deploy to cloud (AWS / Azure / GCP)
- ✔ Add monitoring & alerts

---

## Author

Mostafa Elniny – DevOps Engineer in the making

---

## Repository Links 





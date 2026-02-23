
#  Flask App CI/CD Pipeline

This repository demonstrates how to build a **CI/CD pipeline** for a Dockerized Python Flask application using **Jenkins** running inside a container.

Whenever you push code to GitHub, Jenkins will:
1. Pull the latest code  
2. Build a Docker image  
3. Push the image to Docker Hub  
4. Deploy the latest container

This project simulates a real-world DevOps workflow with automated CI/CD.

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
   - [1️⃣ Install Required Plugins](#1️⃣-install-required-plugins)
   - [2️⃣ Configure Credentials](#2️⃣-configure-credentials)
   - [3️⃣ Create Pipeline Job](#3️⃣-create-pipeline-job)
   - [4️⃣ Enable Webhook Trigger](#4️⃣-enable-webhook-trigger)
   - [5️⃣ Create GitHub Webhook](#5️⃣-create-github-webhook)
   - [6️⃣ Start the Build](#6️⃣-start-the-build)
7. [🔒 Security Note](#-security-note)
8. [Screenshots](#screenshots)  
9. [Future Improvement Ideas](#future-improvement-ideas)  
10. [Author](#author)
11. [Repository Links](#repository-links)

---

##  About the Project

This project contains:
- A simple **Flask web application**  
- A **Dockerfile** to containerize the app  
- A **Jenkinsfile** that defines a CI/CD pipeline  
- Integration with **Docker Hub** for image storage  
- Automated build and deployment on code push

It’s a practical example of how CI/CD pipelines work in real DevOps environments. 

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

 
### 1️⃣ Install Required Plugins
Go to:

Manage Jenkins → Manage Plugins → Install:

- Git
- Pipeline
- Docker Pipeline
- Credentials Binding

**Restart Jenkins after installation.**





### 2️⃣ Configure Credentials

Configure Docker Hub Credentials

Go to:

`Manage Jenkins → Credentials → Global → Add Credentials`

Add:
- **Kind:** Username with password
- **ID:** dockerhub-creds
- **Username:** Your Docker Hub username
- **Password:** Your Docker Hub password

**and add another one for Git Credentials**




### 3️⃣ Create Pipeline Job
1. Click `New Item.`
2. Select `Pipelin.e`
3. Choose:  `Pipeline script from SCM.`
4. Configure:
      - SCM: `Git`
      - Repository URL:  `https://github.com/Mostafaelniny/flask-app-ci-cd-pipeline.git` 
      - Branch: `main`
      - Script Path: `Jenkinsfile`
  
**Save.**



### 4️⃣ Enable Webhook Trigger
In the Pipeline configuration **Build Triggers**, check: `☑ GitHub hook trigger for GITScm polling`
This allows GitHub push events to trigger builds automatically.



### 5️⃣ Create GitHub Webhook
In your GitHub repository:
- Go to `**Settings → Webhooks → Add webhook**`
- **Payload URL:**   `http://<PUBLIC_URL>/github-webhook/`

⚠️ If Jenkins runs locally (e.g., `localhost:8080`), GitHub cannot reach it directly.
To expose Jenkins publicly during development, you can use **ngrok**: ```bash ngrok http 8080 ```
Copy the Forwarding URL (e.g., https://xxxxx.ngrok.io) and use it in the webhook URL.
- **Now every time you push to GitHub, the Jenkins Pipeline will start automatically.**



### 6️⃣ Start the Build
- Click  `Build Now`
- Monitor progress in: `Build → Console Output.`
- A successful build will show:  `Successfully built
                                  Successfully pushed
                                  Finished: SUCCESS`

---

## 🔒 Security Note

For security purposes, only the necessary ports are opened on the host firewall.

By default, **UFW (Uncomplicated Firewall)** blocks all incoming connections except SSH.

The following ports were explicitly allowed:

- **5000/tcp** — Used by the Flask application  
- **8080/tcp** — Used by Jenkins  

All other ports remain blocked to prevent unauthorized external access.

### Commands Used

```bash
sudo ufw allow 5000/tcp   # Flask application
sudo ufw allow 8080/tcp   # Jenkins
sudo ufw status
```


---
## Screenshots

1️⃣ Project Structure

<img width="275" height="193" alt="image" src="https://github.com/user-attachments/assets/2d6d2fd6-baf7-4b9b-b77a-63547b08bd7c" />

---

2️⃣ Application Architecture

<img width="532" height="192" alt="image" src="https://github.com/user-attachments/assets/7f9ff35b-1ce3-4185-9b54-9f432d4cd30e" />

---

3️⃣ Docker Image Build

<img width="852" height="482" alt="2" src="https://github.com/user-attachments/assets/3db53363-1f13-452a-b391-fd499569114b" />

---

4️⃣ Application Container Running

<img width="1796" height="297" alt="3" src="https://github.com/user-attachments/assets/f2610e2e-728c-477d-83a3-eadd16cd7bc4" />

---

5️⃣ Jenkins Container Running (via Docker Compose)

<img width="1086" height="488" alt="Screenshot 2026-02-16 153931" src="https://github.com/user-attachments/assets/9ac2b422-cd45-40ff-a3dc-9e48ecf53d60" />

---

6️⃣ Jenkins Pipeline Running

<img width="1893" height="826" alt="Jenkins_running_Dashbord" src="https://github.com/user-attachments/assets/e6fc9050-bae6-4c63-9480-b516009d8ac4" />

---

7️⃣ Successful Pipeline Execution

<img width="327" height="321" alt="building" src="https://github.com/user-attachments/assets/b4d89d77-0849-44fb-8ea9-eae70c4ec896" />

---

8️⃣ Docker Hub Image Pushed

<img width="893" height="822" alt="hubdocker" src="https://github.com/user-attachments/assets/0967eddf-812b-4bb9-b582-c88f7e4bfd8c" />

---


---

## Future Improvement Ideas

- ✔ Add automated tests (PyTest)
- ✔ Use multi-stage Dockerfile for smaller image
- ✔ Deploy to cloud (AWS / Azure / GCP)
- ✔ Add monitoring & alerts

---

## Feedback
If you have any feedback, please reach out to us at mostafammdouh68@gmail.com

---

## Author

Mostafa Elniny – DevOps Engineer in the making

---

## Repository Links 

- 💼 LinkedIn: [Mostafa Elniny](http://www.linkedin.com/in/mostafa-mmdouh-elniny-4k)
- 🐳 Docker Hub: [mostafaelniny](https://hub.docker.com/r/mostafaelniny)






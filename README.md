# Linear Regression ML model DevOps Project – ML CI/CD Cloud Deployment 🚀

## Project Overview

This project demonstrates a complete DevOps workflow for deploying a Machine Learning application using Docker, GitHub Actions CI/CD, DockerHub, Flask, and AWS EC2 cloud infrastructure.

The application trains a **Linear Regression model using Python** and predicts values based on input data. The ML application is converted into a web application using Flask, containerized using Docker, and automatically deployed to an AWS EC2 cloud server through a CI/CD pipeline.

---

# Technologies Used

- Python
- Flask
- Scikit-learn
- NumPy
- Pytest
- Docker
- Git & GitHub
- GitHub Actions (CI/CD)
- DockerHub (Container Registry)
- AWS EC2 (Cloud Deployment)

---

# Project Structure

```text
lr-devops-project
│
├── app.py                     # Flask + Linear Regression application
├── test_model.py              # Pytest testcases
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker container configuration
├── README.md                  # Project documentation
├── .gitignore                 # Ignore sensitive files
│
└── .github
    └── workflows
        └── docker-ci.yml      # CI/CD pipeline configuration
```

---

# Machine Learning Application

The project uses a simple **Linear Regression model** implemented using **scikit-learn**.

Example dataset:

```python
X = [[1],[2],[3],[4],[5]]
y = [2,4,6,8,10]
```

The model predicts output values for new inputs.

Example prediction:

```text
Prediction: 12.0
```

The application is served through a Flask web server and exposed through port `5000`.

---

# Flask Web Application

The ML model is integrated with Flask to create a browser-accessible web application.

Run locally:

```bash
python app.py
```

Access application:

```text
http://localhost:5000
```

Example browser output:

```text
Prediction from Linear Regression Model: 12.0
```

---

# Docker Containerization

The application is packaged inside a Docker container to ensure consistent execution across environments.

## Build Docker Image

```bash
docker build -t lr-devops-app .
```

## Run Docker Container

```bash
docker run -p 5000:5000 lr-devops-app
```

## Access Application

```text
http://localhost:5000
```

Docker ensures portability, isolation, and reproducible deployments.

---

# Continuous Integration & Continuous Deployment (CI/CD)

GitHub Actions automates the entire DevOps workflow.

Pipeline stages:

1. Push code to GitHub
2. Install Python dependencies
3. Run test cases using pytest
4. Build Docker image
5. Push Docker image to DockerHub
6. Connect to AWS EC2 using SSH
7. Pull latest Docker image
8. Deploy container automatically

---

# GitHub Actions Workflow

The CI/CD pipeline is configured inside:

```text
.github/workflows/docker-ci.yml
```

The workflow automatically triggers whenever code is pushed to the `main` branch.

---

# DockerHub Container Registry

Docker images are stored in DockerHub.

Example:

```bash
docker push <dockerhub-username>/lr-devops-app
```

AWS EC2 pulls the latest image from DockerHub during deployment.

---

# AWS EC2 Cloud Deployment

The application is deployed on an Ubuntu-based AWS EC2 cloud server.

Deployment steps:

1. Create EC2 instance
2. Configure security groups
3. Install Docker on EC2
4. Pull Docker image from DockerHub
5. Run Docker container
6. Access application through public IP

Example EC2 deployment command:

```bash
sudo docker run -d -p 5000:5000 --name lr-devops-app <dockerhub-username>/lr-devops-app
```

Access deployed application:

```text
http://<EC2_PUBLIC_IP>:5000
```

---

# Deployment Architecture

```text
Developer (Windows Laptop)
        │
        │ git push
        ▼
GitHub Repository
        │
        ▼
GitHub Actions CI/CD
        │
        ▼
Run Tests (Pytest)
        │
        ▼
Docker Image Build
        │
        ▼
DockerHub Registry
        │
        ▼
AWS EC2 Cloud Server
        │
        ▼
Docker Container
        │
        ▼
Flask Web Application
        │
        ▼
Linear Regression ML Model
```

---

# Security Practices

Sensitive files are excluded using `.gitignore`.

Ignored files include:

```text
*.pem
__pycache__/
*.pyc
.env
```

Secrets and credentials are securely managed using GitHub Secrets.

Configured secrets:

```text
DOCKER_USERNAME
DOCKER_PASSWORD
EC2_HOST
EC2_USER
EC2_SSH_KEY
```

---

# AWS Security Group Configuration

Inbound rules configured:

| Type       | Port |
|------------|------|
| SSH        | 22   |
| Custom TCP | 5000 |

This allows SSH access and browser access to the Flask application.

---

# Learning Outcomes

This project demonstrates practical understanding of:

- Machine Learning model deployment
- Docker containerization
- Docker image management
- Git and GitHub workflows
- CI/CD automation using GitHub Actions
- DockerHub container registry
- AWS EC2 cloud deployment
- SSH-based remote deployment
- Flask web application deployment
- Cloud networking and port mapping
- Secure secret management

---

# Commands Used

## Build Docker Image

```bash
docker build -t lr-devops-app .
```

## Run Local Container

```bash
docker run -p 5000:5000 lr-devops-app
```

## Push Docker Image

```bash
docker push <dockerhub-username>/lr-devops-app
```

## Connect to AWS EC2

```bash
ssh -i devops-key.pem ubuntu@<EC2_PUBLIC_IP>
```

## Run Container on EC2

```bash
sudo docker run -d -p 5000:5000 --name lr-devops-app <dockerhub-username>/lr-devops-app
```

---

# Future Improvements

- Add Kubernetes deployment
- Implement HTTPS using Nginx
- Deploy using Terraform Infrastructure as Code
- Integrate database support
- Add frontend UI for prediction input

# LR DevOps Project – ML CI/CD Deployment

## Project Overview

This project demonstrates a complete DevOps workflow for deploying a Machine Learning application using Docker, GitHub Actions CI/CD, DockerHub, and AWS EC2 cloud infrastructure.

The application trains a **Linear Regression model using Python** and predicts values based on input data. The application is containerized using Docker and automatically deployed to a cloud server through a CI/CD pipeline.

---

## Technologies Used

* Python
* Scikit-learn
* Docker
* Git & GitHub
* GitHub Actions (CI/CD)
* DockerHub (Container Registry)
* AWS EC2 (Cloud Deployment)

---

## Project Structure

```
lr-devops-project
│
├── app.py                # Linear Regression model code
├── test_model.py         # Pytest test cases
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker container configuration
├── .gitignore            # Ignore sensitive files
│
└── .github/workflows
      └── docker-ci.yml   # CI/CD pipeline configuration
```

---

## Machine Learning Application

The project uses a simple Linear Regression model implemented using **scikit-learn**.

Example dataset:

```
X = [1,2,3,4,5]
y = [2,4,6,8,10]
```

The model predicts output values for new inputs.

Example output:

```
Prediction: 12.0
```

---

## Docker Containerization

The application is packaged inside a Docker container.

### Build Docker Image

```
docker build -t lr-devops-app .
```

### Run Docker Container

```
docker run lr-devops-app
```

Docker ensures the application runs consistently across environments.

---

## CI/CD Pipeline

GitHub Actions automates the entire DevOps workflow.

Pipeline stages:

1. Code push to GitHub
2. Install dependencies
3. Run test cases using pytest
4. Build Docker image
5. Push image to DockerHub
6. Deploy container to AWS EC2

---

## Deployment Architecture

```
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
Docker Image Build
        │
        ▼
DockerHub Registry
        │
        ▼
AWS EC2 Cloud Server
        │
        ▼
Docker Container Running ML Model
```

---

## Security Practices

Sensitive files are excluded using `.gitignore`.

Examples:

```
*.pem
__pycache__/
*.pyc
```

SSH keys and credentials are securely stored using **GitHub Secrets**.

---

## Learning Outcomes

This project demonstrates practical knowledge of:

* Machine Learning deployment
* Containerization using Docker
* CI/CD automation using GitHub Actions
* Secure secret management
* Cloud deployment using AWS EC2

---

## Author

Srinidhi Martha

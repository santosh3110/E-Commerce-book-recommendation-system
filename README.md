
# 📚 E-Commerce Book Recommendation System

## Demo
![alt text](image-2.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [How-to-Run](#how-to-run)
- [Deployment](#deployment)
- [Model-Training](#model-training)
- [Model-Evaluation](#model-evaluation)
- [Model-Deployment](#model-deployment)
- [Future-Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## 🚀 Introduction
This is an end-to-end **Book Recommendation System** built using Python, Pandas, NumPy, and Scikit-learn. The system uses a **Collaborative Filtering** approach to recommend books to users based on their past ratings.

## ✨ Features
- 📚 Book recommendations based on user ratings
- 👥 User-based Collaborative Filtering algorithm
- 🌐 Deployment using Streamlit and Docker
- ☁️ Easy deployment on AWS EC2 instances

## 🛠️ Requirements
- Python 3.11
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Docker

## 🚀 How to Run

### Clone the Repository
```bash
git clone https://github.com/santosh3110/E-Commerce-book-recommendation-system.git
cd E-Commerce-book-recommendation-system
```

### Create a Conda Environment
```bash
conda create -n books python=3.11 -y
conda activate books
```

### Install the Requirements
```bash
pip install -r requirements.txt
```

### Run the Application Locally
```bash
streamlit run app.py
```

Visit `http://localhost:8501` to see the app running!

## ☁️ Deployment

### Deploy on AWS EC2 using Docker

1. **Update and install Docker**:
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

2. **Clone the repository**:
```bash
git clone https://github.com/santosh3110/E-Commerce-book-recommendation-system.git
cd E-Commerce-book-recommendation-system
```

3. **Build the Docker image**:
```bash
docker build -t santosh3110/bookapp:latest .
```

4. **Run the Docker container**:
```bash
docker run -d -p 8501:8501 santosh3110/bookapp
```

5. **Push your Docker image to Docker Hub** (optional):
```bash
docker login
docker push santosh3110/bookapp:latest
```

6. **Optional cleanup commands**:
```bash
docker ps
docker stop <container_id>
docker rm $(docker ps -a -q)
docker rmi santosh3110/bookapp:latest
docker pull santosh3110/bookapp
```

## 🧠 Model Training
The model is trained using **Collaborative Filtering** with the **Nearest Neighbors** algorithm from Scikit-learn to find similar users based on their book ratings.

## 🚀 Model Deployment
The application is deployed using **Streamlit** inside a **Docker container** and can be hosted on **AWS EC2** or any cloud provider.

## 🌟 Future Improvements
- Implement advanced Collaborative Filtering techniques like **Matrix Factorization**.
- Incorporate **metadata features** such as book **genres**, **authors**, etc.
- Improve evaluation with metrics like **Mean Average Precision (MAP)**.

## 🤝 Contributing
Contributions are welcome!  
Feel free to submit a pull request with your improvements, bug fixes, or ideas.

## 📜 License
This project is licensed under the [Apache 2.0](LICENSE).

## 🙏 Acknowledgments
- Deployed using **Streamlit** and **Docker** for easy access.

## 📬 Contact
For any questions or feedback, feel free to reach out:  
**GitHub**: [santosh3110](https://github.com/santosh3110)

> ⭐ Don't forget to star the repo if you find it useful!

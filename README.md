# **End-to-End Sentiment Analysis**

## **Problem**
The goal of this project is to build a robust end-to-end sentiment analysis system. Using natural language processing (NLP) techniques and machine learning models, the system will analyze text data to classify sentiment into categories such as positive, negative. This project integrates data ingestion, preprocessing, model training, and deployment to deliver a production-ready solution.

---

## **Project Structure**

```bash
End-to-End-Sentiment-Analysis/
├── app.py
├── templates/
│   ├── index.html
│   ├── result.html
├── static/
│   ├── styles.css
|
├── main.py
├── data
├── Artifacts
├── requirements.txt
├── README.md
├── Dockerfile
├── experiments
│   ├── experiment.ipynb
│   ├── data_cleaning.ipynb
│   ├── model.ipynb
├── schema_data
│   ├── schema.yaml
├── .gitignore
├── setup.py
├── .github/workflows/aws.yml
├── src
│   ├── __init__.py
│   ├── components
│   │   ├── data_ingestion
│   │   ├── data_validation
│   │   ├── data_transformation
│   │   ├── model_trainer
│   │   ├── cloud
│   ├── utils
│   ├── constants
│   ├── config
│   ├── entity
│   ├── logging
│   ├── pipeline
│   ├── training_pipeline
```

---

## **Workflow**

### **1. Data Pipeline**
- **Data Source**: Import imdb data from Hugging Face datasets. This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. It provide a set of 25,000 highly polar movie reviews.

[Dataset link](https://huggingface.co/datasets/stanfordnlp/imdb) .

- **Steps**:
  1. **Config**: Collect configuration of Data Ingestion, Data Validation, Data Transformation ,Model Trainer
  2. **Artifacts Config** : Storing Output data path of  Data Ingestion, Data Validation, Data Transformation ,Model Trainer
  3. **Data Ingestion**: Collect and split the data into training, validation, and testing sets.
  4. **Data Validation**: Verify data schema and check for missing columns and Data distribution.
  5. **Data Transformation**: Preprocess text data, including tokenization, stemming, and stop-word removal.

### **2. Model Training**
- Train machine learning models using the preprocessed data.
- Evaluate models using metrics such as accuracy, F1 score, precision, and recall.

### **3. Deployment**
- Dockerize the application for containerized deployment.
- AWS EC2 Used for scalable compute resources for training, preprocessing, and serving the model.
 
- AWS S3 Centralized storage for preprocesser, model artifacts.

- Results Achieved 98% accuracy in prediction

- Reduced deployment times by 40% with automated CI/CD pipelines.

- Integrate CI/CD workflows using GitHub Actions for continuous deployment to AWS.

## AWS-Github-Actions-Deployment
1. Login to AWS console.
2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

6. Configure EC2 as self-hosted runner:

setting > actions > runner > new self hosted runner> choose os> run command one by one 

7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = 

---
## **Key Features**
- **Modular Architecture**: Each stage of the pipeline is modular and reusable.
- **Comprehensive Preprocessing**: Handles text cleaning, tokenization, and vectorization.
- **Scalable Deployment**: Uses Docker and FastAPI for easy deployment.
- **CI/CD Integration**: Automated testing and deployment with GitHub Actions.


---


## **How to Run**

### **Clone the Repository**
```bash
git clone https://github.com/your-repo/End-to-End-Sentiment-Analysis.git
cd End-to-End-Sentiment-Analysis
```

### **Create a Virtual Environment**
```bash
conda create -p env python==3.11 -y
conda activate ./env
```

### **Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Run the Flask server**
```bash
python app.py
```
---
###  ***Test the Endpoint***
#### 1.  Web Interface
```bash
Go to the web page: http://127.0.0.1:5000.
Enter a review in the text box.
Click the "Predict Sentiment" button.
View the prediction result on the screen.
```
#### 2. Postman
```bash
Open Postman 
create a new POST request:
URL: http://127.0.0.1:5000/predict
Headers: Content-Type: application/json

{
    "review_text": "I disliked the product, it was terrible."
}
```

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
  4. **Data Validation**: Verify data schema and check for missing or corrupt values and Data distribution.
  5. **Data Transformation**: Preprocess text data, including tokenization, stemming, and stop-word removal.

### **2. Model Training**
- Train machine learning models using the preprocessed data.
- Evaluate models using metrics such as accuracy, F1 score, precision, and recall.

### **3. Deployment**
- 
- Dockerize the application for containerized deployment.
- Integrate CI/CD workflows using GitHub Actions for continuous deployment to AWS.

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

### **Run the Application**
```bash
python app.py
```

---

## **Key Features**
- **Modular Architecture**: Each stage of the pipeline is modular and reusable.
- **Comprehensive Preprocessing**: Handles text cleaning, tokenization, and vectorization.
- **Scalable Deployment**: Uses Docker and FastAPI for easy deployment.
- **CI/CD Integration**: Automated testing and deployment with GitHub Actions.
- **Model Monitoring**: Log model performance metrics with MLflow.

---



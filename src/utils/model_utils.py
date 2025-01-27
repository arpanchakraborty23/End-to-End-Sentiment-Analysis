from src.logging.logger import logging
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from sklearn.metrics import roc_auc_score,accuracy_score
from src.logging.logger import logging

def model_evaluatuion(x_train,y_train,x_test,y_test,models):
    try:
            logging.info(' model evaluation started')
            report={}
            for i in range(len(models)):
                model = list(models.values())[i]
                
                #prams=prams[list(models.keys())[i]]
                print(f"Training {model}...")
                # Train model
                model.fit(x_train,y_train)                

                # Predict Testing data
                y_test_pred =model.predict(x_test)

                
                test_model_score = accuracy_score(y_test,y_test_pred)*100

                print(f"Training {model} accuracy {test_model_score}")

                report[list(models.keys())[i]] =  test_model_score

            return report
        
    except Exception as e:
        logging.info(f' Error {str(e)}')
        print(e)

def get_classification_report(y_true, y_pred):
    try:
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}
    except Exception as e:
        logging.info(f' Error {str(e)}')
        print(e)
     
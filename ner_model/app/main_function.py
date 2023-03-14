import logging
import spacy
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

model = spacy.load('ner_model/app/model/en_pr_vroozi_new')

def model_predictions(input):
    items = []
    try:
       global model
       doc = model(input['text'])
       product = {}
       suppliers = 'None'
       count = 0
       for ent in doc.ents:
           if ent.label_ == "Quantity":
               product["Quantity"] = ent.text
           elif ent.label_ == "Product":
               product["Product"] = ent.text
           elif ent.label_ == "Price":
               if '$' in ent.text:
                    product["Price"] = ent.text.replace('$',"")
               else:
                    product["Price"] = ent.text
           elif ent.label_ == "Supplier":
               suppliers = ent.text
           options = list(product.keys())
           if "Quantity" in options and "Product" in options and "Price" in options:
               product['Supplier'] = suppliers
               items.append( product)
               product = {}
               count += 1
       for item in items:
           item['Supplier'] = suppliers
    except Exception as e:
        logging.Logger.error(self=logging.Logger(name='model_predictions'),msg=str(e))
    finally:
        return items

class request_body(BaseModel):
    text : str


app = FastAPI()

@app.get("/")
def read_root():
    return {"Intro": "Model for prediction of Donation amounts of  "}


@app.post('/predict')
def prediction_function(data : request_body):
    predictions='None'
    try:
        input_payload={
            'text' :data.text,
        }
        predictions=model_predictions(input_payload)
        logging.Logger.info(predictions)

    except Exception as e:
        logging.Logger.error(self=logging.Logger(name='Prediction_Function'),msg='Prediction: '+ str(predictions))
    finally:
        return predictions


if __name__ == '__main__':
    payload={ 'text':'I want to buy 2 boxes of pasta for $4 and 1 pack of orange juice costing $3 from IJAZ EMAIL'
    }
    print(model_predictions(payload))






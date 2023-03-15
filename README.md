# AI-Purchase
An intelligent solution to identify the items that user wants to purchase. It extracts basic fields for item creation and returns a JSON.

# Requirements
```angular2html
jupyter notebook
Python 3.9.6
```
Install packages via requirements.txt inside directory [ner_model/requirements.txt] using following command
```angular2html
pip3 install -r requirements.txt
```
# Training and testing model
You can run Training and testing jupyter notebooks inside notebooks folder via command 
```angular2html
user@user: jupyter notebook
```

# Deployment 
Steps to deploy the model present in the ner_model 

1) Change the directory to ``ner_model`` directory.
2) Build the docker with follwing command.
```angular2html
docker build . -t [name]:[version] 
```
3) Run the docker image with the following command
```angular2html
docker run -d --name [name_of_container] -p [port]:80 [name_of_image]:[version_of_image]
```
4) Request the POST API using following url :
```angular2html
http://[url]:[port]/predict/
```

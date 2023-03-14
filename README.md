# ai-purchase
An intelligent solution to identify the items that user wants to purchase. It extracts basic fields for item creation and returns a JSON.

# Deployment 
Steps to deploy the model present in the ner_model 

1) Change the directory to ``ner_model`` directory.
2) Build the docker with follwing command.
```angular2html
docker build . -t name:version 
```
3) Run the docker image with the following command
```angular2html
docker run -d --name name_of_container -p port:port name_of_image:version_of_image
```
4) Request the POST API using following url :
```angular2html
http://[url]:[port]/predict/
```
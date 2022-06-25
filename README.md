### TRAINING THE MODEL : train.py 

- we receive a json from other side making requests 
- hence need Dictvectorizer (dv) to convert that dictionary like json object to numpy array X 
- this X acts as input to the model 
- y_pred is the output 


### FLASK APPLICATION AND SERVER : app.py

- not easy to send POST request from browser. hence we can use python program to call the we service 
- jsonify does not know how to convert numpy boolean (churn in this case) into boolean. need to convert to python bool. 
- need to install gunicorn for production server.
- while using gunicorn , write the following on the terminal:
    - gunicorn --bind 0.0.0.0:9696 app:app    
    - in app:app --> first one  python file name, second one is name of Flask app declared inside the python file 
    - in this case name of python file is app.py &  app = Flask("churn") is the name of the flask application 
 - waitress may be used by Windows users  in place of gunicorn  

### ENVIRONMENT MGMT AND DEPENDENCIES: pipenv
https://realpython.com/pipenv-guide/#:~:text=Pipenv%20is%20a%20packaging%20tool,a%20single%20command%20line%20tool

- install pipenv in linux python
- inside project folder run the command `pipenv shell` to make that folder a virtual env. OR 
- just go in project folder and start install dependencies using pipenv. this will also 
- make that project folder as a virtualenv. 
- it is stored somewhere in `/home/avanish/.local/share/virtualenvs/...`
- https://stackoverflow.com/questions/52540121/make-pipenv-create-the-virtualenv-in-the-same-folder
- `pipenv shell` inplace for `source/bin/activate`
- install all dependencies using pipenv instead of pip 
- it will add dependencies to Pipfile file and Pipfile.lock file.
- can use `pipenv install awsebcli --dev` to make a dependency as dev dependency.  




### MAKE REQUESTS PROGRAMATICALLY: make_request.py

- url =  'http://localhost:9696/predict'  when we deploy at the localhost
- url = 'http://avanish-ml-1.eba-jcqgyki4.ap-south-1.elasticbeanstalk.com/predict'          

 where host is not localhost but "avanish-ml-1.eba-jcqgyki4.ap-south-1.elasticbeanstalk.com"

- not easy to send POST request from browser.
- hence we can use python program to call the we service 
- use Python's inbuilt `requests` library 



### EBS DEPLOYMENT : 

- see ml zoomcamp 5.7 youtube video : shows logical diagram of ebs
- we can think of ebs to be a docker container running inside eb env. 
- `pipenv install awsebcli --dev`    : installs awscli inside virtualenv python 
- `eb init -p docker  avanish-ml-1` : last argument is name of ebs environment
- inside the project folder .elasticbeanstalk will be created which contains config.yaml
- test ebs deployment  locally : `eb local run --port 9696` 
- to launch the web service via ebs :  `eb create avanish-ml-1`
- the ebs maps docker container port to port 80. 
-  terminate ebs env : `eb terminate avanish-ml-1`

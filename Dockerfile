FROM python:3.8.12-slim

RUN pip install pipenv     

WORKDIR /app                # created inside container linux if not already there

COPY ["Pipfile", "Pipfile.lock", "./"]    # what to copy inside WORKDIR

RUN pipenv install --system --deploy

COPY ["app.py", "model_C=1.0.bin", "./"]   # copying  app.py which conatins flask app called app 

EXPOSE 9696                

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "app:app"]  # app.py : flask app. called app inside app.py



# BUILD : sudo docker build -t avanish-ml-1 .
# RUN : sudo docker run -it --rm -p 9696:9696 avanish-ml-1

# FROM python:3.8.12-slim : base filesystem in the container
# pip install pipenv   :Install pipenv in container linux 
# WORKDIR /app   : default relative directory in container linux. will be created if does not exist
# COPY ["Pipfile", "Pipfile.lock", "./"] : copy these files and folders into WORKDIR
# pipenv install --system --deploy : install all dependencies w/o creating a virtualenv
# COPY ["app.py", "model_C=1.0.bin", "./"] : copying app.py which conatins flask app and model into WORKDIR
# EXPOSE 9696 : expose ths port of container 

# ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "app:app"]  : 
#    - first app refers to app.py , second app 
#    - refers to flask app created inside of that app.py
#    - also note that lines under __name__ = "__main__" are not run when we use this gunicorn command. 

## see ml zoomcamp 5.7 youtube video : shows logical diagram of ebs

## we can think of ebs to be a docker container running inside eb env. 

## install ebs cli :
- `pipenv install awsebcli --dev`    : installs awscli inside virtualenv python 

## `eb init -p docker  avanish-ml-1` : last argument is name of ebs environment

# inside the project folder .elasticbeanstalk will be created which contains config.yaml

# test ebs deployment  locally :
- `eb local run --port 9696` 

# to launch the web service via ebs :
- `eb create avanish-ml-1`

# the ebs maps docker container port to port 80. 

# terminate ebs env :
`eb terminate avanish-ml-1`
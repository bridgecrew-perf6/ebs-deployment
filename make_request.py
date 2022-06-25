import requests


url =  'http://localhost:9696/predict'    # localhost 

host = "avanish-ml-1.eba-jcqgyki4.ap-south-1.elasticbeanstalk.com"
url = f'http://{host}/predict'           # ebs host 

# ebs does not need port number . it maps to port 80 by default. the container port
# we have already mentioned in dockerfile that it exposes 9696. 


"""
Notes : 
- not easy to send POST request from browser.
- hence we can use python program to call the we service 
- use Python's inbuilt requests library 
"""

customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
} 
 
response = requests.post(url,json = customer).json()
print(response)

if response['churn']:
    print('sending email to customer')


from flask import Flask ,jsonify,request
import pickle

"""
Notes : 
- not easy to send POST request from browser. hence we can use python program to call the we service 
- jsonify does not know how to convert numpy boolean (churn in this case) into boolean. need to convert to python bool. 
- need to install gunicorn for production server.
- while using gunicorn , write the following on the terminal:
    - gunicorn --bind 0.0.0.0:9696 app:app    
    - in app:app --> first one  python file name, second one is name of Flask app declared inside the python file 
    - in this case name of python file is app.py &  app = Flask("churn") is the name of the flask application 
 - waitress may be used by Windows users  in place of gunicorn   
"""

# load model 
model_file = 'model_C=1.0.bin'
with open(model_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)

# Flask Stuff
app = Flask("churn")

@app.route("/predict", methods = ["POST"])    # Note : not easy to send post request from browser 
def predict():
  customer = request.get_json()  
  X = dv.transform([customer])
  y_pred = model.predict_proba(X)[0, 1]
  churn = y_pred >= 0.5

  result = {
    "churn probability" : y_pred,
    "churn" : bool(churn )             # jsonify does not how to turn numpy boolean churn into boolean 
  }

  return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 9696)


 
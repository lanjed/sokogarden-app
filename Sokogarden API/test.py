# test 
from flask import * 

# create the flask app variable
app = Flask(__name__)



# define a simple route/endpoint
@app.route('/api/home', methods=['GET'])
def home():
   return jsonify({"message":"Welcome to Home Route"})

# define product route 
@app.route('/api/products', methods=['GET'])
def products():
   return jsonify({"message":"Welcome to my products page"})

# create a method that adds two numbers
@app.route('/api/calc', methods=['POST'])
def calc():
   if request.method == 'POST':
      number1 = request.form['number1']
      number2 = request.form['number2']
      sum = int(number1) + int(number2)
      return jsonify({"Answer":sum})
   
# create a method that prints fullname
@app.route('/api/fullname', methods=['POST'])
def fullname():
   if request.method == 'POST':
      firstname = request.form['firstname']
      lastname = request.form['lastname']
      fullname = firstname + " " + lastname
      return jsonify({"Name":fullname})

# run app if the file is executed
if __name__ == '__main__': 
   app.run(debug=True)
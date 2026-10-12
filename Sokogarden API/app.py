from flask import *
import pymysql
import bcrypt 
import os
from flask_cors import CORS

# contain the entire flask app inside a variable
app = Flask(__name__)
CORS(app)

# set up file upload, os helps in getting computer file path
app.config['UPLOAD_FOLDER'] = 'static/images'

# user registration: id(auto_increment),phone,email,username,password
@app.route('/api/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        # extract values posted in the frontend and store them in variables
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']


        # hashing password value using bcrypt
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # change the hashed password from bytes to string
        hashed_password = hashed.decode('utf-8')


        # connect to database : use pymysql
        connection = pymysql.connect(host="mysql-jeddy.alwaysdata.net", user="jeddy",password='modcom26', database="jeddy_sokogarden")

        # create a cursor to make changes to database
        cursor = connection.cursor()


        # sql query with the four values tobe added in the database
        # we use placeholders to prevent sql injection attack
        sql = "INSERT INTO users (username,email,password,phone) VALUES(%s,%s,%s,%s)"

        # prepare data to replace placeholders
        data = (username, email, hashed_password, phone)

        

        # use cursor to execute sql command
        cursor.execute(sql,data)

        # save information permanently
        connection.commit()

        return jsonify({'success':'Thanks for joining'})

# define a method to login/signin a user into the system
@app.route("/api/signin", methods=['POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # verify if email and password values are present
        if not email or not password:
            return jsonify({"message":'Email and password are required'})
        
        # make connection to database to verify email exists 
        connection = pymysql.connect(user='jeddy',host='mysql-jeddy.alwaysdata.net',password='modcom26',database='jeddy_sokogarden')

        # create a virtual cursor used to execute the sql commands
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # sql command to verify if email exists
        sql = "SELECT * FROM users WHERE email= %s"
        # use cursor to execute sql command
        cursor.execute(sql, (email))

        # store returned user in a variable
        user = cursor.fetchone()

        # validate there is a user
        if not user:
            return jsonify({"message":'Login Failed'})
        
        # verify password is correct 
        stored_hashed_password = user['password']

        # compare stored_hashed_password with suggested password
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
            user.pop('password', None)
            return jsonify({"message":'Logged in successful',"user":user})
        else:
            return jsonify({"message":'Login Failed'})
    

# define the add product route/endpoint
@app.route('/api/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        # Extract details to add to database
        product_name = request.form['product_name']
        product_description = request.form['product_description']
        product_cost = request.form['product_cost']

        # extract image data from request
        photo = request.files['product_photo']

        # get file name from image data
        filename = photo.filename

        # specify computer path where the image is saved
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # update location of photo to be under photo_path
        photo.save(photo_path)

        # connect to database
        connection = pymysql.connect(host='mysql-jeddy.alwaysdata.net', user='jeddy',password='modcom26',database='jeddy_sokogarden')

        # create a cursor to execute and initialize the connection
        cursor = connection.cursor()

        # sql command to add new products to database
        sql = 'INSERT INTO product_details( product_name,product_description,product_cost,product_photo) value(%s,%s,%s,%s)'
        # prepare data to replace placeholders
        data = (product_name,product_description,product_cost,filename)

        # use cursor to execute sql command
        cursor.execute(sql, data)

        # commit changes to database permanently
        connection.commit()

        return jsonify({"success":'Products added successfully'})
    

# define get product route/endpoint
@app.route('/api/get_product_details', methods=['GET'])
def get_product_details():
    # connect to database
    connection = pymysql.connect(host='mysql-jeddy.alwaysdata.net',user='jeddy',password='modcom26',database='jeddy_sokogarden')

    # create virtual cursor to execute sql commands
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # create sql command to return all products from table
    sql = 'SELECT * FROM product_details'

    # use cursor to execute sql command
    cursor.execute(sql)

    # fetch all records from cursor and store them in a variable
    products = cursor.fetchall()

    return jsonify(products)


# Mpesa Payment Route 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
        # Extract POST Values sent
        amount = request.form['amount']
        phone = request.form['phone']

        # Provide consumer_key and consumer_secret provided by safaricom
        consumer_key = "WDIhiVCiICHJeG03Jv8ag9Xd3OJge3WwUUKyfAZTJDrPHJKN"
        consumer_secret = "cPjdAkquvY6GAnDmaPh6hHUcoQvuO15FhfGG1P2lA9A6LJk0aPUm5zBibmgBw1US"

        # Authenticate Yourself using above credentials to Safaricom Services, and Bearer Token this is used by safaricom for security identification purposes - Your are given Access
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        # Provide your consumer_key and consumer_secret 
        response = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        # Get response as Dictionary
        data = response.json()
        # Retrieve the Provide Token
        # Token allows you to proceed with the transaction
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')  # Current Time
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'  # Passkey(Safaricom Provided)
        business_short_code = "174379"  # Test Paybile (Safaricom Provided)
        # Combine above 3 Strings to get data variable
        data = business_short_code + passkey + timestamp
        # Encode to Base64
        encoded = base64.b64encode(data.encode())
        password = encoded.decode()

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password":password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://coding.co.ke/api/confirm.php",
            "AccountReference": "jeddy_sokogarden Online",
            "TransactionDesc": "Payments for Products"
        }

        # POPULAING THE HTTP HEADER, PROVIDE THE TOKEN ISSUED EARLIER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        # Specify STK Push  Trigger URL
        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  
        # Create a POST Request to above url, providing headers, payload 
        # Below triggers an STK Push to the phone number indicated in the payload and the amount.
        response = requests.post(url, json=payload, headers=headers)
        print(response.text) # 
        # Give a Response
        return jsonify({"message": "An MPESA Prompt has been sent to Your Phone, Please Check & Complete Payment"})






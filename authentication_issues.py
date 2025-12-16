from flask import Flask, request, session, make_response
import jwt

app = Flask(__name__)
app.secret_key = 'weak_secret'  # Vulnerable: weak secret key

# Authentication bypass
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Vulnerable: no password verification
    if username:
        session['user'] = username
        return 'Logged in'
    return 'Failed'

# Insecure JWT
@app.route('/token')
def create_token():
    user_id = request.args.get('user_id')
    # Vulnerable: weak secret, no expiration
    token = jwt.encode({'user_id': user_id}, 'secret', algorithm='HS256')
    return token

# Session fixation
@app.route('/set_session')
def set_session():
    session_id = request.args.get('session_id')
    # Vulnerable: accepting user-provided session ID
    response = make_response('Session set')
    response.set_cookie('session_id', session_id)
    return response

# Missing authentication
@app.route('/admin/delete_user')
def delete_user():
    user_id = request.args.get('id')
    # Vulnerable: no authentication check
    # delete_user_from_db(user_id)
    return 'User deleted'

# Insecure password storage
def store_password(username, password):
    # Vulnerable: plaintext password storage
    with open('passwords.txt', 'a') as f:
        f.write(f'{username}:{password}\n')

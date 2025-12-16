import ldap
from flask import Flask, request

app = Flask(__name__)

# LDAP injection vulnerability
@app.route('/ldap_search')
def ldap_search():
    username = request.args.get('username')
    
    # Vulnerable: LDAP injection
    ldap_conn = ldap.initialize('ldap://localhost')
    search_filter = f'(uid={username})'
    result = ldap_conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, search_filter)
    
    return str(result)

@app.route('/ldap_auth')
def ldap_auth():
    user = request.args.get('user')
    password = request.args.get('password')
    
    # Vulnerable: LDAP injection in DN
    dn = f'cn={user},ou=users,dc=example,dc=com'
    ldap_conn = ldap.initialize('ldap://localhost')
    ldap_conn.simple_bind_s(dn, password)
    
    return 'Authenticated'

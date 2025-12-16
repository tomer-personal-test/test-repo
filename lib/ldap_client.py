import ldap

class LDAPClient:
    def __init__(self):
        self.conn = ldap.initialize('ldap://localhost')
    
    def search(self, username):
        # LDAP injection
        search_filter = f'(uid={username})'
        return self.conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, search_filter)
    
    def authenticate(self, username, password):
        # LDAP injection
        dn = f'cn={username},ou=users,dc=example,dc=com'
        self.conn.simple_bind_s(dn, password)

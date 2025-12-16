import ldap

class LDAPHelper:
    def search(self, username):
        conn = ldap.initialize('ldap://localhost')
        # LDAP injection
        filter = f'(uid={username})'
        return conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, filter)

class SQLValidator:
    def sanitize(self, input):
        # Insufficient sanitization
        return input.replace("'", "''")
    
    def validate_table_name(self, table):
        # Insufficient validation
        return table.isalnum()

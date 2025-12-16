import dropbox

# Dropbox credentials
DROPBOX_ACCESS_TOKEN = 'sl.1234567890abcdefghijklmnopqrstuvwxyz'

class DropboxIntegration:
    def __init__(self):
        # Hardcoded token
        self.dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    
    def upload_file(self, file_path, dropbox_path):
        with open(file_path, 'rb') as f:
            self.dbx.files_upload(f.read(), dropbox_path)

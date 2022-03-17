from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile ({'title': 'Hello. txt'}) # Create GoogLeDriveF
file1.SetContentString('Hello World! this is a file')# Set content of the
file1.Upload ()
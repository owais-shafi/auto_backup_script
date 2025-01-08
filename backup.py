# automation backup script in python
import shutil
import os
from datetime import datetime

def backup(source, destination):
    # Generate a timestamp without invalid characters for the filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create a valid backup file name
    backup_file_name = os.path.join(destination, f"backup_{timestamp}")
    
    # Create the archive with gztar (gzip + tar)
    shutil.make_archive(backup_file_name, 'gztar', source)

source = "C:/Users/insha/Desktop/py"  # source directory,what you want to backup 
destination = "C:/Users/insha/Desktop/py/backup_files"  # Destination folder,where backup will be stored

backup(source, destination)


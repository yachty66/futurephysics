"""Uploads images to Google Cloud Storage and returns their URLs."""
from google.cloud import storage
import os
google_id = "mbtichat-388909"
google_bucket = "futurephysics"

from google.cloud import storage

def upload_file_to_bucket(url, google_id, google_bucket):
    """Uploads a file to Google Cloud Storage and returns its URL."""
    client = storage.Client(project=google_id)
    bucket = client.get_bucket(google_bucket)
    blob = bucket.blob(os.path.basename(file_path))
    blob.upload_from_filename(file_path)
    file_url = blob.public_url
    return file_url


# Specify the path to your MANIFEST.IN file
manifest_file_path = 'story.py'

# Call the function to upload the file
file_url = upload_file_to_bucket(manifest_file_path, google_id, google_bucket)

print(f'File uploaded to: {file_url}')
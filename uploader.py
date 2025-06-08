import os
from google.cloud import storage
import uuid

# Load settings from env
GCS_BUCKET = os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET")
PROJECT_ID = os.getenv("PROJECT_ID")

# Create a GCS client
storage_client = storage.Client(project=PROJECT_ID)
bucket = storage_client.bucket(GCS_BUCKET)

async def upload_to_gcs(local_path: str, folder: str = "") -> str:
    filename = os.path.basename(local_path)
    blob_name = f"{folder}/{uuid.uuid4()}_{filename}" if folder else filename
    blob = bucket.blob(blob_name)

    blob.upload_from_filename(local_path)
    blob.make_public()

    return blob.public_url

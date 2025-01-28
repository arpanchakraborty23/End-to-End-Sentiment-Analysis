import os
from src.logging.logger import logging

class S3Sync:
    def sync_folder_to_s3(Self,folder,aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url}"
        logging.info(f"Executing: {command}")
        os.system(command)

    def sync_folder_from_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync {aws_bucket_url} {folder}"
        logging.info(f"Executing: {command}")
        os.system(command)

    def sync_file_to_s3(self, file_path, aws_bucket_url):
        command = f"aws s3 cp {file_path} {aws_bucket_url}"
        os.system(command)

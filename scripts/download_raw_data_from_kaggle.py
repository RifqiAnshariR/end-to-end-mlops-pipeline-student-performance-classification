import os
import shutil

import kagglehub

from app.config import config

# Download latest version
cache_path = kagglehub.dataset_download(
    "devansodariya/student-performance-data"
)

for filename in os.listdir(cache_path):
    source_file = os.path.join(cache_path, filename)
    target_file = os.path.join(config.raw_data_dir, filename)

    shutil.move(source_file, target_file)

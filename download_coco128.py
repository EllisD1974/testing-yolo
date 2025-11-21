import urllib.request
import zipfile
import os
import shutil

url = "https://github.com/ultralytics/yolov5/releases/download/v1.0/coco128.zip"
zip_path = "coco128.zip"
extract_path = "coco128"

print("Downloading COCO128...")
urllib.request.urlretrieve(url, zip_path)

print("Extracting...")
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(".")

# Rename folders
images_path = os.path.join(extract_path, "images")
labels_path = os.path.join(extract_path, "labels")

# Rename images folders
train_old = os.path.join(images_path, "train2017")
val_old = os.path.join(images_path, "test2017")
train_new = os.path.join(images_path, "train")
val_new = os.path.join(images_path, "val")

if os.path.exists(train_old):
    shutil.move(train_old, train_new)
if os.path.exists(val_old):
    shutil.move(val_old, val_new)

# Rename labels folders
train_old_labels = os.path.join(labels_path, "train2017")
val_old_labels = os.path.join(labels_path, "test2017")
train_new_labels = os.path.join(labels_path, "train")
val_new_labels = os.path.join(labels_path, "val")

if os.path.exists(train_old_labels):
    shutil.move(train_old_labels, train_new_labels)
if os.path.exists(val_old_labels):
    shutil.move(val_old_labels, val_new_labels)

print("Done! Folders renamed to 'train' and 'val'.")

import os
import shutil
from zipfile import ZipFile

def rename_files(zip_path, student_number, output_zip):
    extract_path = "renamer/temp/extracted_files"
    new_dir_path = "renamer/temp/new_dir"
    
    with ZipFile(zip_path, 'r') as z:
        z.extractall(extract_path)
    
    new_files = []
    os.makedirs(new_dir_path, exist_ok=True)
    
    childDirName = os.listdir(extract_path)[0]
        
    for filename in os.listdir(os.path.join(extract_path, childDirName)):
        print("renaming:", filename)
        if "PROJECT 2" in filename:
            new_name = filename.replace("PROJECT 2", f"{student_number}-ASSIGNMENT-2W24")
            original_path = os.path.join(extract_path, childDirName, filename)
            new_file_path = os.path.join(new_dir_path, new_name)
            os.rename(original_path, new_file_path)
            new_files.append(new_file_path)

    with ZipFile(output_zip, 'w') as z:
        for file in new_files:
            z.write(file, os.path.basename(file))
    
    # Cleanup
    for file in new_files:
        os.remove(file)
    if os.path.exists(new_dir_path):
        shutil.rmtree(new_dir_path)
    if os.path.exists(extract_path):
        shutil.rmtree(extract_path)

from .main import rename_files

if __name__ == "__main__":
    path = r"C:\\Users\\Raas\\Downloads\\6.0 PROJECT-2 DRILL JIG.zip"
    student_number = "301229214"
    output_zip = "output.zip"
    rename_files(path, student_number, output_zip)
import os
import zipfile

letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

version = os.getenv("VERSION", "1.2.0")

def create_txt_file(letter):
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is {letter}.txt")

def create_zip_file(letter):
    with zipfile.ZipFile(f"{letter}_{version}.zip", "w") as zipf:
        zipf.write(f"{letter}.txt")

for letter in letters:
    create_txt_file(letter)
    print(f"Created {letter}.txt")

for letter in letters:
    create_zip_file(letter)
    print(f"Created {letter}_{version}.zip")

txt_files_exist = all(os.path.exists(f"{letter}.txt") for letter in letters)
zip_files_exist = all(os.path.exists(f"{letter}_{version}.zip") for letter in letters)

if txt_files_exist:
    print("All txt files created successfully.")
else:
    print("Failed: Some txt files were not created.")

if zip_files_exist:
    print("All zip files created successfully.")
else:
    print("Failed: Some zip files were not created.")

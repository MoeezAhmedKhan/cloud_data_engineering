# Write a Python program (using OOP) to rename all files of a specific extension inside a given folder.
# The program should:
# Ask the user for folder path, file extension, and base name.
# Rename files as BaseName01.ext, BaseName02.ext, etc.
# Stop safely if a file with the new name already exists.
# Show clear messages for success, conflicts, or missing files.
# Use the os module and a class structure (FileRenamer).

import os

class FileRenamer:
    def __init__(self):
        print("📂 Welcome to File Renamer Utility\n")
        directory = input("Enter the folder name or path (relative to current directory): ").strip()
        self.folderPath = os.path.join(os.getcwd(), directory)
        self.extension = input("Enter the file extension (e.g. .pdf, .jpg, .png): ").strip()
        self.baseName = input("📝 Enter the new base name for files (e.g. MyFile): ").strip()
        print("\n🔄 Starting rename process...\n")
        self.rename_file()
        
    
    def rename_file(self):
        if self.extension.startswith("."):
            self.extension = self.extension[1:]
        
        if not os.path.exists(self.folderPath):
            print("Path not exist!")
        else:
            directoryFiles = os.listdir(self.folderPath)
            filteredData = list(filter(lambda f:f.endswith(f".{self.extension}"), directoryFiles)) # Here we can also use list comprehension instead of filter
            if(len(filteredData) > 0):
                for index, file in enumerate(filteredData):
                    expected = f"{self.baseName}{index+1:02d}.{self.extension}"
                    if(f"{file}" == expected):
                        print(f"{file} already named correctly. Skipping...")
                        continue
                    olderFile = os.path.join(self.folderPath, file)
                    newFile = os.path.join(self.folderPath,expected)
                    if(os.path.isfile(newFile)):
                        print(
                            f"⚠️  Rename halted: '{file}' cannot be renamed to '{expected}' "
                            f"because that file already exists in the same directory.\n"
                            f"⚠️  Possible cause: You modified or renamed files manually between operations.\n"
                            f"⚠️  Process stopped to avoid data loss."
                        )
                        break
                    os.rename(olderFile, newFile)
                    print(f"🟢 Renamed: '{file}' → '{expected}'")
                print("\n✅ Rename process completed successfully!\n")
            else:
                print(f"According to given extension {self.extension} No Data exist!")
        
        
FileRenamer()


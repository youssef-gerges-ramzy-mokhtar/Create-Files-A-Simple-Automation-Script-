import os

userPathInput = input("Please Enter the Folder Path: ")
numFiles = int(input("Please Enter the Number of Files: "))
extension = input("Please enter the File Extension: ")

for i in range(numFiles):
    file = str(i+1) + "." + extension
    open(os.path.join(userPathInput, file), 'w')
import os
for file in os.listdir():
    if file.lower().endswith(".jpg") == True:
        print(file)
import os       # i/o files
import shutil   # copies files

path = "C:\\Users\\Zach\\OneDrive\\Desktop\\Python-Mini-Projects\\python-mini-projects\\file-handling\\data\\test.txt"

if os.path.exists(path):
    print("The path exists")
    if os.path.isfile(path):
        print("The file exists")
    elif os.path.isdir(path):
        print("The dir exists")
else:
    print("The path doesn't exist")
print()

# reading a file
try:
    with open(path) as file:
        print(file.read())
except FileNotFoundError:
    print("File was not found.")

# writing/appending a file
with open(path, "a") as file:
    file.write("Morning glory!\n")
    file.write("the well bucket-entangled,\n")
    file.write("I ask for water.\n\n")

# copying a file
destPath = "C:\\Users\\Zach\\OneDrive\\Desktop\\Python-Mini-Projects\\python-mini-projects\\file-handling\\data\\copyOfText.txt"
shutil.copyfile(path, destPath)


# moving a file
src = "C:\\Users\\Zach\\OneDrive\\Desktop\\Python-Mini-Projects\\python-mini-projects\\file-handling\\data\\copyOfText.txt"
dst = "C:\\Users\\Zach\\OneDrive\\Desktop\\Python-Mini-Projects\\python-mini-projects\\file-handling\\copyOfText.txt"
try:
    if os.path.exists(dst):
        print("There is already a file there!")
    else:
        os.replace(src, dst)
        print(src + " was moved.")
except FileNotFoundError:
    print(src + " was not found.")


# # deleting a file
# try:
#     os.remove(path)
# except FileNotFoundError:
#     print("That file was not found")

import pywhatkit as tool
import pyfiglet


def textfile(file_name_with_path):
    filename = input("enter the filename to save the image as: ")
    with open(file_name_with_path, "r") as fobj:
        file_data = fobj.read()
    tool.text_to_handwriting(file_data, f"/home/ramees/handwritten-notes/{filename}.jpg")
def stringastext(text_to_convert):

    filename = input("enter the filename to save the image as: ")
    tool.text_to_handwriting(text_to_convert, f"/home/ramees/handwritten-notes/{filename}.jpg")

banner = pyfiglet.figlet_format("Text_To_Handwriting")
print(banner)
print("Author : Ramees")


print("choose your option")
print(" 1. covert a textfile ")
print(" 2. convert a string  ")
choice = int(input("enter the choice (1 or 2): "))

if choice == 1:
    path_of_file = input("enter the path of your text file to convert: ")
    textfile(path_of_file)
if choice == 2:
    enter_text = input("enter the text file you want to convert: ")
    stringastext(enter_text)

print("program exiting.. :)")


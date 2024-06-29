import os

# Replace 'folder_path' with the actual path to the folder containing the files
folder_path = "/Users/isabelcuddihy/Desktop/Coding Practice/File Renamer/File Renamer"

# Change the current working directory to the folder_path
os.chdir(folder_path)
#FUTURE ADDITON - Content_Type = input("Enter Content Type: ")
#FUTURE ADDITION - if Content_Type == "Caption":
Partner = input("Enter Partner Name: ")
for file in os.listdir("."):
    # Check if the file is a regular file (not a directory)
    if Partner == "Roku" or Partner == "Wurl" or Partner == "Vizio":
        if os.path.isfile(file):
            # Extract the last 6 characters before the extension
            filename, extension = os.path.splitext(file)
            new_name = filename[-6:] + extension

            # Rename the file
            os.rename(file, new_name)
        else:
            continue
    elif Partner == "Pluto" or Partner == "Xumo" or Partner == "Plex" or Partner == "Hoopla":
        if os.path.isfile(file):
        # Skip certain files with specific names including hidden files
            if file.startswith('.') or file.startswith ("rename") or file.startswith("_"):
                continue
        
            # Remove the "EN_" and Epi ID from filename
            filename, extension = os.path.splitext(file)
            new_name = filename.replace("EN_", "")
            new_name = new_name[:-7] + extension
            
            # Rename the file
            os.rename(file, new_name)
        else:
            continue
    elif Partner == "Crackle":
        if os.path.isfile(file):
        # Skip certain files with specific names including hidden files
            if file.startswith('.') or file.startswith ("rename") or file.startswith("_"):
                continue
        
            # Remove the illegal characters from art filenames
            illegal_characters = ["'", ":", "&", " "]
            filename, extension = os.path.splitext(file)
            for char in illegal_characters:
                filename= filename.replace(char,"")
            new_name = filename    
            new_name = new_name+ extension
            
            # Rename the file
            os.rename(file, new_name)
        else:
            continue
    else:
        print("Partner Rename Not Available")
#FUTURE ADDITION - if Content Type == "Video"
#Partner = input("Enter Partner Name: ")
#for file in os.listdir("."):
    # Check if the file is a regular file (not a directory)
    #if Partner == "Roku" or Partner == "Wurl" or Partner == "Vizio":
       # if os.path.isfile(file):
            # Extract the last 6 characters before the extension
        #    filename, extension = os.path.splitext(file)
        #    new_name = filename[-6:] + extension

            # Rename the file
       #     os.rename(file, new_name)
      #  else:
      #      continue
print(illegal_characters)

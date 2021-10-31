import os

# Absolute path of a file
x = 1

while(x < 5):
    #old_name = r"C:/Users/justi/OneDrive/Desktop/Testing Folder/00" + str(x) + ".txt"
    #new_name = r"C:/Users/justi/OneDrive/Desktop/Testing Folder/Helstin00" + str(x)  + ".txt"
    
    old_name = r"C:/Users/justi/OneDrive/Desktop/Testing Folder/HelloJustin00" + str(x)  + ".txt"
    new_name = r"C:/Users/justi/OneDrive/Desktop/Testing Folder/00" + str(x) + ".txt"
    # Renaming the file
    os.rename(old_name, new_name)
    x = x+1
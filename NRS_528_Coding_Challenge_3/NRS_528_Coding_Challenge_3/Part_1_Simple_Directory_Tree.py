# Coding Challenge 3: Part 1

# Replicate this tree of directories and subdirectories:

# ├── draft_code
# |   ├── pending
# |   └── complete
# ├── includes
# ├── layouts
# |   ├── default
# |   └── post
# |       └── posted
# └── site

# Using os.system or os.mkdirs replicate this simple directory tree.
# Delete the directory tree without deleting your entire hard drive.
# No pressure!

import os

directory = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree'
os.mkdir(directory)

filepath_1 = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\draft_code'
os.mkdir(filepath_1)

subdirectory_1A = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\draft_code\pending'
os.mkdir(subdirectory_1A)

subdirectory_1B = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\draft_code\complete'
os.mkdir(subdirectory_1B)

filepath_2 = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\includes'
os.mkdir(filepath_2)

filepath_3 = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\layouts'
os.mkdir(filepath_3)

subdirectory_2A = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\layouts\default'
os.mkdir(subdirectory_2A)

subdirectory_2B = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\layouts\post'
os.mkdir(subdirectory_2B)

subsubdirectory = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\layouts\post\posted'
os.mkdir(subsubdirectory)

filepath_4 = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\site'
os.mkdir(filepath_4)

list = os.listdir(directory)
print(list)
for folder_name in list:
    if (folder_name == "draft_code" or
            folder_name == "includes" or
            folder_name == "layouts" or
            folder_name == "site"):
      print("Yay, making this directory worked!")
    elif (folder_name == "pending" or
          folder_name == "complete" or
          folder_name == "default" or
          folder_name == "post" or
          folder_name == "posted"):
      print("Cool, just making sure the subdirectories work too.")
    else:
      print("Check your code, you screwed up somewhere.")

######

# Yay, it works! Now let's delete it all while keeping my hard drive intact.

######
# os.rmdir(directory)
# os.system("dir")
######

# The code above is bad code.
# Why? Because if the house goes up in flames, everyone needs to be out before the house goes.
# Make sure all the subdirectories are deleted before trying to delete the main directory.

#######

# We still need to reference the directories we're deleting,
#   so we can't just leave them commented out, as per above.
# Instead, I'm going to relist all the references down here,
#   in the order they should be deleted in,
#   so we can remove the directory more easily.

#######

# subsubdirectory = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\layouts\post\posted'
#
# subdirectory_1A = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\draft_code\pending'
# subdirectory_1B = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\draft_code\complete'
# subdirectory_2A = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\layouts\default'
# subdirectory_2B = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\layouts\post'
#
# filepath_1 = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\draft_code'
# filepath_2 = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\includes'
# filepath_3 = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\layouts'
# filepath_4 = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree\site'
#
# directory = r'C:\Users\ektic\Coding_Challenge_3_Directory_Tree'
#
# os.rmdir(subsubdirectory)
#
# os.rmdir(subdirectory_1A)
# os.rmdir(subdirectory_1B)
#
# os.rmdir(subdirectory_2A)
# os.rmdir(subdirectory_2B)
#
# os.rmdir(filepath_1)
# os.rmdir(filepath_2)
# os.rmdir(filepath_3)
# os.rmdir(filepath_4)
#
# os.rmdir(directory)
#
# directory_parent_folder = r'C:\Users\ektic'
#
# os.listdir(directory_parent_folder)
#
# for folder in os.listdir(directory_parent_folder):
#     if folder == r'Coding_Challenge_3_Directory_Tree':
#         print("Oops, try again")
#     else:
#         print("All gone!")

#Task 6
#edx online cource task
#File System
#Directory operations
# [ ] Complete the following program to:
# 1) navigate to `parent_dir` directory (if not already in it)
# 2) create a new directory called `practice_1`
# 3) change the working directory to `practice_1`
# 4) display the current working directory to verify you are in the correct location
# 5) create a new directory called `practice_2`
# 6) verify that `practice_2` was created by listing the content of the current directory
# 7) rename `practice_2` as `sub_practice_2`
# 8) verify the name was successful changed by listing the content of the current directory
# 9) remove `sub_practice_2`
# 10) change working directory to the parent directory using `..`
# 11) remove `practice_1`
# 12) verify your current working directory and display its content

import os, os.path

# 1) navigate to `parent_dir` directory (if not already in it)
if('parent_dir' not in os.getcwd()):
    # Changing the current working directory to parent dir
    print("Changing working dir to parent_dir")
    os.mkdir('parent_dir')
    os.chdir('parent_dir')
    print("Current working directory:", os.getcwd())

# 2) create a new directory called `practice_1`
#TODO
os.mkdir("practice_1")

# 3) change the working directory to `practice_1`
#TODO
os.chdir("practice_1")

# 4) display the current working directory to verify you are in the correct location
#TODO
print(os.getcwd(), "current dir after changing to prac1")
# 5) create a new directory called `practice_2`
#TODO
os.mkdir("practice_2")

# 6) verify that `practice_2` was created by listing the content of the current directory
#TODO
print(os.listdir(), "verify prac 2")
# 7) rename `practice_2` as `sub_practice_2`
#TODO

os.rename("practice_2","sub_practice_2")

# 8) verify the name was successful changed by listing the content of the current directory
#TODO
print(os.listdir(),"verify name is changed to sub")

# 9) remove `sub_practice_2`
#TODO
os.rmdir("sub_practice_2")

# 10) change working directory to the parent directory using `..`
#TODO
os.chdir("..")

# 11) remove `practice_1`
#TODO
os.rmdir("practice_1")

# 12) verify your current working directory and display its content
#TODO
print(os.getcwd(), "current dir")
print(os.listdir(), "list of current dir")

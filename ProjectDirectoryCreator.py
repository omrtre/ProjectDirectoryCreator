#### Ask where to:
###### Create folders in sequnece
###### Create readme's for initial folder
### Must follow a top-level hierachy diagram

### Make a checking funciton for project files that don't exist
### INtegration with Github, init pull, etc

### os.mkdir
### os.mkdirs

import os

def programPDC_init():

    inputPDC_name = input("Name of the Project?")
    inputPDC_desc = input("Description of the Project") ## add a character limit to this.
    inputPDC_loc = input("") # where is this directory going to be created.

    if os.path.dirname(projectName):
        ### don't do anything
        print("Dummy")
    else:
        ### create the directoy
        print("Dummy")

    

    print("Project Directory Creator, Ready.")

def programPDC_decorator():
    print("Dummy.")


def main():
    programPDC_init()
   
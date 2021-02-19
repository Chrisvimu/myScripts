# dependancies
import os
import fastProjectGit


# Writes ReadMe with a basic layout
def writeReadme(files):
    try:
        file = open(files, "w")
        file.write("# El encabezado más largo" + "\n" +
                   "## El segundo encabezado más largo" + "\n" + "###### El encabezado más pequeño")
        file.close()
    except Exception:
        print("Error when writing readMe")


# Create files
def createLocalFile(pathf):
    print(pathf)
    with open(pathf, 'a'):
        os.utime(pathf, None)
    return pathf


# Create folder Tree
def createTree(path):
    try:
        createLocalProject(path)
        createLocalProject(path + "/Resources")
        createLocalProject(path + "/Docs")
        readMe = createLocalFile(path + "/readMe.md")
        writeReadme(readMe)
        createLocalFile(path + "/Resources/index.html")
        return True
    except Exception:
        print("Error tree creation" + path)
        exit()


# Create project folder
def createLocalProject(path):
    print(path)
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of directory failed")
        exit()
    else:
        return True


# Generic things
def readTitle():
    return(input('Project name? '))


# detect the current working directory and check if it is correct.
def userLocation(title):
    path = os.getcwd()
    print("The current working directory is %s" % path)
    print("The project will be created a subfolder here, is that correct?")
    if (input(() == "yes" or "y").lower()):
        path = path + "/" + title
        return path
    else:
        exit()


# Only calls other
def main():
    try:
        title = readTitle()
        project = userLocation(title)
        createTree(project)
        print("Project folder created in :" + project)
        fastProjectGit.main(title)
    except Exception:
        print("Project folder error: " + project)
        exit()


# Begins the script
if __name__ == "__main__":
    main()

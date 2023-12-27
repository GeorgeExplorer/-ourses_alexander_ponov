def newfile():

    directory = open("test_files/newFile1.txt", "a")
    newFile = directory.write("\nNew line")
    directory.close()

    directory = open("test_files/newFile1.txt", "r")
    newFile = directory.read()
    print(newFile)
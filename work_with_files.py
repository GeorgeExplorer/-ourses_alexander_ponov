import new_file

changeFile = open('test_files/newFile1.txt', 'w')
changeFile.write('Delete all lines and save only this one')
changeFile.close()

readFile = open('test_files/newFile1.txt', 'r')
text = readFile.read()
readFile.close()

print(text)
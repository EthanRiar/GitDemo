file = open('test.txt')
#print(file.read(1))
#print(file.readline())
#print(file.readline())

line = file.readline()
while line != '':
    print(line)
    line = file.readline()

print(type(line))



file.close()
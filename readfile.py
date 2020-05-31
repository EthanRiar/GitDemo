with open('test.txt','r') as file:
    list1 = file.readlines()



    with open('test.txt','w') as writer:

        list1.__reversed__()
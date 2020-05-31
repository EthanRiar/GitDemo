try:
    with open('test.txt') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print('test')
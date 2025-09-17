try:
    file1 = open('sample.txt', 'r')
    print("Reading file contents:")
    file1_data = file1.readlines()
    i=1
    for x in file1_data:
        print("Line ",i,":",x)
        i+=1
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
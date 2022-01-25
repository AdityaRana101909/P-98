from fileinput import filename


def counter():
    filename= input("Enter the file name")
    file= open(filename,'r')
    count=0
    for line in file:
        words=line.split()
        count= count+len(words)
    print('No. of words =')
    print(count)

counter()
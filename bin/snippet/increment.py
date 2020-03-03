import os


def incrementName():

    i = 0
    while os.path.exists("sample%s.txt" % i):
        i += 1


    fh = open("sample%s.txt" % i, "w")

    print(i)



incrementName()


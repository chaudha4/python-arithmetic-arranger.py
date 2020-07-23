

print("hello world")


def count_words_in_file():
    filename = input("Please enter the file name:")

    # One way to print
    print("You entered: %s" % (filename))

    # Another way using format method
    print("You entered: {0}".format(filename))
    handle = open(filename, "r")
    
    mydict = dict()
    for line in handle:
        for word in line.split():
            #print(word, end="\n")
            if word not in mydict:
                mydict[word] = 1
            else:
                mydict[word] = mydict[word] + 1

    print(mydict)


count_words_in_file()

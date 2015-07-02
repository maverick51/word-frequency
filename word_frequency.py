import re #import for re.sub


def word_frequency(mystring):
    '''This function counts the number of words in the passed in string'''

    freq = {} #the dictionary of words and number of appearances
    #change string to a list to make it easier to pull out words
    mylist = mystring.split(' ')

    #find number of times words appear in string
    for word in mylist:
        if word not in freq:  #add word for first time
            freq[word] = 1
        else:  #word appears already so add one to total
            freq[word] += 1

    freq = dict(freq)  #change list of words/total to dictionary

    return freq  #return list of words/total as dictionary


if __name__ == "__main__":
    #do whatever when the file is run directly

    #open file and read in whole text
    with open("sample.txt") as sample:
        data = repr(sample.readlines())

    #make data lower case
    data = data.lower()

    #strip all punctuation and commands
    data = re.sub(r'[^A-Za-z]', r' ', data)

    #call word_frequency to find out how many times words appear
    mydict = word_frequency(data)

    #call sorted to make a list of sorted words by accurance
    mydictsorted = sorted(mydict.items(), key=lambda x: x[1], reverse=True)

    #print out the top 20 most used words
    count = 0
    while count <= 19:
        (x, y) = mydictsorted[count]
        print(x, y)
        count += 1

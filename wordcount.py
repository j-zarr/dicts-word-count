

def get_word_count(filename):
    """Count words in file."""

    # create an empty dictionary
    word_count = {}

    # read file and get each word 
    file_name = open(filename)

    for line in file_name: #outer loop looping over lines
        words_in_line = line.rstrip().split(" ") #creats a list of all words of one line
        for word in words_in_line: #loop through each word of the line from outer loop
            word_count[word] = word_count.get(word, 0) + 1 #Creates the dictionary
    
    file_name.close()

    print(word_count)
    return word_count

get_word_count("test.txt")

    
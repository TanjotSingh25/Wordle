class database:

    def __init__(self, word_length, file):
        self.word_length = word_length
        self.database = self.make_hash_table()
        self.search_database = []
        self.make_database(file)

    def make_database(self, file):
        word_file = open(file)
        for word in word_file:
            word = word.strip()
            if(len(word) != self.word_length):  
                continue
            if(word == ""):
                continue
            self.hash(word)
            self.search_database.append(word)

    def make_hash_table(self):
        hash_table = []
        for i in range(0, 26*26*26):
            hash_table.append([])
        return hash_table

    # Creating function that hashes each string based of first 3 characters of that word
    def hash_number(self, word):
        # convert char to ascii value
        c = (26*26*(ord(word[0])-97)) + (26*(ord(word[1])-97)) + (ord(word[2])-97)
        return c
    
    def hash(self, word):
        h = self.hash_number(word)
        self.database[h].append(word)
    
    def add_word(self, word):
        if(word.length() != self.word_length):
            print("Word length does not match")
            return
        h = self.hash_number(word)
        self.database[h].append(word)





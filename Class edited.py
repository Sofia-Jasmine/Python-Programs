class String:
    def __init__(self):
        self.upper = 0
        self.lower = 0
        self.vowel = 0
        self.consonant = 0
        self.space = 0
        self.string = ""
        
    def getstring(self):
        self.string = input("Enter a String: ")
        
    def count(self):
        for ch in self.string:
            if ch.isupper():
                self.upper += 1
            if ch.islower():
                self.lower += 1
            if ch in "AEIOUaeiou":
                self.vowel += 1
            if ch == " ":
                self.space += 1
        self.consonant = self.upper + self.lower - self.vowel
        
    def display(self):
        print("The given string contains....")
        print("%d Uppercase Letters" % self.upper)
        print("%d Lowercase Letters" % self.lower)
        print("%d Vowels" % self.vowel)
        print("%d Consonants" % self.consonant)
        print("%d Spaces" % self.space)
        
# Creating an instance of the String class
S = String()

# Calling the methods to get input, analyze, and display the string statistics
S.getstring()
S.count()
S.display()

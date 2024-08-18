class String:
    def__init__(self):
        self.upper=0
        self.lower=0
        self.vowel=0
        self.consonanat=0
        self.space=0
        self.string=" "
    def getstring(self):
        self.string=str(input("Enter a String:"))
    def count(self):
        for ch in self.string:
            if (ch.isupper()):
                self.uppercase+=1
            if (ch.islower()):
                self.lowercase+=1
            if (ch in ("AEIOUaeiou")):
                self.vowel+=1
            if(ch==""):
                self.spaces+=1
            self.consonant=self.upper+self.lower-self.vowel
    def display(self):
        print("The given string contains....")
        print("%d Uppercase Letters"%self.upper)
        print("%d Lowercase Letters"%self.lower)
        print("%d Vowels"%self.vowels)
        print("%d Consonants"%self.consonants)
        print("%d Spaces"%self.space)
        S=String()
        S.getstr()
        S.execute()
        S.display()
                

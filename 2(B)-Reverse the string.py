def reverse (str1):
    str2=""
    for i in str1:
        str2=i+str2
    return str2
word=input("\nEnter a String:")
print("\nThe reverse of the given string is:",reverse(word))
        
    

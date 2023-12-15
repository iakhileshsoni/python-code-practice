# Check if a character is a vowel or consonant



def CheckVowelCons(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter in vowels:
        print("{0} is Vowel".format(letter))
    else:
        print("{0} is Consonent".format(letter))


letter = "e"
CheckVowelCons(letter)


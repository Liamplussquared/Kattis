#https://open.kattis.com/problems/anewalphabet
alphabet = {
    "A": "@",
    "B": "8",
    "C": "(",
    "D": "|)",
    "E": "3",
    "F": "#",
    "G": "6",
    "H": "[-]",
    "I": "|",
    "J": "_|",
    "K": "|<",
    "L": "1",
    "M": "[]\\/[]",
    "N": "[]\\[]",
    "O": "0",
    "P": "|D",
    "Q": "(,)",
    "R": "|Z",
    "S": "$",
    "T": "']['",
    "U": "|_|",
    "V": "\\/",
    "W": "\\/\\/",
    "X": "}{",
    "Y": "`/",
    "Z": "2",
    " ":" "
}
translation = ""
for letter in input():
    if letter.upper() in alphabet:
        translation+= alphabet[letter.upper()]
    else: translation+=letter
print (translation)
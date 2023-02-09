avalue="saurabh"
# print(type(avalue))            ## (string)
# print(len(avalue))             ## (7)length is 7
# print(avalue.capitalize())     ## (Saurabh)initial letter is capitalised--S
# print(avalue.upper())          ##(SAURABH) whole string is converted into upper case
# print(avalue.lower())          ##(saurabh) whole string is converted into lower case
# print(avalue.startswith("s"))  ##(true) gives boolean Trues/False if condition is satisfied
# print(avalue.endswith("bh"))   ##(true)  gives boolean Trues/False if condition is satisfied
# print(avalue.find("r"))        ##(3) indicate index of given character
#print(avalue.find("R"))         ##(-1) index is -1 as "CAPITAL R" is absent
# print(avalue.find("abh"))      ##(4) indicate the starting index of given sub_string
#print(avalue.find("ABH"))       ##(-1) index is -1 as "CAPITAL ABH" is absent
#print(avalue.find("a",2))       ##(4)indicate index of 'a' but starts counting from index"2"
# print(avalue.find("ura",1))     ##(2) in given syntax "ura" indicate what to find and ""1" indicate starting index
# print(avalue.find("rab",2,6))   ##(3) in given syntax "rab" indicate what to find and ""2" indicate starting index and "6" is limit
#print(avalue.count('a'))          ##(2) indicate count of char in given string
#print(avalue.replace('sau','pau'))  ##(paurabh)) performs replacement
#print(avalue.replace('sau','pau').replace('abh','bbb'))  ## performs simultaneous replacement
#print(avalue.replace('sau','pau').replace('pau','mau').replace('mau','gau'))  ## performs simultaneous replacement
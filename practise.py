#nm='harry'
# print(nm)   ### harry
#print(nm[-4:-2])  ## ar

#=================================================
# pie="Applepie"
# print(pie[:5])     ##Apple
# print(pie[5:])     ##pie
# print(pie[2:6])    ##plep
# print(pie[-8:])    ##Applepie

##==============================================
# for i in range(5):
#     print(i)       ## 01234

##================================================
#print(len("python"))  ## length is 6
#print(len("python          "))## length is 16 as it considers space given in in string size

###=================================================
# x=input("Enter your name:")
# print("my name is",x)  ##my name is saurabh 

##====================================================
# name="saurabh"
# print("hello,", name)  ## hello, saurabh

# ##===================================================
# print("He said,\"I want to eat an apple\". ")   ### He said,"I want to eat an apple".

###====================================================
# Address='''saurabh patil
# manegaon
# madha                    
# solapur
# 413410'''
# print(Address)  

##==========================================================
# Address='''saurabh patil
# manegaon
# madha                    
# solapur
# 413410'''
# for alphabets in Address:
#     print(alphabets)  #### alphabet by alphabet extraction from given string

##===========================================================
# city="solapur"
# print(city[0:-5])  #### ([0:-5] is equal to [0:2])

##=============================================================
# taste="yummmmmmmm"
# print(taste.rstrip("m"))  ##yu

##==============================================================
# str="daddy"
# print(str.replace("d","p",3))

# god="digambara digambara shripad vallabha digambara "
# print(god)
# print(god.replace("digambara","vitthal"))  ##vitthal vitthal shripad vallabha vitthal 
# print(god.replace("digambara","vitthal",0)) ##digambara digambara shripad vallabha digambara 
# print(god.replace("digambara","vitthal",1)) ##vitthal digambara shripad vallabha digambara   
# print(god.replace("digambara","vitthal",2)) ##vitthal vitthal shripad vallabha digambara
# print(god.replace("digambara","vitthal"))   ##vitthal vitthal shripad vallabha vitthal     

##====================================================================
# god="digambara digambara shripad vallabha digambara "
# print(god.split())  ##['digambara', 'digambara', 'shripad', 'vallabha', 'digambara']
   
##========================================================================
relation="Akka" 
# print(relation.startswith("Ak"))  ##True
# print(relation.endswith("a"))    ##false

##===============================================================================
# field="we have five acres of land"
# print(field.title())       ## We Have Five Acres Of Land

# qst="How Are you doing"
# print(qst.swapcase())   ##hOW aRE YOU DOING

##===========================================================================
# colours=['red','blue','white','pink']
# if 'red' in colours:
#     print('yes')
# else:
#     print('no')

##========================================================================= 
# state=['maharashtra','punjab','karnataka']
# city=['mumbai','amritsar','ooty']
# l=state.extend(city)
# print(l)

# l=[1,2,3,4,5]
# m=[6,7,8,9]
# print(l.extend(m))

##==============================================================================
color=['red','green','blue']
color2=['white','black','grey']
print(color2+color)   ##['white', 'black', 'grey', 'red', 'green', 'blue']
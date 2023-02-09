# avalue=input("Enter the string :")                    ## ENTERED STRING IS "INNOVANT"
# bvalue=input("Enter the character from avalue :")

# Result=avalue.find(bvalue,0)
# print(f"INDEX of N in given string :{(Result)}")      ## SHOWS INDEX OF N=1

# Result=avalue.find(bvalue,2)
# print(f"INDEX of N in given string :{(Result)}")       ##SHOWS INDEX OF N=2

# Result=avalue.find(bvalue,5)
# print(f"INDEX of N in given string :{(Result)}")        ## SHOWS INDEX OF N=6


                
## PROGRAM FOR FINDING THE COUNT------

# avalue="saurabh"
# result=avalue.count('a')
# print(f"count of \"a\" : {(result)}")


## PROGRAM FOR ESCAPE SEQUENCE CHARACTER AND REPLACING THE STRINGS
avalue= "\n Dear Candidate,\n\t We are delighted to inform you that you have cleared all the rounds of interview and we are extending the offer to join us.\nThank You,\nHR"

#print(avalue)
result=avalue.replace('Candidate','Saurabh').replace('HR','Rahul')
print(result)
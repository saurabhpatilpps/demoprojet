avalue="welcome"
# print(avalue)        #welcome
# print(avalue[0])     #w
# print(avalue[1])     #e
# print(avalue[2])     #l
# print(avalue[3])     #c
# print(avalue[4])     #o
# print(avalue[5])     #m
# print(avalue[6])     #e
# print(avalue[7])     #string index out of range
# print(avalue[-1])     #e
# print(avalue[-2])     #m
# print(avalue[-3])     #o
# print(avalue[-4])     #c
# print(avalue[-5])     #l
# print(avalue[-6])     #e
# print(avalue[-7])     #w
#print(len(avalue))    # (7)dislpays actual length of given string...
#print(avalue[0],avalue[1],avalue[2],avalue[3],avalue[4],avalue[5],avalue[6])   ## w e l c o m e
#print(avalue[0]+avalue[1]+avalue[2]+avalue[3]+avalue[4]+avalue[5]+avalue[6])     ##welcome
#print(avalue[-1]+avalue[-2]+avalue[-3]+avalue[-4]+avalue[-5]+avalue[-6]+avalue[-7]) ## emoclew
# print(avalue[0:2])  ##(we) will start from 0 index and take 2 values from start
# print(avalue[0:3])   ##(wel) will start from 0 index and take 3 values from start
#print(avalue[0:])       ##(welcome) will start from 0 index and take all value after that
#print(avalue[:])         ## (welcome)
# print(avalue[3:])       ##(come) will start from  3 index and take remaining values
# print(avalue[3:6])       ##(com) will start from 3 index and take 6 values from start
# print(avalue[3:7])        ##(come) will start from 3 index and take 7 values from start
#print(avalue[3:100])       ##(come) will start from 3 index and take whole values after 3
#print(avalue[-1:-7])         ## will show blank output
#print(avalue[-1:-6])          ## will show blank output
#print(avalue[-1:-5])            ## will show blank output
#print(avalue[-7:])             ## (welcome) will start from -7 reverse index and continue till end
# print(avalue[-7:0])              ## blank output
# print(avalue[-7:-1])             ## (welcom) will start from -7 reverse index and continue till -1
# print(avalue[-7:7])               ##(welcome) will start from -7 reverse index and go till end
#print(avalue[0:7:0])              ##inserted pattern represents slice step and it should not be zero
#print(avalue[0:7:1])            ##(welcome)
#print(avalue[0:7:2])           ##(wloe)
#print(avalue[0:7:3])             ##(wce)
#print(avalue[-2:-5])          ##blank output
#print(avalue[-7:-4])           ## (wel)
print(avalue[-1::-1])          ## emoclew
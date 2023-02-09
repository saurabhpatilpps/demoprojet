avalue=10,20,30,10,40,50,10,20,60,50
#print(type(avalue))    ##...tuple

# print(f"before count(10)")
# result=avalue.count(10)
# print(f"after count(10):{result}")

# print(avalue.count(10))  #### displays count of 10---3
# print(avalue.count(100))  #### displays count of 100 as 0 because no values present in tuple=100
##print(avalue.index(10))  #### displays index=0


firstindex=avalue.index(10)
secondindex=avalue.index(10,firstindex+1)
thirdindex=avalue.index(10,secondindex+1)
print(firstindex,secondindex,thirdindex)   ### displays indices of same element at different positions
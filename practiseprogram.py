##(1)To find length of list
# city=['Maharaashtra','Haryana','Telangana','Kerala','Karnataka']
# print(type(city))   ### output- class list
# print(len(city))    ### output- 5

###=====================================================================
##(2)To clear given list
# city=['Maharashtra','Haryana','Telangana','Kerala','Karnataka']
# print(city.clear())    ## using clear gives output as none

##======================================================================
##(3)To copy the list
# dish=['poha','dosa','idli','coffee']
# print(dish)
# breakfast=dish.copy()   ### new list created with elements present in old list
# print(breakfast)

###=====================================================================
##(4)To count occurences of element in given list
# marks=[23,45,32,78,76,32,55,32]
# print(marks.count(32))     ### gives count of 32 as==3

###======================================================================
##(5)To check presence of element in given list
# candidate=['saurabh','sawan','priya','bhausaheb']
# if 'bhausaheb' in candidate:
#     print("Element Exist")
# else:
#     print("Element dose not Exist")  ### output-Element Exist

###========================================================================
##(6) To swap first and last element in the list
# city=['mumbai','pune','nagpur','nashik','aurangabad']
# print('list before swap',city)  ###['mumbai', 'pune', 'nagpur', 'nashik', 'aurangabad']
# city[0],city[4]=city[4],city[0]
# print('list after swap',city)   ###['aurangabad', 'pune', 'nagpur', 'nashik', 'mumbai']

###=============================================================================
##(7) To swap any two element in the list
#num=[23,56,78,44,12,90]
#print("List before swap",num)   ###[23, 56, 78, 44, 12, 90]
#num[0],num[5]=num[5],num[0]
#print("List after swap",num)  ###[90, 56, 78, 44, 12, 23]
#print(num.sort())
###=============================================================================
##(8) To find sum all element in the list
# num=[34,12,67,99,88]
# sum=0
# for x in range(0,len(num)):
#     sum=sum+num[x]
# print('Sum of elements in given list:',sum)     ### Sum of elements in given list: 300
###============================================================================= 
##(9)To find max and min element in the array
# array=[11,22,33,44]
# print("maximum Element in array:",max(array),"Minimum Element in array:",min(array)) ### 44 AND 11
###================================================================================
##(10) To find sum all element in the array
# array=[11,22,33,44]
# print(sum(array))   ### 110

###=================================================================================
##(11) To multiply all element in the list
# list=[4,5,6,7]
# print(list[0]*list[1]*list[2]*list[3]) ### output-840
# prod=1
# for x in range(0,len(list)):
#     prod=prod*list[x]
# print('multiplication',prod)          ### output-840
###===================================================================================
##(12) To swap two numbers
# a=5
# b=9
# c=a+b
# b=c-b
# a=c-b
# print('a:',a,'b:',b)   ### a: 9 b: 5

###=====================================================================================
##(13) To find smallest and largest number in given list
# number=[54,76,63,88,47]
# print('largest number:',max(number),'smallest number:',min(number))  ###88 and 47

###=======================================================================================
##(14) To find substring in string
# message="HELLO INNOVANT"
# print(message.find("VANT"))   ### OUTPUT-10
 
###=========================================================================================
##(15) To find length of given string
# oath='India is Democratic Country'
# print(len(oath))              ### OUTPUT-27

###==========================================================================================
##(17) To remove nth occurence in given word list
# twister=['she','sells','sea','shells','by','the','sea','shore']
# word='sea'
# n=2
# count=0
# for i in range(0,len(twister)-1):
#     if(twister[i]==word):
#         count=count+1
#         if(count==n):
#          twister.pop(i)
# print('NEW TWISTER:',twister)  ###NEW TWISTER: ['she', 'sells', 'sea', 'shells', 'by', 'the', 'shore']          

###=============================================================================================
##(18) To reverse words in given string
# text='my name is saurabh'
# dec=text.split(' ')
# print("Old string:",dec)  ###['my', 'name', 'is', 'saurabh']
# dec=dec[-1::-1]
# print("New Reversed string:",dec)   ###['saurabh', 'is', 'name', 'my']

###=================================================================================================
##(19) To check whether given string is palandrome or not
# x=input("Enter a Word:")   ### MALYALAM
# print(x)
# rev=(x[::-1])
# if rev==x:
#     print("Given Word is Palandrome")
# else:
#     print("Given Word is NOT Palandrome")   ##MALYALAM IS NOT PALANDROME  

###==========================================================================================
##(20) To reverse elements in list
# salary=[10000,12000,18000,23000]
# print("salary before reverse:",salary)   ###[10000, 12000, 18000, 23000]
# salary.reverse()
# print("salary after reverse:",salary)    ###[23000, 18000, 12000, 10000]

###============================================================================================
##(21) To find second highest elements in list
# salary=[55000,12000,18000,23000]
# salary.sort()
# print("second highest salary:",salary[-2])   #### second highest salary: 23000

###=============================================================================================
##(22) To find factorial
x=int(input("Enter the Number"))
count=0
result=1
while x>count:
    fact=x*result
    x=x-1
print("factorial of given number:",fact)    
# #employeeList = [
#                 [101, 'Priya', '6667434'],
#                 [102, 'Manoj', '452'],
#                 [103, 'Saurabh', '24344'],
#                 [104, 'Savan', '008855'],
#                 [105, 'Komal', '76622'],
#                 [106, 'Namrata', '98988']
#                ]

# #print(employeeList[2])

# # print(employeeList[0][0] == 103)    #False
# # print(employeeList[1][0] == 103)    #False
# # print(employeeList[2][0] == 103)    #True
# # print(employeeList[3][0] == 103)    #False

Innovantlist={  
              101:['saurabh','solapur','986754321'],
              102:['savan','phaltan','9866554433'],
              103:['priya','nashik','877665432']
                }
##print(Innovantlist)
#print(Innovantlist.items())  ### displays keys and value in given dictionary
#print(Innovantlist.keys())  ### displays keys in given dictionary
# result=Innovantlist.update({104:['kiya','baghdad','765543689']})
# print(f"updated dictionary{Innovantlist}:{result}")  ## new value can be added or old can be updated
print(Innovantlist.get(102)) ## it is used to display values associated with the specific key

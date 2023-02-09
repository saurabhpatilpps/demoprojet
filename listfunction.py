cities=['pune', 'solapur', 'mumbai', 'nanded', 'alibag', 'sillod']
# print(type(cities)) ##<class 'list'>
# print(len(cities))  ##6  

# print(f"list before sort{cities}")  ##['pune', 'solapur', 'mumbai', 'nanded', 'alibag', 'sillod']
# k=cities.sort()
# print(f"result after sort{cities}:{k}")  ##['alibag', 'mumbai', 'nanded', 'pune', 'sillod', 'solapur']:None

# print(f"list before sort{cities}")  ##['pune', 'solapur', 'mumbai', 'nanded', 'alibag', 'sillod']
# k=cities.sort(reverse=True)
# print(f"result after sort{cities}:{k}")  ##['solapur', 'sillod', 'pune', 'nanded', 'mumbai', 'alibag']:None

# print(f"list before reverse{cities}")   ##['pune', 'solapur', 'mumbai', 'nanded', 'alibag', 'sillod']
# z=cities.reverse()
# print(f"list after reverse{cities}:{z}") ##['sillod', 'alibag', 'nanded', 'mumbai', 'solapur', 'pune']:None

# print(f"list before append {cities}") ##['pune', 'solapur', 'mumbai', 'nanded', 'alibag', 'sillod']
# q=cities.append('islamabad')
# print(f"list after append{cities}:{q}")  ##['pune', 'solapur', 'mumbai', 'nanded', 'alibag', 'sillod', 'islamabad']:None

#print(f"list before insert {cities}")  ##['pune', 'solapur', 'mumbai', 'nanded', 'alibag', 'sillod']
# x=cities.insert(3,'parbhani')
# print(f"list after insert{cities}:{x}")  ##['pune', 'solapur', 'mumbai', 'parbhani', 'nanded', 'alibag', 'sillod']:None

#x=cities.insert(1000,'egypt')
#print(f"list after insert{cities}:{x}") ## in this case EGYPT will take append operation and value will add at the end

#print(f"list before pop{cities}")  ##['pune', 'solapur', 'mumbai', 'nanded', 'alibag', 'sillod', 'egypt']
#t=cities.pop()
#print(f"list after pop{cities}:{t}")  ## is nothing is mentioned then last value is deleted and resullt shows deleted value
t=cities.pop(3)
#print(f"list after pop{cities}:{t}")   ## nanded is popped

# print(f"list before remove{cities}") ##r['pune', 'solapur', 'mumbai', 'alibag', 'sillod']
# VV=cities.remove('sillod')
# print(f"list after remove{cities}:{VV}")  ##remove['pune', 'solapur', 'mumbai', 'alibag', 'sillod']:NONE

print(f"list before count{cities}")
ss=cities.count('pune')
print(f"list after count{cities}:{ss}")
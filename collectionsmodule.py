import collections
# counter
# mylist=["A", "B", "D", "E", "F", "G", "A", "D", "C", "E"]
# result=collections.Counter(mylist)
# print(result)

# ordered dict
# dict=collections.OrderedDict()
# dict["a"]=1
# dict["b"]=2
# dict["c"]=3
# dict["d"]=4
# dict["e"]=5
# dict["f"]=6
# dict.pop("a")
# dict["a"]=1
# for i ,j in dict.items():
#     print(i,j)

# default  dict 
# dict=collections.defaultdict(int)
# list=[1,2,3,4,5,1,2,3,4,8,9]
# for i in list:
#     dict[i]+=i
# print(dict)

# chainmap
# dict={"name":"keerthana","age":21}
# mydict={"course":"java","course":"python"}
# result=collections.ChainMap(dict,mydict)
# print(result)

# namedtuple
# employee=collections.namedtuple("employee",["name","age"])
# emp=employee("keerthana",21)
# print(emp[1])

# deque
mydeque=collections.deque([1,2,3,4,5])
mydeque.appendleft(3)
print(mydeque)
mydeque.append(2)
print(mydeque)
mydeque.pop()
print(mydeque)
mydeque.popleft()
print(mydeque)
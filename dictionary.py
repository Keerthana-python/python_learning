# mydict={"name":"keerthana",
#         "ae":24,
#         "course":"python"
#         }
# print(type(mydict))

# nested dictionary
company={
    "employe 1":{
    "emply name":"keerthana",
    "emply no":1111,
    "emply code":"aaaa"
    },
    "employe 2":{
    "emply name":"geetha",
    "emply no":2222,
    "emply code":"bbbb"
    },
    "employe 3":{
    "emply name":"narmatha",
    "emply no":3333,
    "emply code":"cccc"
    },
    "employe 4":{
    "emply name":"giri",
    "emply no":4444,
    "emply code":"dddd"
    },
    "employe 5":{
    "emply name":"ram",
    "emply no":5555,
    "emply code":"eeee"
    },
}
# print(company)

for i,j in company.items():
    print(i)
    for k in j:
        print(k,j[k])



# def new_func():
#     address = input('Please Enter The Address\n')
#     print(address)
#     x = address.split(',')
#     z = []
#     w = ''
#     for i in x:
#         if i in z:
#             z.append('NA')
#         else:
#             z.append(i)
#     print(z)
#     print('Output Address')
#     w = ''
#     for j in z:
#         print(j)
#         w = w +' '+ j
    
#     return print(w) 
# new_func()
# address = input('Enter Your Address\n')
# address = address.lower()
# splits = address.split(',')
# print(splits)
# z = []
# for i in splits:
#     if i not in z:
#         z.append(i)
# print(z)

# length = len(z)

# if length == 7:
#     house = z[0]
#     landmark = z[1]
#     area = z[2]
#     city = z[3]
#     district = z[4]
#     state = z[5]
#     pincode = z[6]
# elif length == 6:
#     house = z[0]
#     if 'near'or'opposite'or'besides'or'infront'or'in front'or'b/h'or'behind'or'nr'or'nr.' in z[1]:
#         landmark = z[1]
#         area = 'NULL'
#     else:
#         landmark='NULL'
#         area = z[1] 
#     city = z[2]
#     district = z[3]
#     state = z[4]
#     pincode = z[5]
# elif length == 5:
#     house = z[0]
#     landmark = 'NULL'
#     area = 'NULL'
#     city = z[1]
#     district = z[2]
#     state = z[3]
#     pincode = z[4]
# elif length == 4:
#     house = z[0]
#     landmark = 'NULL'
#     area = 'NULL'
#     city = 'NULL'
#     district = z[1]
#     state = z[2]
#     pincode = z[3] 
# elif length == 3:
#     house = z[0]
#     landmark = 'NULL'
#     area = 'NULL'
#     city = 'NULL'
#     district = 'NULL'
#     state = z[1]
#     pincode = z[2] 

# print(house, landmark, area, city, district,state,pincode)

# z = "380050"
# w = z.isnumeric()
# if w == True:
#     x = z
#     print(x)
# else:
#     x = 'NULL'
s1 = "hello world"
# # # length of the string

# # print(s1)
# # print(len(s1))


# #indexing
# print("first character", s1[0])
# print("last character", s1[-1])


# Syntax of indexing: string[index] 
# Syntax of slicing: srting[start:end:step]

#print(s1[:5])
#print(s1[6:])
#print(s1[1:5])
#print(s1[0:5])
#print(s1[0:5:1])
#print(s1[0:5:2])
#print(s1[0:11:1])
#print(s1[0:11:2])
#print(s1[0:11:3])
#print(s1[0:11:4])

"""
 0    1.   2    3.    4.    5    6.     7.    8    9
-10  -9   -8   -7    -6    -5    -4    -3    -2   -1
"""
# same wahi sab kuch kaam karte hai bss ulta negative numbring karni hai

#for reverse the string
print(s1[ : :-1]) 


print(s1[-11: ])
print(s1[:])

s2 = "abcdefghijklmnopqrstuvwxyz"

part1 = s2[0::1]
part2 = s2[0::2]
part3 = s2[1::2]
print(f"{part1}\n{part2}\n{part3}")
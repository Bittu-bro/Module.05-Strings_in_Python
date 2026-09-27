a = 1
b = 2
c = a + b
print(c)




s1 = "python is fun"

# in /not in
print("python" in s1)
print("i" in s1)
print("z" in s1)
print("python" not in s1)
print("i" not in s1)
print("z" not in s1)
print("java" not in s1)


# Comparison of strings ("==")
print("   Python" == "   Python")


#in string, '*' is repeatition operator 
print("Python" * 3)


##removing space from a string whose persent ii th last or start of string - ("strip")
s1 = "          Python             "
s2 = s1.strip() 
s2 = s1.strip() == "Python"
print(s2)


# replace()

ss = "we are learning Python"
print(ss)
print(ss.replace("Python","Java"))
print(ss.replace("e","E",2))
#counting substring from a string using "count()"
#count()
#string.count(substring)


s1 = """I\'m so fine shit, fine shit, fine shit, fine shit, fine shit, fine shit.
Yeah, you so fine shit, fine shit, fine shit, fine shit, fine shit, fine shit."""
print(s1.count("fine"))
print(f"occurrences of fine is {s1.count("fine")} Times.")
print(f"occurrences of shit is {s1.count("shit")} Times.")


#changing case of a string
#upper(), lower(), title(), capatilize()
s1 = "We are learing Python,It's fun."


print(s1.lower())
print(s1.upper())
print(s1.title())
print(s1.capitalize())


#Starting and ending of a string
s1 = "we are learning python"


print(s1.startswith("w"))
print(s1.startswith("W"))
print(s1.startswith("j"))
print(s1.startswith("we"))
print(s1.startswith("We"))
print(s1.startswith("java"))
print(s1.endswith("w"))
print(s1.endswith("W"))
print(s1.endswith("n"))
print(s1.endswith("we"))
print(s1.endswith("We"))
print(s1.endswith("python"))


print("       Bittu     ".strip())
print("       Bittu     ".lstrip())
print("       Bittu     ".rstrip())
print("       Bittu     ".replace("B", "T"))


s = "Hello gyus Hello Hello"
s = s.replace("Hello", "Hi", 2)
s.replace("Hello", "Hi")
print(s)
# Strings are immutable
a = "AnveshMangalam!!!!"
a1 = "ANVESH MANGALAM"
print(len(a))
# upper is used to all string changes into uppercase
print(a.upper())
# all string changes into lowercase
print(a1.lower())
print(a.rstrip("!"))
# it replaces the string
print(a.replace("Mangalam","Kulshrestha"))
#  it Capitalize the first word of the sentence
blog = "introduction to python"
print(blog.capitalize())
print(blog.upper())
# center gives the spaces in the begning
print(a.center(50))
# it counts the alphabet in the sentence
print(blog.count("o"))


str1= "Welcome to the World of Python !!!"
# ittells the sentence ends with
print(str1.endswith("!!!"))
# it finds the particular word in the whole sentence
print(str1.find("of"))

str2 = "WelcomeToTheConsole"
print(str2.isalnum())
print(str2.isalpha())
print(str2.islower())
print(str2.isupper())
print(str2.isprintable())

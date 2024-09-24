letter = "Hello my name is {} and I am from {}"
country = "India"
name = "Anvesh"
print(letter.format(name,country))
print(f"Hello my name is {name} and I am from {country}")

# Another Example

price = 99.0099988
txt = f"For only {price:.2f} dollars!"
print(txt)
print((f"{2*30}"))
print(type(f"{2*30}"))
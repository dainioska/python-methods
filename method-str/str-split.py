# str.split(separator, maxsplit)

txt = "Hello! , myname is Jon!, I am 26 years old"
txt1 ="   alio hello\n123, bum\\n999"

print(txt.split())
print(txt.split(", "))
print(txt.split("!"))
print(txt.split("!", 1))
print(txt1.split("\n"))
# str.splitlines([keepends])

string1 = "Tim\nCharlie\nJohn\nAlan"
string2 = "Wellcome\n\n\to\r\nAskPython\t!"
string3 = "Keyboard\u2028monitor\u2029\x1cMouse\x0cCPU\x85Motherb\x1eSpeakers\r\nUPS"

print(string1.splitlines())
print(string2.splitlines())
print(string3.splitlines())

print(string1.splitlines(keepends=True))
print(string2.splitlines(keepends=True))
print(string3.splitlines(keepends=True))

# \n line feed
# \r carriage return
# \r\n carriage return+line feed
# \v or \x0b line tab
# \f or x0c form feed
# \x1c file separator
# \x1d group separator
# \x1e record separator
# \x85 next line
# \u2028 line separator
# u\2029 paragraph separator
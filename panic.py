phrase = "Don't panic"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.remove('D')
plist.remove('\'')
plist.remove(' ')
plist.insert(2,' ')
plist.insert(4,'a')
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)



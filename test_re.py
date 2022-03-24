import re

# p = re.compile('[a-z]+')
# m = re.match( '[a-z]+','string goes here' )

# if m:
#     print('Match found: ', m.group())
# else:
#     print('No match')

# result = p.findall("life is too short")
# print(result)

# result = p.finditer("life is too short")
# for r in result:
#     print(r)

p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(data)

# print(p.findall(data))
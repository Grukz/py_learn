#group(0) == group()

import re

result = re.search("[a-z]\d", "a1b2c3")
print result
print result.group()
print result.groups()
print

result = re.search("[a-z]\d", " a1b2c3")
print result
print result.group()
print

result = re.match("[a-z]\d", "a1b2c3")
print result
print result.group()
print

result = re.match("[a-z]\d", " a1b2c3")
print result
print

result = re.findall("[a-z]\d", "a1b2c3")
print result
print '*' * 30

mo = re.search("([0-9]+)+", "Customer number: 232454, Date: February 12, 2011")
print mo.group()
print mo.groups()
print

result = re.match(".*", " a1b2c3")
print result
print result.group()
print result.groups()
print

result = re.match("..*?", "a1b2c3")
print result
print result.group()
print result.groups()
print

result = re.match("(...)*", "ttta1b2c3f")
print result
print result.group()
print result.groups()
print

result = re.match("(...)(...)(...)", "ttta1b2c3f")
print result
print result.group()
print result.groups()
print '*' * 30

result = re.match("(t..)*", "txxtyy2c3f")
print result
print result.group()
print result.groups()
print

result = re.match("(t..)*", "txxbtyy2c3f")
print result
print result.group()
print result.groups()
print

result = re.match("(...)+?", "ttta1b2c3f")
print result
print result.group(0)
print result.group()
print result.groups()
print '*' * 30

result = re.match("\s*(\d+)\s*(\w*)\s*-\s*(\d+)\s*(\w+)\s*", " 0 - 12 M ")
result = re.match("\s*(\d+)\s*(\w*)\s*-\s*(\d+)\s*(\w+)\s*", " 0 M - 12 M ")
print result
if result:
    print result.group()
    print result.groups()
print '*' * 30

import re

message = 'Call me 415-555-1011 tommorrow, or at 415-555-9999'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
for mo in phoneNumRegex.finditer(message):
    print(mo.group(1))
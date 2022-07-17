import re


# ================================== 1 ======================================
pattern = r"[+\d]{1,3}-[\d]{2,4}-[\d]{2,4}"
text = "Hello, my phone number is 251-6543-2343."
rez = re.findall(pattern=pattern, string=text)

if rez:
    print("match received")
else:
    print("no matches found")

print(rez)


# ================================== 2 ======================================
pattern = r"(\b[A-Za-z0-9._%/+-]{1,255})+@([A-Za-z0-9]+.[A-Z|a-z]{2,255}\b)"
text = "tsapyura1999@gmail.com"
rez = re.match(pattern=pattern, string=text)

if rez:
    print("match received")
else:
    print("no matches found")

print(rez.groups())

# ================================== 3 ======================================

pattern = r'\.[0]*'
text = "120.008.009.196"
rez = re.sub(pattern=pattern, repl=".", string=text)

if rez:
    print("match received!")
else:
    print("no matches found")

print(rez)

# ================================== 4 ======================================

pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
text = "153.192.198.84"
rez = re.match(pattern=pattern, string=text)

if rez:
    print("match received")
else:
    print("no matches found")

print(rez)

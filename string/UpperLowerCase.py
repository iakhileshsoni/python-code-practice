# Alternate case (UPPER & lower) of String

str = "akhilesh"
res = ""
for i in range(len(str)):
    if not i % 2:      #  if i % 2: aKhIlEsH
        res = res + str[i].capitalize()
    else:
        res = res + str[i].lower()

print("String after alternate case : ", res)   # AkHiLeSh
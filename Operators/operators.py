a, b, c = "akhil", "kumar", "Soni"
new_var = a + " " + b + " " + c
print(new_var)          # akhil kumar Soni
print(type(new_var))    # <class 'str'>

l1 = ["akhil", "kumar", "Soni"]
l2 = " ".join(l1)
print(l2)               # akhil kumar Soni
print(type(l2))         # <class 'str'>
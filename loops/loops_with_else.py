
""" loops with else """

""" 
    If loop executed successfully without break then only else part will be executed. In other words, 
    if break is not encountered inside the loop then else part will be executed
    
"""

cart = [10, 20, 30]

for item in cart:
    if item > 500:
        print("We can't process this item. You need to have insurance for processing this item")
        break
    print("Processing your item")
else:
    print("Congratulations! Your all items processed successfully")
print("\n")


"""
Output:

Processing your item
Processing your item
Processing your item
Congratulations! Your all items processed successfully

Here,  if statement is not True so break will never be executed. Hence else part will be executed after print inside the for
"""



"""  

continue with else : It is no where related because else will only/always be executed if there is no break whether we use continue
or not. else is meaningful with break not with continue. In fact if we're using continue then also else will always be executed.

"""

cart = [10, 20, 600, 30]

for item in cart:
    if item > 500:
        print("We can't process this item for {} amount. You need to have insurance for processing this item of  {}".format(item, item))
        continue
    print("Processing your item")
else:
    print("Congratulations! Your all items processed successfully")
print("\n")


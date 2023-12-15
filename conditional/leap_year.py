
"""
Leap Year:
A leap year is exactly divisible by 4 except for century years (years ending with 00).
The century year is a leap year only if it is perfectly divisible by 400.
For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600, 2000 and 2012, 2024 are.

"""
# Method-1
print(1700%100)
# def LeapYear(year):
#     """
#     Here, there is 2 conditions which are as
#       1. (year % 4 == 0 and year % 100 != 0)
#       2. (year % 400 == 0)
#     In some cases it might be possible that year is divisible by 4 but not by 100 then 1st condition will be False.
#     In that situation we can go for 2nd condition if year is divisible by 400, if it is, then in that case also year
#     would be leap year. For ex. 2024.
#
#     2024 is divisible by 4 but not by 100 then 1st condition is True. Even though it's not divisible by 400 also,
#     it means that 2nd condition is False but, it's in OR condition, so we'll check only 1st Condition
#     """

#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return "Leap Year"
#     else:
#         return "Not a leap year"
#
# print(LeapYear(2024))


# Method-2

# def LeapYear(year):
#     # If divided by 100 then Century Year and if divided by 400 then Leap Year
#     if (year % 100 == 0) and (year % 400 == 0):
#         print("{0} is Leap Year".format(year))
#     # If divided by 100 then Century Year and if divided by 4 then Leap Year
#     elif (year % 100 == 0) and (year % 4 == 0):
#         print("{0} is Leap Year".format(year))
#     else:
#         print("{0} is not a Leap Year".format(year))
#
# LeapYear(1900)


Year= int(input("Enter a year: "))
if Year%4 == 0 and Year%100 != 0:
    print("It's a leap Year")
else:
    print("It's not a leap year")


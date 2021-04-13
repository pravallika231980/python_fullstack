# # def is_leap(year):
# #     leap = False
# #     if(year%4)==0 and (year%100)==0 and (year%400)==0:
# #         return True
# #     else:
# #         return leap
# #
# # year = int(input("enter the year:"))
# # print(is_leap(year))
# def is_leap(year):
#     leap = False
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 return True
#             else:
#                 return leap
#         else:
#             return leap
#     else:
#         return leap
#
#
# year = int(input("enter the year:"))
# print(is_leap(year))
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
year = int(input("enter the year:"))
print(is_leap(year))

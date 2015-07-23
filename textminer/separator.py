import re

# @xfail
# @params("input,expected", [
#     ("hello", ['hello']),
#     ("hello world", ['hello', 'world']),
#     ("raggggg hammer dog", ['raggggg', 'hammer', 'dog']),
#     ("18-wheeler tarbox", ['18-wheeler', 'tarbox']),
#     ("12", None),
# ])

def words(input):
    input_list = input.split(' ')
    print(input_list)
    return input_list


# @xfail
# @params("input,expected", [
#     ("919-555-1212", {"area_code": "919", "number": "555-1212"}),
#     ("(919) 555-1212", {"area_code": "919", "number": "555-1212"}),
#     ("9195551212", {"area_code": "919", "number": "555-1212"}),
#     ("919.555.1212", {"area_code": "919", "number": "555-1212"}),
#     ("919 555-1212", {"area_code": "919", "number": "555-1212"}),
#     ("555-121", None)
# ])

#def phone_number(input):


#
# @xfail
# @params("input,expected", [
#     ("$4", {"currency": "$", "amount": 4.0}),
#     ("$19", {"currency": "$", "amount": 19.0}),
#     ("$19.00", {"currency": "$", "amount": 19.0}),
#     ("$3.58", {"currency": "$", "amount": 3.58}),
#     ("$1000", {"currency": "$", "amount": 1000.0}),
#     ("$1000.00", {"currency": "$", "amount": 1000.0}),
#     ("$1,000", {"currency": "$", "amount": 1000.0}),
#     ("$1,000.00", {"currency": "$", "amount": 1000.0}),
#     ("$5,555,555", {"currency": "$", "amount": 5555555.0}),
#     ("$5,555,555.55", {"currency": "$", "amount": 5555555.55}),
#     ("$45,555,555.55", {"currency": "$", "amount": 45555555.55}),
#     ("$456,555,555.55", {"currency": "$", "amount": 456555555.55}),
#     ("$1234567.89", {"currency": "$", "amount": 1234567.89}),
#     ("$12,34", None),
#     ("$1234.9", None),
#     ("$1234.999", None),
#     ("$", None),
#     ("31", None),
#     ("$$31", None),
# ])

#def money(input):
    # """We are just concerned with dollars here for now but might take other
#    currencies later."""


# @xfail
# @params("input,expected", [
#     ("63936", {"zip": "63936", "plus4": None}),
#     ("50583", {"zip": "50583", "plus4": None}),
#     ("06399", {"zip": "06399", "plus4": None}),
#     ("26433-3235", {"zip": "26433", "plus4": "3235"}),
#     ("64100-6308", {"zip": "64100", "plus4": "6308"}),
#     ("7952", None),
#     ("115761", None),
#     ("60377-331", None),
#     ("8029-3924", None),
# ])

#def zipcode(input):



# @xfail
# @params("input,expected", [
#     ("9/4/1976", {"month": 9, "day": 4, "year": 1976}),
#     ("1976-09-04", {"month": 9, "day": 4, "year": 1976}),
#     ("2015-01-01", {"month": 1, "day": 1, "year": 2015}),
#     ("02/15/2004", {"month": 2, "day": 15, "year": 2004}),
#     ("9/4", None),
#     ("2015", None),
# ])

#def date(input):

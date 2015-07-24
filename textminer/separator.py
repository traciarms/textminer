import re


def words(input):
    input_list = re.findall(r'\b[A-z0-9\-]*[A-z]+', input)

    if len(input_list) == 0:
        return None
    else:
        return input_list


def phone_number(input):
    phone = re.search(r"(?:\(?(\d{3})+\)?[\-\.]?\s*)?(\d{3})[\-\.]?(\d{4})",
                      input)

    if phone == None:
        return None
    else:
        r_dict = {}
        r_dict["area_code"] = phone.group(1)
        r_dict["number"] = "{}-{}".format(phone.group(2), phone.group(3))
        return r_dict


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

def money(input):
    """We are just concerned with dollars here for now but might take other
   currencies later."""
    money = re.match(r'(\${1})((\d{1,3})+,\d{3}?\.\d{2})?', input)

    # print(money.string)
    # print(money.group())
    # print(money.groups())

    if money == None:
        return None
    else:
        r_dict = {}
        r_dict["currency"] = money.group(0)

        print(money.string)
        print('the group 1 {}'.format(money.groups()))
        r_dict["amount"] = money.string.replace('$','')
        mystring = float(r_dict["amount"].replace(',', ''))
        r_dict["amount"] = mystring

        print(r_dict)
        return r_dict

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

if __name__ == '__main__':

    money("$19")
    money("$19.00")
    money("$3.58")
    money("$5,555,555.55")
    money("$$31")

import re


def words(word):
    input_list = re.findall(r'\b[A-z0-9\-]*[A-z]+', word)

    if 0 == len(input_list):
        return None
    else:
        return input_list


def phone_number(num):
    phone = re.search(r"(?:\(?(\d{3})+\)?[\-\.]?\s*)?(\d{3})[\-\.]?(\d{4})",
                      num)

    if phone is None:
        return None
    else:
        r_dict = {"area_code": phone.group(1),
                  "number": "{}-{}".format(phone.group(2), phone.group(3))}
        return r_dict


def money(mon):
    """We are just concerned with dollars here for now but might take other
        currencies later."""
    money = re.search(r'(\${1})(\d+(?:\,?\d{3})*(?:\.?\d{2})*)',
                      mon)

    if money is None:
        return None
    else:

        r_dict = {"currency": money.groups(0)[0], "amount": money.groups()[1]}

        if len(mon) != (len(money.groups()[1]) + 1):
            return None

        mystring = float(r_dict["amount"].replace(',', ''))
        r_dict["amount"] = mystring

        return r_dict


def zipcode(code):
    zipcode = re.search(r'^(\d{5})(\-?\d{4})?$', code)

    if zipcode is None:
        return None
    else:

        r_dict = {"zip": zipcode.groups(0)[0]}
        if zipcode.groups()[1] is not None:
            r_dict["plus4"] = zipcode.groups()[1].replace('-', '')
        else:
            r_dict["plus4"] = None

    return r_dict


def date(input):
    date = re.search(r'(\d{1,4})[\-/]{1}(\d{1,2})[\-/]{1}(\d{2,4})', input)

    if date is None:
        return None
    else:

        r_dict = {}
        if len(date.groups(0)[0]) < 4:
            r_dict["month"] = int(date.groups(0)[0])
            r_dict["year"] = int(date.groups(0)[2])
            r_dict["day"] = int(date.groups()[1])
        else:
            r_dict["year"] = int(date.groups(0)[0])
            r_dict["month"] = int(date.groups(0)[1])
            r_dict["day"] = int(date.groups()[2])

    return r_dict


if __name__ == '__main__':


    print('hello')

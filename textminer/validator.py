import re


def binary(num):
    """
       String must be a binary number
    """
    match = re.match(r'^[0-1]+$', num)
    if match:
        return True
    else:
        return False


def binary_even(num):
    """String must be a binary number and be even."""
    match = re.match(r'^[0-1]+[0]$', num)
    if match:
        return True
    else:
        return False

def hex(num):
    match = re.match(r'^[\dA-Fa-f]+$', num)
    if match:
        return True
    else:
        return False

def word(word):
    match = re.findall(r'^[A-z0-9\-]+[A-z]+$', word)

    if match:
        return True
    else:
        return False

def words(words, count=0):
    """
        words can take an optional count argument. In case it exists, the text
        must match that number of words.
    """
    words_list = words.split(' ')
    cnt = len(words_list)
    if cnt > 0:
        words_list = words.split(' ')
        for each in words_list:
            match = word(each)

    else:
        match = word(words)

    if count == 0 or cnt == count:
        return match
    else:
        return False


def phone_number(phone_num):
    """US phone numbers only."""
    match = re.search(r'^[\(]?[0-9]{3}[\-\)\.\s]?[\s]?[0-9]{3}'
                      r'[\-\.\s]?[0-9]{4}$',
                      phone_num)

    if match:
        return True
    else:
        return False

def money(mon):
    """We are just concerned with dollars here."""
    match = re.search(r'^\${1}\d+(?:\,\d{3})?(?:\,\d{3})?(?:\.\d{2})?$', mon)

    print(match)
    if match:
        return True
    else:
        return False


def zipcode(zip):
    match = re.search(r'^\d{5}(?:\-\d{4})?$', zip)

    print(match)
    if match:
        return True
    else:
        return False

def date(date):
    match = re.search(r'^\d{1,4}[\-/]{1}\d{1,2}[\-/]{1}\d{2,4}$', date)

    print(match)
    if match:
        return True
    else:
        return False

# ## HARD MODE BEGINS

# def hard_date(date):
#     match = re.search(r'^\d{1,4}[\-/]{1}\d{1,2}[\-/]{1}\d{2,4}$', date)
#
#     print(match)
#     if match:
#         return True
#     else:
#         return False

    # assert v.date("2014 Jan 01")
    # assert v.date("2014 January 01")
    # assert v.date("Jan. 1, 2015")
    # assert not v.date("07/40/2015")
    # assert not v.date("02/30/2015")

#
# @xfail
# def test_email():
#     """Some of the emails listed as invalid are actually valid according to
#     the email spec, but we will not accept them."""
#
#     assert v.email("stroman.azariah@yahoo.com")
#     assert v.email("viola91@gmail.com")
#     assert v.email("eathel.west@example.org")
#     assert v.email("dwehner@harley.us")
#     assert v.email("malcolm.haley@hotmail.com")
#     assert v.email("ezzard90@hotmail.com")
#     assert v.email("legros.curley@gmail.com")
#     assert v.email("leatha75@mertz.net")
#     assert v.email("bonita43@yahoo.com")
#     assert not v.email("")
#     assert not v.email("legros.curley")
#     assert not v.email("mertz.net")
#     assert not v.email("bonita43@")
#
#
# @xfail
# def test_address():
#     """This must be a full address with street number, street, city, state,
#     and ZIP code. Again, US-only."""
#     assert v.address("""368 Agness Harbor
#     Port Mariah, MS 63293""")
#     assert v.address("""96762 Juluis Road Suite 392
#     Lake Imogenemouth, AK 20211""")
#     assert v.address("""671 Tawnya Island Apt. 526
#     Clementeburgh, AK 82652""")
#     assert v.address("""568 Eunice Shoals
#     Parishaven, AK 09922-2288""")
#     assert v.address("8264 Schamberger Spring, Jordanside, MT 98833-0997")
#
#     assert not v.address("")
#     assert not v.address("99132 Kaylah Union Suite 301")
#     assert not v.address("Lake Joellville, NH")
#     assert not v.address("35981")

if __name__ == '__main__':


    print('hello')
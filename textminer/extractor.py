import re


def phone_numbers(text):
    return re.findall(r'[\(]?[0-9]{3}[\-\)\.\s]?[\s]?[0-9]{3}'
                      r'[\-\.\s]?[0-9]{4}', text)

def emails(em):
    return re.findall(r'[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!'
                      r'# #$%&\'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*'
                      r'[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?', em)


if __name__ == '__main__':

    print('hello')
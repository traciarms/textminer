import re


def phone_numbers(text):
    # print(text)
    text_list = text.split('\n')
    # poss_phone = [possibility
    #                 for possibility in text_list
    #                     if re.search(r'^[\(]?[0-9]{3}[\-\)\.\s]?[\s]?[0-9]{3}'
    #                                  r'[\-\.\s]?[0-9]{4}$', possibility)]

    poss_phone = []
    match = []
    for poss in text_list:
        print('the poss is {}'.format(poss))
        #match = re.findall(r'^[\(]?[0-9]{3}[\-\)\.\s]?[\s]?[0-9]{3}'
        #                   r'[\-\.\s]?[0-9]{4}$', poss)

        print(match)
        if match:
            poss_phone.append(match.string)

    return poss_phone

if __name__ == '__main__':

    print('hello')
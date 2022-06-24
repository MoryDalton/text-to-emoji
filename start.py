from A_Z import text_to_emoji
from string import ascii_uppercase


def check_text():

    text = input('text:').upper()

    for item in text:
        if item not in ascii_uppercase:

            print('invalid text')
            return check_text()

    elm = input('element:')

    if len(elm) > 1:

        print('invalid element')
        return check_text()

    return text_to_emoji(text, elm)


if __name__ == ('__main__'):
    print(type(check_text()))

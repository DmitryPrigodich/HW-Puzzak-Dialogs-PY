import constants

def write_to_file(value):
    try:
        with open(constants.OUTPUT, 'a', encoding='utf-8') as file:
            file.write(value)
    except IOError as e:
        print(f'Error: {e}')

def write_line_to_file(value):
    try:
        with open(constants.OUTPUT, 'a', encoding='utf-8') as file:
            file.writelines(value)
    except IOError as e:
        print(f'Error: {e}')
def rewrite_file(value, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(value)
    except IOError as e:
        print(f'Error: {e}')

def add_to_file(value, file_name):
    try:
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(value)
    except IOError as e:
        print(f'Error: {e}')

def wait_a_bit(page):
    page.wait_for_timeout(2000)
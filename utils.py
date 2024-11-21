import json

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

def write_json(data_to_record, file_to_create):
    json_data = json.dumps(data_to_record, ensure_ascii=False)
    rewrite_file(json_data, file_to_create)

def create_lowercase_key_map(d):
    return {k.lower(): k for k in d}
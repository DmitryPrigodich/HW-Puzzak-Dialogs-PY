def write_in_file(value):
    try:
        with open('OUTPUT.md', 'a', encoding='utf-8') as file:
            # file.writelines(value)
            file.write(value)
            file.write('\n')
    except IOError as e:
        print(f'Error: {e}')
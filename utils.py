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

def sort_dict_by_keys(my_dict: dict):
    return dict(sorted(my_dict.items()))

def get_corrected_faction_name(faction):
    match faction:
        case hiigaran if hiigaran in ["Hiigaran Territories","Hiigaran"] :
            return "Hiigaran Medea"
        case "DarkHiigaran":
            return "Hiigaran Kiithless"
        case iyatequa if iyatequa in ['Tr1','tr1_territories','tr1_territories_t3','tr1_territories_t4','tr1_territories_special']:
            return "Iyatequa"
        case cangacian if cangacian in ["P1","P1 Territories"]:
            return "Cangacian"
        case tanoch if tanoch in ["Tanoch Territories","Tanoch Territories T4"]:
            return "Tanoch"
        case "TanochChicuat":
            return "Tanoch Chicuat"
        case "TanochTecuban":
            return "Tanoch Tecuban"
        case "Tanoch Temple":
            return "Tanoch Temple Guards"
        case yaot if yaot ["Yaot Territories","yaot_territories_t4"]:
            return "Yaot"
        case amassari if amassari ["Amassari Territories"]:
            return "Amassari"
        case "Clan Territories":
            return "Clans"
        case _:
            return faction
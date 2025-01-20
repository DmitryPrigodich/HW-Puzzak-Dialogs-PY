import json
import re

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

def clean_file(file_name):
    rewrite_file("", file_name)


def write_json(json_input, json_output):
    json_data = json.dumps(json_input, ensure_ascii=False)
    rewrite_file(json_data, json_output)

def read_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        json_data = file.read()
    return json.loads(json_data)


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
        case yaot if yaot in ["Yaot Territories","yaot_territories_t4"]:
            return "Yaot"
        case amassari if amassari in ["Amassari Territories"]:
            return "Amassari"
        case tanoch if tanoch in ["Tanoch Territories","Tanoch Territories T4"]:
            return "Tanoch"
        case "TanochChicuat":
            return "Tanoch Chicuat"
        case "TanochTecuban":
            return "Tanoch Tecuban"
        case "Tanoch Temple":
            return "Tanoch Temple Guards"
        case "Clan Territories":
            return "None"
        case _:
            return faction
        
def remove_color(text):
    pattern = r"<color.*?</color>"
    clean_text = re.sub(pattern, "", text, flags=re.DOTALL)
    return clean_text.strip()


def format_heading1(title):
    return f"\n# {title}\n"

def format_heading2(title):
    return f"\n## {title}\n"

def format_heading3(title):
    return f"\n### {title}\n"

def format_heading4(title):
    return f"\n#### {title}\n"

def format_heading5(title):
    return f"\n##### {title}\n"

def format_heading6(title):
    return f"\n###### {title}\n"


def format_paragraph(text):
    return f"\n{text}\n"

def format_br(number):
    return "\n" * number

def format_indent(number):
    return "\t" * number

def format_bold(text):
    return f"**{text}**"

def format_caps(text):
    return text.upper()

def format_code(text):
    return f"`{text}`"

def format_code_block(text):
    return f"```\n{text}\n```"

def format_quote(text):
    return f"> {text}\n"

def format_note(text):
    return f"> [!NOTE]\n> {text}\n"

def format_tip(text):
    return f"> [!TIP]\n> {text}\n"

def format_important(text):
    return f"> [!IMPORTANT]\n> {text}\n"

def format_warning(text):
    return f"> [!WARNING]\n> {text}\n"

def format_caution(text):
    return f"> [!CAUTION]\n> {text}\n"
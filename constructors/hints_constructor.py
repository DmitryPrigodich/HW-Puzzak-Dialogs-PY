import utils
from .constructor_base import Constructor_Base

class Hint_Data_Constructor(Constructor_Base):
    _HINT_DATA_JSON = "json_bak/LoadingHintData-module.json"
    _FILE_NAME = "data/HINTS.md"
    _FILE_NAME_JSON = "json/hints.json"

    _hint_data = {}
    _hints = {}

    def __init__(self):
        super().__init__()
        self._hint_data = utils.read_json(self._HINT_DATA_JSON)
        self._set_data()

    def _set_data(self):
        for hint_header, hint_tags in self._hint_data.items():
            self._hints[hint_header] = {
                "Text:": self.get_string_by_key(hint_tags.get("LocaId:")),
                "Requirements:": hint_tags.get("Requirements:")
            }
    
    def write_json(self):
        utils.write_json(self._hints, self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM HINTS:\n"
        for hint_header, hint_params in self._hints.items():
            body += f"\n## {hint_header}\n"
            for h_param_key, h_param_value in hint_params.items():
                if h_param_value:
                    if h_param_key == "Text:":
                        h_param_value = h_param_value.replace("\\n","\n")
                        body += f"{h_param_value}\n"
                    if h_param_key == "Requirements:":
                        if len(h_param_value.split("\n")) > 1:
                            body += f"* **{h_param_key}**\n"
                            for qc_param in h_param_value.split("\n"):
                                body += f"\t* {qc_param}\n"
                        else:
                            body += f"* **{h_param_key}** {h_param_value}\n"
        utils.rewrite_file(body, self._FILE_NAME)
import utils
import re

from .constructor_base import Constructor_Base

class Dialog_Sequence_Constructor(Constructor_Base):
    _DIALOG_SEQUENCE_DATA_JSON = "dataset/json_bak/DialogSequenceData-module.json"

    _FILE_NAME = "dataset/data/DIALOGS.md"
    _FILE_NAME_JSON = "dataset/json/dialogs.json"

    _dialog_seqs_data = {}
    _dialogs = {}
    
    def __init__(self):
        super().__init__()
        self._dialog_seqs_data = utils.read_json(self._DIALOG_SEQUENCE_DATA_JSON)
        self._set_data()

    def _set_data(self):

        def _get_speaker_name(speaker_id):
            speaker_key = f"name_{speaker_id}".lower()
            speaker_name = self.get_string_by_key(speaker_key)

            if not speaker_name:
                speaker_name = f"{speaker_id} - speaker name not found"
                # print(speaker_name)

            return speaker_name

        def _get_dialog_string(dialog_id):
            dialog_key = dialog_id.lower()
            body_dialog = self.get_string_by_key(dialog_key)

            if not body_dialog:
                dialog_key = re.sub(r'_(\d+)$', r'_dia_\1', dialog_id)
                body_dialog = self.get_string_by_key(dialog_key)

                if not body_dialog:
                    body_dialog = f"dialog_id not found: {dialog_id}"
                    # print(body_dialog)
                
            return body_dialog

        for dialog_seq_header, dialog_seq in self._dialog_seqs_data.items():
            speaker_ids = dialog_seq["SpeakerIds:"].split(":")
            dialog_ids = dialog_seq["DialogIds:"].split(":")

            speakers_dialogs = []
            for index, (speaker_id, dialog_id) in enumerate(zip(speaker_ids, dialog_ids)):
                speakers_dialogs.append({
                    "Index:": index, 
                    "SpeakerId:": speaker_id,
                    "SpeakerName:": _get_speaker_name(speaker_id),
                    "DialogId:": dialog_id,
                    "DialogLine:": _get_dialog_string(dialog_id)
                    })

            self._dialogs[dialog_seq_header] = speakers_dialogs

    def get_data(self):
        return self._dialogs
    
    def write_json(self):
        utils.write_json(self._dialogs, self._FILE_NAME_JSON)
    
    def read_json(self):
        self._dialogs = utils.read_json(self._FILE_NAME_JSON)
        return self._dialogs

    def write_data(self):
        body = "# HWM DIALOGS\n\n"
        for dialog_seq_header, dialog_seq_list in self._dialogs.items():
            body += f"## {dialog_seq_header}\n\n".upper()

            for dialog in dialog_seq_list:
                body += f"### {dialog.get('SpeakerId:')}:{dialog.get('SpeakerName:')}\n"
                body += f"**{dialog['DialogId:']}**\n"
                body += f"{dialog['DialogLine:']}\n\n"

        utils.rewrite_file(body, self._FILE_NAME)

    
    def get_dialog_text(self, dialog_id):
        body_dialog = ""     

        if dialog_id == "Story-S2-01-Lighthouse_fail_dialog":
            print(f"Dialog id replaced: {dialog_id}")
            dialog_id = "Story-S2-01-Lighthouse_dialog_fail"

        if dialog_id == "st_hataldan_fail_2_dialog":
            print(f"Dialog id replaced: {dialog_id}")
            dialog_id = "s_hataldan_dialog_failKill"
            # s_hataldan_dialog_failKill -- not used
            # s_hataldan_dialog_failAmassari -- not used

        if dialog_id in self._dialogs:
            body_dialog += utils.format_br(1)
            body_dialog += utils.format_code(dialog_id)
            body_dialog += utils.format_br(1)

            for dialog_part in self._dialogs.get(dialog_id):
                speaker = dialog_part.get("SpeakerName:")
                dia_line = dialog_part.get("DialogLine:")

                body_dialog += utils.format_br(1)
                body_dialog += utils.format_bold(speaker)
                body_dialog += utils.format_br(1)
                body_dialog += utils.format_quote(dia_line)
            body_dialog += utils.format_br(2)

            return body_dialog
        
        elif dialog_id.startswith("qe_amaSum_2023"):
            # print(f"dialog id: {dialog_id}")
            prefix = dialog_id.lower().replace("qe_", "dia_").replace("2023","2024")
            prefix = re.sub(r'day(\d)(?!\d)', r'day0\1', prefix)    # day1 -> day01
            prefix = re.sub(r'_t\d_', '_', prefix)                  # _t(4) -> remove
            # print(f"Modified prefix: {prefix}")

            dia_str_values = []
            for key, value in self._string_data.items():
                if key.startswith(prefix):
                    dia_str_values.append(value.get("en:"))

            body_dialog += utils.format_br(1)
            body_dialog += utils.format_code(f"{dialog_id} / {prefix}")
            for dia_str_value in dia_str_values:
                body_dialog += utils.format_br(1)
                body_dialog += utils.format_quote(dia_str_value)
            body_dialog += utils.format_br(2)
            
            return body_dialog
        
        else:
            return None
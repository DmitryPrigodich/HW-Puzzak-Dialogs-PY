import utils
import re

from .constuctor_base import Constructor_Base

class Dialog_Sequence_Constructor(Constructor_Base):
    _DIALOG_SEQUENCE_DATA_JSON = "json_bak/DialogSequenceData-module.json"

    _FILE_NAME = "data/DIALOGS.md"
    _FILE_NAME_JSON = "json/dialogs.json"

    _FILE_NAME_STR = "data/DIALOGS_STRINGS.md"
    _FILE_NAME_STR_JSON = "json/dialogs_strings.json"

    _dialog_seqs_data = {}
    _dialogs = {}
    
    def __init__(self):
        super().__init__()
        self._dialog_seqs_data = self._read_json(self._DIALOG_SEQUENCE_DATA_JSON)

    def set_dialogs(self):
        for dialog_seq_header, dialog_seq in self._dialog_seqs_data.items():
            speaker_ids = dialog_seq["SpeakerIds:"].split(":")
            dialog_ids = dialog_seq["DialogIds:"].split(":")

            speakers_dialogs = []
            for index, (speaker_id, dialog_id) in enumerate(zip(speaker_ids, dialog_ids)):
                speakers_dialogs.append({"index": index, "speaker_id": speaker_id, "dialog_id": dialog_id})

            self._dialogs[dialog_seq_header] = speakers_dialogs
        self._write_json(self._dialogs)

    def read_json(self):
        self._dialogs = self._read_json(self._FILE_NAME_JSON)
        return self._dialogs

    def write_data(self):
        body = "# HWM DIALOGS\n\n"
        for dialog_seq_header, dialog_seq_list in self._dialogs.items():
            body += f"## {dialog_seq_header}\n\n".upper()
            for dialog in dialog_seq_list:
                body += f"### {dialog['speaker_id']}\n"
                body += f"{dialog['dialog_id']}\n\n"
        utils.rewrite_file(body, self._FILE_NAME)

    def write_data_w_strings(self):
        body = "# HWM DIALOGS with STRINGS\n\n"
        for dialog_seq_header,dialog_seq_list in self._dialogs.items():
            body += f"## {dialog_seq_header}\n".upper()
            body += self.get_dialog_seq_string_by_header(dialog_seq_header)
        utils.rewrite_file(body, self._FILE_NAME_STR) 
    
    def get_dialog_seq_string_by_header(self, dialog_seq_header):
        raw_dialog_seqs = self._read_json(self._FILE_NAME_JSON)
        dialog_seq_list = raw_dialog_seqs.get(dialog_seq_header)

        body = ""
        for dialog in dialog_seq_list:
            speaker_id = dialog['speaker_id']
            dialog_id = dialog['dialog_id']

            speaker = self.get_speaker_string(speaker_id)
            body += f"### {speaker}\n"

            dialog = self.get_dialog_string(dialog_id)
            body += f"{dialog}\n\n"

        return body

    def get_speaker_string(self, speaker_id):
        speaker_key = f"name_{speaker_id}".lower()
        
        speaker_string_el = self._string_data.get(speaker_key)
        if speaker_string_el:
            speaker_string = speaker_string_el['en:']
            return speaker_string
        else:
            speaker_string = f"{speaker_id}: speaker name not found"
            print(speaker_string)
            return speaker_string

    def get_dialog_string(self, dialog_id):
        dialog_string = ""

        dialog_id_upd = dialog_id.lower()
        dialog_string_element = self._string_data.get(dialog_id_upd)
        if dialog_string_element:
            dialog_string = dialog_string_element['en:']
            return dialog_string
        else:
            dialog_id_upd = re.sub(r'_(\d+)$', r'_dia_\1', dialog_id)
            dialog_string_element = self._string_data.get(dialog_id_upd)
            if dialog_string_element:
                dialog_string = dialog_string_element['en:']
                return dialog_string
            else:
                dialog_string = f"dialog_id not found: {dialog_id}"
                print(dialog_string)
                return dialog_string
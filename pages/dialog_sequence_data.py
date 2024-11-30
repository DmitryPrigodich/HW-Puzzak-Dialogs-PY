import utils
import json
from .base_page import Base_Page

class Dialog_Seq_Data_Page(Base_Page):
    _LOCATOR = "#DialogSequenceData-module"
    _FILE_NAME = "data/DIALOGS_SEQ.md"
    _FILE_NAME_JSON = "json/dialog_seq.json"

    _dialog_seqs = {}

    def __init__(self, page):
        super().__init__(page, self._LOCATOR)

    def save_data(self):
        for element_entry in self._get_list_elements_entries("Dialog Sequence Data"):
            dialog_seq_header = self._get_entryhead(element_entry)
            dialog_ids = self._get_entryitem_by_tag(element_entry, "DialogIds").split(":")
            speaker_ids = self._get_entryitem_by_tag(element_entry, "SpeakerIds").split(":")

            speakers_dialogs = [] 
            for index, (speaker_id, dialog_id) in enumerate(zip(speaker_ids, dialog_ids)):
                speakers_dialogs.append({"index": index, "speaker": speaker_id, "dialogue": dialog_id})
            self._dialog_seqs[dialog_seq_header] = speakers_dialogs
        return self._dialog_seqs

    def write_json(self):
        json_data = json.dumps(self._dialog_seqs, ensure_ascii=False)
        utils.rewrite_file(json_data, self._FILE_NAME_JSON)
    
    def read_json(self):
        with open(self._FILE_NAME_JSON, 'r', encoding='utf-8') as file:
            json_data = file.read()
        self._dialog_seqs = json.loads(json_data)
        return self._dialog_seqs
    
    def get_dialog_seq_by_header(self, dialog_seq_header):
        return self._dialog_seqs.get(dialog_seq_header)
    
    def write_data(self):
        body = "# HWM DIALOGS SEQUENCES:\n"
        for dialog_seq_header, speakers_dialogs in self._dialog_seqs.items():
            body += f"\n### {dialog_seq_header}\n"
            for speaker_dialog in speakers_dialogs:
                body += f"* {speaker_dialog['speaker']}: {speaker_dialog['dialogue']}\n"

        utils.rewrite_file(body, self._FILE_NAME)

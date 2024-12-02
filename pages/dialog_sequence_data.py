import utils
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
        self._write_json(self._dialog_seqs)
    
    def read_json(self):
        return self._read_json(self._FILE_NAME_JSON)
    
    def write_data(self):
        body = "# HWM DIALOGS SEQUENCES:\n"
        for dialog_seq_header, speakers_dialogs in self._dialog_seqs.items():
            body += f"\n### {dialog_seq_header}\n"
            for speaker_dialog in speakers_dialogs:
                body += f"* {speaker_dialog['speaker']}: {speaker_dialog['dialogue']}\n"

        utils.rewrite_file(body, self._FILE_NAME)

    def get_dialog_seq_by_header(self, dialog_seq_header):
        return self._dialog_seqs.get(dialog_seq_header)
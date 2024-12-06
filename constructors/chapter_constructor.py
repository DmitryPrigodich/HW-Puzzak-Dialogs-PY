from .constuctor_base import Constructor_Base

class Chapter_Constructor(Constructor_Base):
    _CHAPTER_DATA_JSON = "json_bak/ChapterData-module.json"
    _CHAPTERS_JSON = "json/chapter_strings.json"

    _FILE_NAME = "data/CHAPTER.md"
    _FILE_NAME_TMP = "data/CHAPTER_TMP.md"

    _chapter_data = {}
    _chapters = {}

    def __init__(self):
        super().__init__()
        self._chapter_data = self._read_json(self._CHAPTER_DATA_JSON)
        self._chapters = self._read_json(self._CHAPTERS_JSON)
        # self._set_chapters()

    # data was already recorded in pages\chapter_data.py, so I won't repeat myself for now
    # def _set_chapters(self):
    # def write_data(self):
    # def write_data_spc(self):

    def get_chapters(self):
        return self._chapters
    
    def check_chapter(self, chapter):
        return any(item["header"] == chapter for item in self._chapters)
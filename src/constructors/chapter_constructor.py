import utils
from .constructor_base import Constructor_Base
from .quest_constructor import Quest_Constructor
from .quest_line_constructor import Quest_Line_Constructor

class Chapter_Constructor(Constructor_Base):
    _CHAPTER_DATA_JSON = "dataset/json_bak/ChapterData-module.json"

    _FILE_NAME = "dataset/data/CHAPTERS.md"
    _FILE_NAME_JSON = "dataset/json/chapters.json"

    _chapter_data = {}
    _chapters = {}

    def __init__(self):
        super().__init__()
        self._chapter_data = utils.read_json(self._CHAPTER_DATA_JSON)
        self._set_data()

    def _set_data(self):
        for chapter_id, chapter_params in self._chapter_data.items():

            chapter_order = chapter_params.get("Order:")
            chapter_quest_ids = chapter_params.get("Ids:").split("\n")
            chapter_name = self._get_chapter_name(chapter_id)

            self._chapters[chapter_id] = {
                "Order:": chapter_order,
                "Name:": chapter_name,
                "Ids:": chapter_quest_ids,
            }

    def get_data(self):
        return self._chapters
    
    def write_json(self):
        utils.write_json(self._chapters,self._FILE_NAME_JSON)

    def write_data(self):
        body = "# **HWM CAMPAIGN CHAPTERS**\n"

        for chapter_id, chapter_params in self._chapters.items():
            chapter_order = chapter_params.get("Order:")
            chapter_name = chapter_params.get("Name:")
            chapter_quest_ids = chapter_params.get("Ids:")

            body += f"\n## **{chapter_order}. {chapter_id}: {chapter_name}**\n".upper()
            for id in chapter_quest_ids:
                body += f"\t* {id}\n"

        utils.rewrite_file(body, self._FILE_NAME)

    def get_chapters(self):
        return self._chapters
    
    def check_chapter(self, chapter):
        return any(item["header"] == chapter for item in self._chapters)
    
    def _get_chapter_name(self, chapter_id):
        chaptername_key = f"chaptername_{chapter_id}"
        return self.get_string_by_key(chaptername_key)
    

    def get_chapter_text(self, chapter_id):
        def _get_quest_text(quest_id):
            # print(f"Quest Id: {quest_id}")
            return quest_data.get_quest_text(quest_id)

        chapter = self._chapters.get(chapter_id)
        chapter_order = chapter.get("Order:")
        chapter_name = chapter.get("Name:")
        chapter_quest_ids = chapter.get("Ids:")
        
        body_chapter = ""
        body_chapter += utils.format_br(1)
        body_chapter += utils.format_heading1(f"Chapter: {chapter_order}. {chapter_name}")
        body_chapter += utils.format_br(2)

        quest_line_data = Quest_Line_Constructor()
        quest_data = Quest_Constructor()
        for quest_id in chapter_quest_ids:
            if quest_id.startswith("ql_"):
                # print(f"Quest Line Id: {quest_id}")
                quests = quest_line_data.get_quests_by_quest_line_id(quest_id.lower())
                if quests:
                    for quest_id in quests:
                        body_chapter += _get_quest_text(quest_id)
            else:
                body_chapter += _get_quest_text(quest_id)

        return body_chapter
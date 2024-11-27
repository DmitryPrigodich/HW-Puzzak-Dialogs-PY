from .constuctor_base import Constructor_Base

class String_Data_Constructor(Constructor_Base):
    FILE_NAME = "data/STRINGS.md"

    def __init__(self):
        super().__init__()
    
    def get_string_by_key(self, key):
        return self._string_data.get(key)['en:']


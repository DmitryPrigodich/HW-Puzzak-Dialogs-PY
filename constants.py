URL_HWM_DB = 'https://hwm.puzzak.page/'
OUTPUT = 'OUTPUT.md'

LOCATOR_ENTRYHEAD = "//div[@class='entryhead']/b"
# '.entryhead b'
LOCATOR_ENTRYITEM = "//div[@class='entryitem'][b[@class='entryitemname' and contains(text(), '{}')]]/a"
# ".entryitem:has(b.entryitemname:has-text('{}')) a.entryitemvalue"

#modules
LOCATOR_EVENTDATA = "#EventData-module"
LOCATOR_QUESTLINEDATA = "#QuestLineData-module"
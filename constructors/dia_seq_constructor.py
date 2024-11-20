import utils
import json

class Dialog_Sequence_Constructor():
    _dialog_seqs = []
    _speakers = {}
    _dialogs = {}
    

    def _read_json(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            json_data = file.read()
        json_input = json.loads(json_data)
        return json_input
    
    def write_json(self):
        json_data = json.dumps(self._all_systems_map, ensure_ascii=False)
        utils.rewrite_file(json_data, self.FILE_NAME_JSON)

    def write_data(self):
        body = "# NIMBUS KNOWN STAR SYSTEMS\n"
        # for coords, system in self._all_systems_map.items():
        #     body += f"* {system['faction']} : {system['name']} : {coords}\n"
        # utils.rewrite_file(body, self.FILE_NAME)

        sorted_systems_by_faction = sorted(self._all_systems_map.items(), key=lambda item: item[1]['faction'])
        for faction, group in groupby(sorted_systems_by_faction, key=lambda item: item[1]['faction']):
            body += f"\n## {faction}\n"
            for coords, system in group:
                body += f"* {system['name']} : {coords}\n"
        utils.rewrite_file(body, self.FILE_NAME)
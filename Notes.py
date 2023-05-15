import json
import os
from datetime import datetime
from typing import Union, List

class Notebook():
    def __init__(self) -> None:
        self.data_file = r'Notebook.json'
        with open(r'menu.json', encoding='utf-8') as f:
                  self.rows = json.load(f)
        if os.path.exists(self.data_file):
            with open(self.data_file, encoding='utf-8') as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def open_note(self, note_name) -> Union[str, None]:
        if note_name in self.data.keys():
            for key in self.data[note_name].keys():
                print(f'{key}: {self.data[note_name][key]}')
        print(self.rows['redactor'][0])
        text = input()
        self.data[note_name] = {}
        self.data[note_name]['text'] = text
        print(self.rows['redactor'][1])
        author = input()
        self.data[note_name]['author'] = author
        self.data[note_name]['data'] = str(datetime.now().date())
        self.data[note_name]['time'] = str(datetime.now().time())
        with open(self.data_file, 'w', encoding='utf-8') as f:
            js = json.dumps(self.data)
            f.write(js)

    def read_note(self, note_name: str) -> Union[dict, None]:
        if note_name in self.data.keys():
            return self.data[note_name]
        else:
            return None
        
    def get_note_names(self) -> List[str]:
        return list(self.data.keys())
    
    def remove_note(self, note_name: str) -> int:
        if note_name in self.data.keys():
            del self.data[note_name]
            with open(self.data_file, 'w', encoding='utf-8') as f:
                js = json.dumps(self.data)
                f.write(js)
            return 0
        else:
            return 1
        
    def rename_note(self, old_name: str, new_name: str) -> int:
        if old_name in self.data.keys():
            self.data[new_name] = self.data.pop(old_name)
            with open(self.data_file, 'w', encoding='utf-8') as f:
                js = json.dumps(self.data)
                f.write(js)
            return 0
        else:
            return 1

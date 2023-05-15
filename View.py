import json
import os
from Notes import Notebook


class Handler():
      def __init__(self) -> None:
            self.notebook = Notebook()
            with open(r'menu.json', encoding='utf-8') as f:
                  self.rows = json.load(f)

      def action(self, enter: str) -> int:
            enter = enter.split()
            command = enter[0]
            args = enter[1:]
            if command not in self.rows['commands']:
                  return 1
            elif command == 'exit':
                  return -1
            elif command == 'remove':
                  self.notebook.remove_note(args[0])
                  return 0
            elif command == 'rename':
                  if len(args) <= 1:
                        return 1
                  else:
                        self.notebook.rename_note(*args[:2])
                        return 0
            elif command == 'list':
                  data = self.notebook.get_note_names()
                  for item in data:
                        print(item)
                  return 0
            elif command == 'read':
                  data = self.notebook.read_note(args[0])
                  for key in data.keys():
                        print(f'{key}: {data[key]}')
                  return 0
            elif command == 'open':
                  self.notebook.open_note(args[0])
                  return 0

      def main_process(self) -> None:
            os.system('cls')
            while 1:                  
                  for row in self.rows['menu']:
                        print(row)
                  command = input()
                  os.system('cls')
                  status = self.action(command)
                  if status == -1:
                        break

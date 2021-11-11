import json

def create_json_file(path, obj):
    with open(path, 'w') as fh:
        json.dump(obj, fh)

if __name__ == '__main__':
    j = {"menu": {
        "id": "file",
        "value": "File",
        "popup": {
          "menuitem": [
            {"value": "New", "onclick": "CreateNewDoc()"},
            {"value": "Open", "onclick": "OpenDoc()"},
            {"value": "Close", "onclick": "CloseDoc()"}
          ]
        }
      }}
    create_json_file('test.json', j)
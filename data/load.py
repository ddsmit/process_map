import json
import pathlib

def all(file_location=r'data\elements.json'):

    file_path = pathlib.Path('.',file_location)
    try:
        with file_path.open() as json_file:
            return json.load(json_file)
    except:
        raise
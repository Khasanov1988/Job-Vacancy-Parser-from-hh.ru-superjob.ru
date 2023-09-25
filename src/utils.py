import json


def printj(dict_to_print: dict) -> None:
    """Prints a dictionary in a JSON-like format with indentation."""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

import json

def json_formatter(input):
    try:
        parsed = json.loads(input)
        pretty = json.dumps(parsed, ensure_ascii = True, indent = 4)
        return pretty
    except ValueError as e:
        pretty = None
        return pretty
    
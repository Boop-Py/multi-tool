import json

def json_formatter(input):
    try:
        parsed = json.loads(input)
        pretty = json.dumps(parsed, ensure_ascii = True, indent = 4)
        return pretty
    except ValueError as e:
        pretty = "Invalid JSON. Please try again."
        return pretty
    
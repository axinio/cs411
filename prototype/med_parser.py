import json
#new tracing function

def wrap_trace(json_d):
    temp = []
    a = json_d.json()
    finders = a.keys()
    if "fullInteractionTypeGroup" not in finders:
        return None
    else:
        b = a["fullInteractionTypeGroup"]
        c = b[0]["fullInteractionType"]
        d = c[0]["interactionPair"]
        results = d[0]["description"]
    return results



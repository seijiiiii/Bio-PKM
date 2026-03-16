import re

def highlight(text, query):

    keywords = query.split()

    for word in keywords:
        pattern = re.compile(f"({word})", re.IGNORECASE)
        text = pattern.sub(r"<mark>\1</mark>", text)

    return text
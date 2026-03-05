def format_advice(text):

    lines = text.split("\n")

    cleaned = [line.strip() for line in lines if line.strip() != ""]

    return cleaned
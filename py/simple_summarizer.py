def summarize(text, max_sentences=4):
    import re
    sentences = re.split(r"(?<=[.!?])\s+", text)
    sentences = sorted(sentences, key=lambda s: -len(s))
    return " ".join(sentences[:max_sentences])

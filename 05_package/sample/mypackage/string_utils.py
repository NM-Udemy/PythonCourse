def format_name(first, last):
    return f'{last.title()}, {first.title()}'

def clean_text(text):
    return text.strip().lower().replace('  ', ' ')

def count_words(text):
    return len(text.split())
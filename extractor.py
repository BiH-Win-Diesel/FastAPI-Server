import re
def extract_information(text):
    description_pattern = re.compile(r'([a-zA-Z]+)\s*')
    quantity_pattern = re.compile(r'(\d+)\s*(?:unit|units|packet|pack)\s*')
    price_pattern = re.compile(r'(\d+(\.\d{1,2})?)')

    description_match = description_pattern.search(text)
    quantity_match = quantity_pattern.search(text)
    price_matches = price_pattern.findall(text)

    description = description_match.group() if description_match else None
    quantity = quantity_match.group(1) if quantity_match else None
    price = price_matches[-1] if price_matches else None

    return description, quantity, price
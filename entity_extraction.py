import re
def extract_entity(text, product_list):
    text = text.lower()
    entities = {
        "product": None,
        "complaint_keywords": [],
        "date_mentions": [],
        "order_number": None
    }
    for product in product_list:
        if product.lower() in text:
            entities["product"] = product
            break
    order_number_match = re.findall(r'#(\d+)', text)
    if order_number_match:
        entities['order_number'] = order_number_match[0]
    
    # Extract complaint keywords
    complaint_keywords = ["installation", "payment","broken", "error", "stopped", "not working","malfunction", "late", "underbilled", "wrong",  "issue"]
    for word in complaint_keywords:
        if word in text:
            entities["complaint_keywords"].append(word)
    
    
    #Extract date mentions
    date_patterns = [
        r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",      # dates like 12/01/2024
        r"\b\d+ (day|week|month|year)s?\b",  # 2 days, 1 week, etc.
        r"\b(last|next) (day|week|month|year)\b",  # last week, next month
        r"\b(today|yesterday|tomorrow)\b"
    ]
    
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        if matches:
            entities["date_mentions"].extend([' '.join(m) if isinstance(m, tuple) else m for m in matches])
    
    return entities 
    
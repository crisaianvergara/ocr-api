import re
import datetime
import nltk


# FORMAT DATE
def extract_and_format_date(result, patterns):
    for pattern in patterns:
        for item in result:
            match = re.search(pattern, item)
            if match:
                date = match.group(0).strip()
                if len(date) > 15:
                    date = date[6:]
                formats = [
                    "%Y-%m-%d",
                    "%d-%m-%y",
                    "%m/%d/%y",
                    "%m/%d/%Y",
                    "%d %b %y",
                    "%m-%d-%y",
                    "%b %d,%Y",
                ]
                for date_format in formats:
                    try:
                        dt = datetime.datetime.strptime(date, date_format)
                        formatted_date = dt.strftime("%m/%d/%Y")
                        return formatted_date
                    except ValueError:
                        pass
    return None


# TOKENIZE AND FILTER THE OCR RESULT
def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    stop_words = set(nltk.corpus.stopwords.words("english"))
    filtered_tokens = [w for w in tokens if not w in stop_words]
    return filtered_tokens


# CLASSIFY DESCRIPTION
def classify_description(words):
    categories_found = {}
    for word in words:
        for description, keywords in categories.items():
            if word in keywords:
                if description in categories_found:
                    categories_found[description] += 1
                else:
                    categories_found[description] = 1
    if categories_found:
        return max(categories_found, key=categories_found.get)
    else:
        return "Other"


categories = {
    "Grocery": [
        "grocery",
        "food",
        "beverage",
        "produce",
        "meat",
        "dairy",
        "bakery",
        "deli",
        "canned",
        "snacks",
        "cereal",
        "frozen",
        "alcohol",
        "milk",
        "bread",
        "fruit",
        "vegetable",
    ],
    "Shopping": [
        "iphone",
        "laptop",
        "saree",
        "max",
        "pantaloons",
        "westside",
        "vedic",
        "makeup",
        "lipstick",
        "cosmetics",
        "mac",
        "facewash",
        "heels",
        "crocs",
        "footwear",
        "purse",
    ],
    "Household": [
        "household",
        "cleaning",
        "laundry",
        "paper",
        "tissue",
        "toiletries",
        "pet",
        "soap",
        "kitchen",
    ],
    "Healthcare": ["healthcare", "medicine", "pharmacy", "vitamins", "supplements"],
    "Apparel": ["apparel", "clothing", "shoes", "accessories"],
    "Electronics": ["electronics", "computer", "phone", "accessories"],
    "Home Improvement": ["home improvement", "hardware", "tools", "paint"],
    "Office Supplies": ["office supplies", "stationery", "paper"],
    "Entertainment": ["entertainment", "movies", "music", "books", "magazines"],
    "Transportation": [
        "transportation",
        "gas",
        "car",
        "parking",
        "tolls",
        "public transit",
        "taxi",
        "ride share",
    ],
    "Travel": ["travel", "hotel", "flight", "rental", "cruise"],
    "Services": [
        "services",
        "cleaning",
        "maintenance",
        "repair",
        "consulting",
        "professional fees",
        "subscriptions",
        "memberships",
    ],
    "Charitable Donations": ["charitable donations", "charity", "philanthropy"],
    "Taxes": ["taxes", "tax", "government", "fees"],
    "Personal Care": [
        "toothpaste",
        "shampoo",
        "soap",
        "lotion",
        "razor",
        "deodorant",
        "feminine",
    ],
    "Pharmacy": [
        "medicine",
        "vitamin",
        "supplement",
        "prescription",
        "pain",
        "first aid",
    ],
    "Pet Care": ["dog", "cat", "pet", "food", "treat", "toy"],
    "Electronics": ["computer", "tablet", "phone", "charger", "speaker", "cable"],
    "Clothing": ["shirt", "pants", "dress", "shoes", "socks", "jacket", "accessory"],
    "Home Decor": ["furniture", "rug", "curtain", "pillow", "decor"],
    "Gifts": ["card", "gift", "wrap", "ribbon", "bow"],
    "Meals": [
        "breakfast",
        "lunch",
        "dinner",
        "brunch",
        "snack",
        "appetizer",
        "main course",
        "dessert",
        "beverage",
        "coffee",
        "tea",
        "juice",
    ],
    "Home Utility": [
        "internet",
        "telephone",
        "electricity",
        "meter",
        "wifi",
        "broadband",
        "consumer",
        "reading",
        "gas",
        "water",
        "postpaid",
        "prepaid",
    ],
    "Investment": [
        "endowment",
        "grant",
        "loan",
        "applicant",
        "income",
        "expenditure",
        "profit",
        "interest",
        "expense",
        "finance",
        "property",
        "money",
        "fixed",
        "deposit",
    ],
}

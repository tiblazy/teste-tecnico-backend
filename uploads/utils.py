from transactions.models import Transaction

def normalize_file_txt(file) -> dict:
    decode_file = file.read().decode("utf-8")
    split_file = decode_file.split("\r\n")

    for line in split_file:
        data = {
            "type": line[0],
            "date": f"{line[1:5]}-{line[5:7]}-{line[7:9]}",
            "value": round(int(line[9:19]) / 100, 2),
            "ssn": line[19:30],
            "card": line[30:42],
            "hour": f"{line[1:5]}-{line[5:7]}-{line[7:9]} {line[42:44]}:{line[44:46]}:{line[46:48]}",
            "owner": line[48:62].strip(),
            "store": line[62:].strip(),
        }

        Transaction.objects.create(**data)

def filter_store(stores) -> list:
    store_names = []
    store_unique = []

    for store in stores:
        if store.store not in store_names:
            store_names.append(store.store)

    for store_name in store_names:
        if store_name not in store_unique:
            store_unique.append({"store": store_name})

    return store_unique

def get_store(store_name) -> list:
    store = list(store_name.values())[0]
    return Transaction.objects.filter(store=store)

def transactions_store(store_name) -> list:
    stores = get_store(store_name)
    transactions = []
    transactions_type = [
        {"1":"Debit"}, 
        {"2":"Bank Slip"}, 
        {"3":"Financing"}, 
        {"4":"Credit"}, 
        {"5":"Loan"},
        {"6":"Sell"},
        {"7":"TED"}, 
        {"8":"DOC"},
        {"9":"Rent"},
                        ]
    negative = [
        "2",
        "3",
        "9",
    ]
    
    for transaction in stores:
        for trasaction_type in transactions_type:
            if list(trasaction_type.keys())[0] == transaction.type:
                if transaction.type in negative:
                    transactions.append({"type": list(trasaction_type.values())[0], "value": round(-transaction.value,2),},)
                else:
                    transactions.append({"type": list(trasaction_type.values())[0], "value": round(transaction.value,2),},)

    return transactions

def calculate_store_currency(store_name) -> float:
    stores = get_store(store_name)
    negative = [
        "2",
        "3",
        "9",
    ]

    sum = 0
    for transaction in stores:
        if transaction.type in negative:
            sum -= round(transaction.value, 2)
        else:
            sum += round(transaction.value, 2)

    return sum

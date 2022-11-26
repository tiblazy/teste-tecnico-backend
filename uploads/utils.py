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


def filter_store(stores) -> float:
    store_names = []
    store_unique = []

    for store in stores:
        if store.store not in store_names:
            store_names.append(store.store)

    for store_name in store_names:
        if store_name not in store_unique:
            store_unique.append({"store": store_name})

    return store_unique


def calculate_store_currency(store_name) -> float:
    store = list(store_name.values())[0]
    stores = Transaction.objects.filter(store=store)
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

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


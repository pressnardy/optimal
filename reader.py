import csv


def get_summary(file_path) -> "list of dict":
    raw_summary = []
    summary = []
    fieldnames = ["name", "symbol", "risk score", "balance", "investment"]
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_summary.append(row)

    # verify the format of the cvs file
    for key in raw_summary[0].keys():
        if key.strip() not in fieldnames:
            raise KeyError(f"csv file missing correct headers. use {fieldnames}")

    # convert numeric values of balance and investment from str to float
    for coin in raw_summary:
        coin_update = {}
        for k, v in coin.items():
            try:
                coin_update.update({k: float(v)})
            except ValueError:
                coin_update.update({k: v})

        summary.append(coin_update)
    return summary


for i in get_summary("test.csv"):
    print(i)

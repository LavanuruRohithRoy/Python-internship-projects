def get_exchange_rates():
    # Mocked rates (USD base). Will replace with real time API later.
    return {
        "USD": 1.0,
        "INR": 83.24,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 148.12
    }


def convert_currency(rates, source, target, amount):
    # Core conversion logic
    if source not in rates or target not in rates:
        raise ValueError("Unsupported currency code")

    return round((amount / rates[source]) * rates[target], 2)


def get_user_input():
    # UI validation only.
    source = input("Source currency: ").strip().upper()
    target = input("Target currency: ").strip().upper()

    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("Amount must be a positive number")

    return source, target, amount


def main():
    try:
        source, target, amount = get_user_input()
        rates = get_exchange_rates()
        result = convert_currency(rates, source, target, amount)
        print(f"{amount} {source} = {result} {target}")
    except ValueError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

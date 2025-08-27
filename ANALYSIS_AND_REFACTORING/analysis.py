def validate_data(entry: str) -> tuple[int, str] | None:

    try:
        number_str, text = entry.split(",")
        number = int(number_str.strip())

        if 0 < number < 150 and text.strip():
            return number, text.strip()
        else:
            return None
    except (ValueError, IndexError):
        return None


def main():
    data = input("Enter data in the format 'number,text': ")
    result = validate_data(data)

    if result:
        print("OK")
    else:
        print("Error: Invalid input")


if __name__ == "__main__":
    main()

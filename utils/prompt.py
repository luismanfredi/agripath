def ask_int(num_str: str) -> int | None:
    try:
        num: int = int(num_str)
        return num
    except ValueError:
        return None


def choose_index(labels: list[str], prompt: str) -> int | None:
    for index, label in enumerate(labels):
        print(f"{index + 1}. {label}")
    print("-" * 40)

    user_input: str = input(prompt)
    print("-" * 40)

    if user_input == "0":
        print("Operation cancelled.")
        return None

    chosen: int | None = ask_int(user_input)

    if chosen is None:
        print(f"{chosen} is not a valid number. Please try again.")
        return None

    if not (1 <= chosen <= len(labels)):
        print(f"Not found! Choose a number between 1 and {len(labels)}!")
        return None

    return chosen - 1

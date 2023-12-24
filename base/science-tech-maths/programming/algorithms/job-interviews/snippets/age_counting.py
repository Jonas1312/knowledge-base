"""Count the number of ages above or equal to 50 in a string of data."""


def age_count(data: str) -> int:
    count = 0
    for key_value in data.split(", "):
        if "age=" in key_value:
            age = int(key_value.split("=")[1])
            if age >= 50:
                count += 1
    return count


def main():
    assert age_count("key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47") == 2


if __name__ == "__main__":
    main()

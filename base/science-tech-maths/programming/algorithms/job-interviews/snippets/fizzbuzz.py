def main():
    for i in range(1, 100 + 1):
        buzz = not i % 3
        fizz = not i % 5
        if fizz and buzz:  # // 3*5 = 15 must be tested first !!!
            print("FizzBuzz")
        elif buzz:
            print("Buzz")
        elif fizz:
            print("Fizz")
        else:
            print(i)


if __name__ == "__main__":
    main()

def print_full_name(first_name, last_name):
    if (len(first_name) <= 10 and len(last_name) <= 10):
        print("hello {} {}! You just delved into python.".format(first_name,last_name))


if __name__ == '__main__':
    first_name =input()
    last_name = input()
    print_full_name(first_name, last_name)
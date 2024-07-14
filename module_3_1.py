calls = 0


def count_calls():
    global calls
    calls += 1 
    print(calls)


def string_info(string):
    global calls
    calls +=1
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    global calls
    calls += 1
    for i in list_to_search:
        if string.upper() == i.upper():
            return True
    return False


print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains("Urban", ["ban", "BaNaN", "urBan"]))
print(is_contains("cycle", ["recycling", "cyclic"]))
print(calls)

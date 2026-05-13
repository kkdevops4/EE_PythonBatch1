# CAN BUS MESSAGE VALIDATOR
# Function to read CAN messages from file
def read_can_file(filename):

    messages = []

    try:
        file = open(filename, "r")

        for line in file:
            msg = line.strip()

            if msg != "":
                messages.append(msg)

        file.close()
        return messages

    except:
        print("Error reading file:", filename)
        return None


# Function to compare messages
def validate_can_messages(correct_msgs, test_msgs):

    print("\n========== VALIDATION REPORT ==========\n")

    matched = 0
    wrong = 0

    # Check order
    for i in range(min(len(correct_msgs), len(test_msgs))):

        if correct_msgs[i] == test_msgs[i]:
            print("MATCHED ->", correct_msgs[i])
            matched += 1

        else:
            print("WRONG ORDER")
            print("Expected :", correct_msgs[i])
            print("Found    :", test_msgs[i])
            wrong += 1

    # Missing messages
    missing = []

    for msg in correct_msgs:
        if msg not in test_msgs:
            missing.append(msg)

    # Extra messages
    extra = []

    for msg in test_msgs:
        if msg not in correct_msgs:
            extra.append(msg)

    # Summary
    print("\n========== SUMMARY ==========")
    print("Matched Messages     :", matched)
    print("Wrong Order Messages :", wrong)

    print("\nMissing Messages:")
    if missing:
        for msg in missing:
            print(msg)
    else:
        print("None")

    print("\nExtra Messages:")
    if extra:
        for msg in extra:
            print(msg)
    else:
        print("None")

    print("\n================================")


# MAIN PROGRAM

print("===== CAN BUS MESSAGE VALIDATOR =====")

correct_file = input("Enter correct file name: ")
test_file = input("Enter test file name: ")

correct_messages = read_can_file(correct_file)
test_messages = read_can_file(test_file)

if correct_messages != None and test_messages != None:
    validate_can_messages(correct_messages, test_messages)
    
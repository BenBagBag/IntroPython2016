#!/usr/bin/env python

def accept_donation():
    amount = input("How much did this person donate? \n")
    if amount == "x" or check_if_number(amount):
        return amount
    else:
        print("You must enter a numeric amount.")
        return accept_donation()

def check_if_number(num):
    try:
        float(num)
        return True
    except ValueError or TypeError:
        return False


def create_reports():
    donor_rows = []
    for donor in donors:
        new_row = []
        new_row.append(donor[0])
        new_row.append("{:.2f}".format(sum(donor[1:])))
        new_row.append(str(len(donor[1:])))
        new_row.append("{:.2f}".format(float(new_row[1]) / int(new_row[2])))
        donor_rows.append(new_row)
    return donor_rows


def format_row(row):
    formatted = []
    for item in row:
        formatted.append('{:30}'.format(item))
    return ' '.join(formatted)


def print_donor_list():
    print("These are the donors you have in your database:")
    for donor in donors:
        print(donor[0])
    print()


def print_report():
    print("This will print a report")
    header_row = ["Name", "Total Donated", "Number of Donations", "Average Donation"]
    donor_rows = create_reports()
    sorted_donors = sort_donors(donor_rows)
    print(format_row(header_row))
    for row in sorted_donors:
        print(format_row(row))
    print()


def send_thanks():
    print("This will write a thank you note")
    donor_names = [x[0] for x in donors]
    thank_you_command = input("Type the full name of the person you would like to thank. \nOr type 'list' to see a list of donors.\n")
    if thank_you_command == "x":
        return
    elif thank_you_command.lower() == "list":
        print_donor_list()
    else:
        donation_amount = accept_donation()
        if donation_amount == "x":
            return
        else:
            donation_amount = float(donation_amount)
        if thank_you_command in donor_names:
            name = thank_you_command
            donors[donor_names.index(name)].append(donation_amount)
            print("Adding ${:02.2f} to {}'s donations.".format(donation_amount, name))
            print_thank_you(name, donation_amount)
        else:
            print(donation_amount)
            name = thank_you_command
            donors.append([name, donation_amount])
            print("Adding {} as a donor, with a donation of ${:02.2f}.".format(name, donation_amount))
            print_thank_you(name, donation_amount)



# here is where triple quoted strings can be helpful
msg = """
What would you like to do?

To send a thank you: type "s"
To print a report: type "p"
To exit: type "x"
"""

donors = [["Wilmot Filipe", 18.00, 72.00], ["Neoptolemus Yaropolk", 36.00], ["Mahesha Diogenes", 90.00, 54.00, 18.00], ["Arthur Tjaz", 18.00], ["Luuk Sinclair", 180.00]]


def main():
    """
    run the main interactive loop
    """

    response = ""
    # keep asking until the users responds with an 'x'
    while True:  # make sure there is a break if you have infinite loop!
        print(msg)
        response = input("==> ").strip().lower()  # strip() in case there are any spaces
        if response == 'p':
            print_report()
        elif response == 's':
            send_thanks()
        elif response == 'x':
            break
        else:
            print('please type "s", "p", or "x"')

def print_thank_you(name, donation):
    print("Sending this email: ")
    print("Dear {},\nThank you for your gift of ${:02.2f} to the Fund for Unmatched Socks. Your help will be greatly appreciated by all those who partake in our holey work.".format(name, donation))
    print()


def sort_donors(donor_list):
    sorted_donors = []
    sorted_donors.append(donor_list[0])
    for donor in donor_list[1:]:
        for x in range(len(sorted_donors)):
            if float(donor[1]) > float(sorted_donors[x][1]):
                sorted_donors.insert(x, donor)
                break
            elif x == len(sorted_donors) - 1:
                sorted_donors.append(donor)
    return sorted_donors


if __name__ == "__main__":
    main()

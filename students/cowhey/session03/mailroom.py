#! /usr/bin/env python3

donors = [["Wilmot Filipe", 18.00, 72.00], ["Neoptolemus Yaropolk", 36.00], ["Mahesha Diogenes", 90.00, 54.00, 18.00], ["Arthur Tjaz", 18.00], ["Luuk Sinclair", 180.00]]

def accept_donation():
    amount = input("How much did this person donate? \n")
    while not amount.isnumeric():
        amount = input("Sorry, you need to enter a donation amount using only numbers: \n")
    return float(amount)


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

def main():
    user_command = orig_prompt()
    while user_command != "quit":
        if user_command == "1":
            send_thank_you()
            user_command = orig_prompt()
        elif user_command == "2":
            print_report()
            user_command = orig_prompt()
        else:
            print("Not a valid command.")
            user_command = orig_prompt()
    return


def orig_prompt():
    return input("Would you like to: \n 1.Send a thank you \n 2. Create a report \n or quit? \n")


def print_donor_list():
    print("These are the donors you have in your database:")
    for donor in donors:
        print(donor[0])


def print_report():
    header_row = ["Name", "Total Donated", "Number of Donations", "Average Donation"]
    donor_rows = create_reports()
    sorted_donors = sort_donors(donor_rows)
    print(format_row(header_row))
    for row in donor_rows:
        print(format_row(row))


def print_thank_you(name, donation):
    print("Sending this email: ")
    print("Dear {},\nThank you for your gift of ${:02.2f} to the Fund for Unmatched Socks.".format(name, donation))


def send_thank_you():
    donor_names = [x[0] for x in donors]
    thank_you_command = input("Type the full name of the person you would like to thank. \nOr type 'list' to see a list of donors.\n")
    if thank_you_command.lower() == "quit":
        orig_prompt()
    elif thank_you_command.lower() == "list":
        print_donor_list()
    elif thank_you_command in donor_names:
        donation_amount = accept_donation()
        donors[donor_names.index(thank_you_command)].append(donation_amount)
        print("Adding ${:02.2f} to {}'s donations.".format(float(donation_amount), thank_you_command))
        print_thank_you(thank_you_command, donation_amount)
        orig_prompt()
    else:
        donation_amount = accept_donation()
        donors.append([thank_you_command, donation_amount])
        print("Adding {} as a donor, with a donation of ${:02.2f}.".format(donation_amount, float(donation_amount)))
        print_thank_you(thank_you_command, donation_amount)
        orig_prompt()


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

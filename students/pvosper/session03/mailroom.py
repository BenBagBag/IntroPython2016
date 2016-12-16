#!/usr/bin/env python3

print("You've Got Mail!")

# ===== Initial data set =====

donor_list = [
    ["Domingo Nair", [75, 50, 25]],
    ["Cruz Woodman", [100]],
    ["Quinn Halvorsen", [125, 500, 50]],
    ["Carlota Lamkin", [50, 200]],
    ["Angelyn Meekins", [500, 50]],
    ["Maryland Cassel", [100, 50, 60]],
    ["Muoi Macken", [125]],
    ["Robby Remus", [25, 50, 75]],
    ["Arlette Vanderveer", [125, 50]],
    ["Reed Brantley", [125, 50, 200]],
    ["Lenard Hardegree", [100]],
    ["Lashunda Mckeithan", [125, 50]],
    ["Eveline Paquette", [100, 250]],
    ["Shawana Cano", [125, 50, 250]],
    ["Phylicia Sansbury", [25, 100]],
    ["Ricarda Wykoff", [100, 50, 200]],
    ["Lue Mollett", [125, 50, 250]],
    ["Janean Hetzler", [125, 50]],
    ["Garth Figura", [125]],
    ["Kurt Cowherd", [100, 50, 25]]
    ]

# ===== Utilities =====

def donor_name_length():
    length_name = 0
    for entry in donor_list:
        if len(entry[0]) > length_name:
            length_name = len(entry[0])
    return length_name

def donor_average(index):
    total_donations = 0
    for entry in donor_list[index][1]:
        total_donations += entry
        average_donation = total_donations / len(donor_list[index][1])
    return average_donation

def donor_total(index):
    total_donations = 0
    for entry in donor_list[index][1]:
        total_donations += entry
    return total_donations
    
def list_donors():
    for entry in donor_list:
        print(donor_list[entry][0])
        
def find_donor(str):
    for entry in donor_list:
        check = entry[0].lower()
        if check.find(str.lower()) > -1:
            return donor_list[donor_list.index(entry)]
    return False

def second_element(list):
    return list[1]

# ===== Main Elements =====

start_message = ('''
Choose from one of the following actions:
    a   Add a new donor
    d   Enter a new donation from an existing donor
    m   Mail a Thank You letter to a selected donor
    r   Report list of all donors, sorted by donation size
    x   Exit the program
''')

def add_donation():
    target_donor = []
    print('''
    First you'll need to select a donor to add a donation to.
    Enter a full or partial name to search for:
    ''')
    response = input().strip().lower()
    target_donor = find_donor(response)
    if target_donor != False:
        print("Add donation to:", target_donor[0])
        print("Is this correct? (y/n)")
        correct_response = input().strip().lower()
        if correct_response == "y":
            print('''
            Add a donation for {}
            Enter the donation amount:
            '''.format(response))
            donation = input().strip()
            if donation.isdigit() == True:
                index = donor_list.index(target_donor)
                donor_list[index][1].append(int(donation))
                return
            else:
                print("Sorry, but {} is not a number".format(response))
                return

def add_donor():
    print('''
    Enter the full name as Firstname Lastname
    Example: Alexander Hamilton
    ''')
    response = input().strip()
    print('''
    {}
    Is this correct? y/n
    '''.format(response))
    correct_response = input().strip().lower()
    if correct_response == "y":
        donor_list.append([response])
        print('''
        {} Added
        Enter the donation amount:
        '''.format(response))
        donation = input().strip()
        if donation.isdigit() == True:
            donor_list[-1].append([int(donation)])
            return
    else:
        print("Sorry, but {} is not a number".format(response))
        return

def mail_message(donor_info):
    donations = 0
    for entry in donor_info[1]:
        donations += entry
    first_name = donor_info[0][:donor_info[0].index(' ')]
    form = '''\
    Dear {name},
    Thank you so much for your generous donation of ${amount:0.2f}.
    Without such selfless contributions from people like you, we
    would not be able to continue this important work.
    We are all very appreciative of your support!
    
    Sincerely,
    
    Carl
    '''
    print(form.format(name=first_name, amount=donations))
    return

def mail_thank_you():
    target_donor = []
    print('''
    First you'll need to select a donor to mail.
    Enter a full or partial name to search for:
    ''')
    response = input().strip().lower()
    target_donor = find_donor(response)
    if target_donor != False:
        print("Mail to:", target_donor[0])
        print("Is this correct? (y/n)")
        correct_response = input().strip().lower()
        if correct_response == "y":
            print(mail_message(target_donor))
            return
    else:
        print("Sorry, but {} could not be found".format(response))
        return
    
def report_donors():
    temp_list = []
    name_length = donor_name_length()
    for i in range(len(donor_list)):
        temp_list.append([donor_list[i][0], donor_total(i), donor_average(i)])
    temp_list = sorted(temp_list, key=second_element, reverse=True)
    print("{}\t{}\t{}".format("Donor Name".ljust(name_length), "Total".rjust(10), "Average".rjust(10)))
    for donor in temp_list:
        print("{}\t{:10.2f}\t{:10.2f}".format(donor[0].ljust(name_length), donor[1], donor[2]))

def main():

    while True:

        print(start_message)
    
        response = input().strip().lower()

        if response == "a":
            print("This will allow you to add a new donor with their inital donation")
            add_donor()
        
        elif response == "d":
            print("This will allow you to enter a new donation for an existing donor")
            add_donation()
        
        elif response == "m":
            print("This will allow you to pick a donor, then send a Thank You message")
            mail_thank_you()
        
        elif response == "r":
            print("Report of all donors, sorted by donation size:")
            report_donors()

        elif response == "x":
            print("Exiting program")
            break
    
        else:
            print("try again")

  
if __name__ == "__main__":
    main()
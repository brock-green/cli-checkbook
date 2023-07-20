import csv
import time
import os

cols = ['credit', 'debit', 'timestamp']
    
                                                        #### CREDIT, DEBIT, BALANCE, EXIT FUNCTIONS ####

                                            # Credit function
def credit(inputvalue):
    '''
    '''
    if inputvalue.isdigit() == False:
        print('Invalid input. Please try again.')
        return checkbook()
    else:
        with open('checkbook_ledger.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=cols)
            writer.writerow(
            {
                'credit': inputvalue,
                'debit': 0,
                'timestamp': time.time()
            })
        print(f'\n${inputvalue} was added to your account.\n')
        return checkbook()

                                            # Debit Function
def debit(inputvalue):
    '''
    '''
    with open('checkbook_ledger.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writerow(
        {
                'credit': 0,
                'debit': inputvalue,
                'timestamp': time.time()
        })
    print(f'\n${inputvalue} was withdrawn from your account.\n')
    return checkbook()

                                            # Balance Function

def balance():
    '''
    '''
    with open('checkbook_ledger.csv', 'r') as f:
        content = csv.DictReader(f, fieldnames=cols)
        lines = [line for line in content][1:]
    print(f"\nYour account balance is ${sum([float(row['credit']) for row in lines]) - sum([float(row['debit']) for row in lines])}.\n")
    return checkbook()

                                            # Exit Function
def exit():
    print('Thanks, have a great day!')
    return quit()


                                            # Checkbook Function
def checkbook():
    onetwothreefour = input('What would you like to do?\n1) view current balance\n2) record a debit (withdraw)\n3) record a credit (deposit)\n4) exit\n\nYour choice?')
    if onetwothreefour == '1':
        balance()
    elif onetwothreefour == '2':
        #record a debit
        input_two = input('How much would you like to withdraw?')
        if input_two.isdigit() != True:
            print('\nInvalid response. Please input a number with digits.\n')
            checkbook()
        else:
            withdrawal = input_two
            debit(withdrawal)
    elif onetwothreefour == '3':
        #record a credit
        input_three = input('How much would you like to deposit?')
        if input_three.isdigit() != True:
            print('\nInvalid response. Please input a number with digits.\n')
            checkbook()
        else:
            deposit = input_three
            credit(deposit)
    elif onetwothreefour == '4':
        exit()
        # Before exit function save current balance to file
        # Create an exit function
    else:
        print('\nInvalid response. Please input a digit between 1 and 4.\n')
        return checkbook()

                                    #Begin Function
def check_create_csv():
    welcome = '\n~~~Welcome to your terminal checkbook!~~~\n'
    if os.path.exists('/Users/brockgreen/codeup-data-science/cli-checkbook/checkbook_ledger.csv') == False:
        print(welcome)
        cols = ['credit', 'debit', 'timestamp']
        with open('checkbook_ledger.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=cols)
            writer.writeheader()
    else:
        with open('checkbook_ledger.csv', 'r') as f:
            print(welcome)
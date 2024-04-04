"""Import the Account class from the Account.py file."""
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months, variable_3):
    #  Create an instance of the `SavingsAccount` class and pass in the balance and interest parameters.
    savings_account = Account(balance, 0)

    # Calculate interest earned
    interest_earned = balance * (interest_rate/100 * months/12)

    # Update savings account balance with interest earned
    updated_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    savings_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned, variable_3
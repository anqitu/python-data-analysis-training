# Q3
#
# Write a program that computes the net amount
# of a bank account based a transaction log from
# console input. The program will keep asking the user
# for transaction logs until the keyword 'exit'
# is provided by the user. The transaction log
# format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# balance: 500

if __name__ == "__main__":

    balance = 0
    while (True):
        transaction = input("Enter transaction log > ");

        # guard clause
        if (transaction == "exit"):
            break

        t = transaction.split()
        # type = t_split[0]
        # amount = t_split[1]
        type, amount = t

        if not (len(t) == 2 and type in ["D", "W"] and amount.isdigit()):
            print("Invalid log, try again")
            continue

        amount = float(amount)

        if (type == "D"):
            balance += amount
        elif (type == "W"):
            balance -= amount

        # balance += amount * (-1 if type == "W" else 1)

    print("balance: {}".format(balance))

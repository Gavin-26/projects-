import csv

# Class Definition
class TicketRecord:
    def __init__(self, date, ticketID, ticketsBought, method):
        self.date = date
        self.ticketID = ticketID
        self.ticketsBought = ticketsBought
        self.method = method

# Function to calculate income
def calculate_income(filename):
    totalWeekday = 0
    totalFriday = 0
    counter = 0

    # open the file
    file = open(filename, "r")
    reader = csv.reader(file)

    # open file to write Friday tickets
    fridayFile = open("Friday_Tickets.csv", "w", newline="")
    writer = csv.writer(fridayFile)
    writer.writerow(["TicketID", "TicketsBought"])

    # loop through each record (row) in the CSV
    for row in reader:
        # create TicketRecord object
        record = TicketRecord(*row)

        ticketID = record.ticketID
        ticketsBought = record.ticketsBought

        if ticketsBought.isdigit():
            ticketsBought = int(ticketsBought)

            # check for weekday tickets
            if ticketID =="W1" or ticketID == "W2" or ticketID == "W3" or ticketID == "T1" or ticketID == "T2" or ticketID == "T3":
                totalWeekday += ticketsBought * 5
                counter += 1

            # check for Friday tickets
            elif ticketID == "F1" or ticketID == "F2" or ticketID == "F3":
                totalFriday += ticketsBought * 10
                counter += 1
                writer.writerow([ticketID, ticketsBought])

    file.close()
    fridayFile.close()

    totalIncome = totalWeekday + totalFriday
    return totalWeekday, totalFriday, counter, totalIncome

# Function to find most popular method
def most_popular_method(path):
    file = open(path, "r")

    school_count = 0
    online_count = 0

    for line in file:
        data = line.strip().split(",")
        record = TicketRecord(*data)
        method = record.method

        if method == "S":
            school_count += 1
        elif method == "O":
            online_count += 1

    file.close()

    if school_count > online_count:
        return "The most popular way of buying tickets is School (S)"
    elif online_count > school_count:
        return "The most popular way of buying tickets is Online (O)"
    else:
        return "Both School (S) and Online (O) are equally popular"

# Main program
path = input("Enter the path to the CSV file: ")

weekday, friday, count, total = calculate_income(path)

print("Total Weekday Income = £", weekday)
print("Total Friday Income = £", friday)
print("Total Income Raised = £", total)

print(most_popular_method(path))

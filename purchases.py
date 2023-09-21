#this program asks users for input data and puts the data into two lists using
#append in a loop. includes a funtion which adds tax and returns a new list with
#sales tax added. Then, define an empty dictionary and add each customer as a key

#inputs
num_purchases = int(input("Number of purchases: "))
sales_tax = float(input("Sales tax: "))

#global variables
customer_list = []
cost_list = []
cost_list_tax = []
dictionary = {}

#loop with append
for i in range(num_purchases):
    temp_customer = input("Customer: ")
    temp_cost = int(input("Cost: "))
    customer_list.append(temp_customer)
    cost_list.append(temp_cost)

#function to add tax
def add_tax(my_list, tax):
    for i in range(len(my_list)):
        tax_cost = my_list[i]*(1+tax)
        cost_list_tax.append(tax_cost)

#adds the tax
add_tax(cost_list, sales_tax)

#adds to dictionary
for i in range(len(customer_list)):
    dictionary[customer_list[i]] = cost_list_tax[i]

#prints dictionary
print(dictionary)

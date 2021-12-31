"""
2 important Python keywords:
Usually placed inside a loop

Break
Continue
"""
#cars status which are in production
cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

#iterating over list:
# for status in cars:
#     if status == "faulty":
#         print("Stopping the production line!")
#         break #stops the for loop
#     else:
#         print(f'This car is {status}.')
#         print("Shipping new car to customer")

"""
Output is:
This car is ok.
Shipping new car to customer
This car is ok.
Shipping new car to customer
This car is ok.
Shipping new car to customer
Stopping the production line!
"""
for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue # jumps back to start of loop without printing the 2 statements below
    print(f'This car is {status}.')
    print("Shipping new car to customer")
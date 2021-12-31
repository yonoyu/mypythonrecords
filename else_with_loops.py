"""
The else block just after for/while loop is executed only 
when the loop is NOT terminated by a break statement.

count = 0
while (count < 1):   
    count = count+1
    print(count)
    break
else:
    print("No Break")

Output: 1

This else executes only if break is NEVER
reached and loop terminated after all iterations.
"""

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break #stops the for loop
    print(f'This car is {status}.')
    print("Shipping new car to customer")
else:
    print("All cars built successfully. No faulty cars!")
"""
This car is ok.
Shipping new car to customer
This car is ok.
Shipping new car to customer
This car is ok.
Shipping new car to customer
Stopping the production line!

if the for loop did not encounter a 'break' (no faulty cars), 
the body in the else block will be executed!

Shipping new car to customer
This car is ok.
Shipping new car to customer
This car is ok.
Shipping new car to customer
This car is ok.
Shipping new car to customer
All cars built successfully. No faulty cars!
"""

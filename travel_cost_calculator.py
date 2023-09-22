# Index Number: EG/2020/4176
# Name: Samarakoon P. G. C.
from csv import *

# dictionaries for store data for functions
a = {}
b = {}
c = {}
"""
file - get data from csv
No returns
"""

def hotel_Rates(file):  
    with open(file) as hotel:
        r = reader(hotel)
        for row in r:
            a[row[0]] = float(row[1])
"""
file - get data from csv
No returns
"""
def exchange_Rates(file): 
    with open(file) as exchange:
        r = reader(exchange)
        for row in r:
            b[row[0].upper()] = float(row[1]) * 1 
"""
file - get data from csv
No returns
"""
def flight_Cost(file):
    with open(file) as flight:
        r = reader(flight)
        for row in r:
            c[row[0]] = float(row[1])

def main():
    hotel_Rates('data/hotel_rates.csv')
    exchange_Rates('data/exchange_rates.csv')
    flight_Cost('data/flight_costs.csv')

    destination = input("Enter your destination: ").upper()

    flight = c.get(destination, 0.0)
    hotel = a.get(destination, 0.0)

    days = int(input("Enter your stay duration in days: "))
    hotel *= days
    total = flight + hotel

    print(f"Flight cost: USD {flight:.2f}")
    print(f"Hotel cost for {days} days: USD {hotel:.2f}")
    print(f"Total: USD {total:.2f}")

    currency = input(f"Select your currency for final price estimation ({', '.join(b.keys())}): ")

    price = total * b[currency]
    print(f"Total in {currency}: {price:.2f}")

if __name__ == "__main__":
    main()

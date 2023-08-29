#!/usr/bin/env python3
import ipdb
from customer import Customer
from restaurant import Restaurant
from review import Review


if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    brian = Customer("Brian","B")
    chris = Customer("Chris", "C")

    star = Restaurant("StarBucks")
    kfc = Restaurant("KFC")
    
    review1 = Review("Brian", "B", "KFC", 7)
    review2 = Review("Chris", "C", "StarBucks", 9)
    review3 = Review("Brian", "B", "KFC", 4)
    review4 = Review("Chris", "C", "StarBucks", 10)
    
    print("Customers: ")
    for i in Customer.all_customer():
        print(Customer.get_full_name(i))
    
    print(" ")
    print("Restaurants: ")
    for i in Restaurant.all_rest():
        print(i._name)

    print(" ")
    print("Reviews:")
    for i in Review.all_reviews():
        print(f"{i._customer}: {i._restaurant} - {i.review}")

    print(" ")
    print("Customer review count: ")

    print(" ")
    given_name = "Chris"
    print(f"Customer names similar to: {given_name}: ")
    print(Customer.find_all_by_given_name(given_name))

    print(" ")
    cust_name = "Brian B"
    print(f"Find customer: {cust_name}")
    print(Customer.find_by_name(cust_name))
    

    print(" ")
    print("Average Star Ratings: ")
    







# DO NOT REMOVE THIS
    ipdb.set_trace()
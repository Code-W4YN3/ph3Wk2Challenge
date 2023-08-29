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
    review3 = Review("Brian", "B", "StarBucks", 4)
    review4 = Review("Chris", "C", "KFC", 10)
    
    print("Customer: ")
    print(f"customer given_name: {Customer.given_name(brian)}")
    print(f"customer family_name: {Customer.family_name(brian)}")
    print(f"customer full_name: {Customer.get_full_name(brian)}")
    print("customer all: ")
    for i in Customer.all_customer():
        print(Customer.get_full_name(i))

    print(" ")
    print("Restaurant: ")
    print(f"restaurant name: {Restaurant.get_name(kfc)}")
    print("restaurant all: ")
    for i in Restaurant.all_rest():
        print(Restaurant.get_name(i))

    print(" ")
    print("Review: ")
    print(f"review rating: {Review.restaurant(review1)} - {Review.rating(review1)}")
    print("review all: ")
    for i in Review.all_reviews():
        print(f"{Review.customer(i)}: {Review.restaurant(i)} - {Review.rating(i)}")

    print(" ")
    print(f"review customer: {Review.customer(review1)}")
    print(f"review restaurant: {Review.restaurant(review1)}")

    print(" ")
    rest_name = "KFC"
    print(f"Restaurant Reviews for {rest_name}: ")
    for i in Review.all_reviews():
        if(Review.restaurant(i) == rest_name):
            print(f"{Review.customer(i)}: {Review.rating(i)}")
    print(f"Customers who reviewed {rest_name}: ")
    unique_cust = []
    for i in Review.all_reviews():
        if(Review.restaurant(i) == rest_name):
            unique_cust.append(Review.customer(i))
    print(list(set(unique_cust)))

   

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
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
    









# DO NOT REMOVE THIS
    ipdb.set_trace()
from review import Review

class Customer:
    all_cus = []

    @classmethod
    def all_customer(cls):
        return cls.all_cus
    
    @classmethod
    def find_by_name(cls,name):
        for i in cls.all_cus:
            if i.get_full_name == name:
                return i 
            return None 
        
    @classmethod
    def find_all_by_given_name(cls,name):
        for i in cls.all_cus:
            if i.given_name == name:
                return i

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_cus.append(self.full_name)

    def first_name(self):
        return self.given_name
    
    def last_name(self):
        return self.family_name

    def get_full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    def my_reviews(self, review):
        self.reviews.append(review)

    def count_my_reviews(self):
        return len(self.reviews)

    


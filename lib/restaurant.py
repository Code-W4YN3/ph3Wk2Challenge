from review import Review

class Restaurant:
    all_restaurants = []

    @classmethod
    def all_rest(cls):
        return cls.all_restaurants

    def __init__(self, name):
        self._name = name
        self._reviews = []
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self._name
    
    def reviews(self):
        return self._reviews
        
    def customers(self):
        customers_set = set()
        for review in self._reviews:
            customers_set.add(review.customer())
        return list(customers_set)

    def average_star_rating(self):
        if (len(self._reviews) == 0):
            return 0
        total_rating = 0
        for i in Review.all_reviews():
            if(i.restaurant == self._name):
                total_rating += i.review

        return total_rating / len(self._reviews)

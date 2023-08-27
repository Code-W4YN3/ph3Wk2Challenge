class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews = []

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
        total_rating = sum(self._reviews)
        return total_rating / len(self.reviews)

class Review:
    all_rev = []

    @classmethod
    def all_reviews(cls):
        return cls.all_rev

    def __init__(self, given_name, family_name, restaurant, review:int):
        self._customer = f"{given_name} {family_name}"
        self._restaurant = restaurant
        self.review = review
        Review.all_rev.append(self)

    def rating(self):
        return self.review

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

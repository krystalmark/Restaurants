class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews = []

    def name(self):
        return self._name

    def add_review(self, review):
        self._reviews.append(review)

    def average_star_rating(self):
        total_rating = sum(review.rating() for review in self._reviews)
        num_reviews = len(self._reviews)
        if num_reviews == 0:
            return 0.0
        return total_rating / num_reviews

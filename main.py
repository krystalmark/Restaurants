from lib.customer import Customer
from lib.restaurant import Restaurant
from lib.review import Review

if __name__ == "__main__":
    red_ginger = Restaurant("Red Ginger")
    bore_wores = Restaurant("Bore Wores")

    krystal_mark = Customer("Krystal", "Mark")
    triza_wanjugu = Customer("Triza", "Wanjugu")

    krystal_mark.add_review(red_ginger, 9)
    krystal_mark.add_review(bore_wores, 6)

    triza_wanjugu.add_review(red_ginger, 8)
    triza_wanjugu.add_review(bore_wores, 5)

    print(red_ginger.name())
    print(bore_wores.name())
    print(krystal_mark.given_name())
    print(triza_wanjugu.given_name())
    print("{:.1f}".format(red_ginger.average_star_rating()))
    print("{:.1f}".format(bore_wores.average_star_rating()))
    print([restaurant.name() for restaurant in krystal_mark.restaurants()])
    print([restaurant.name() for restaurant in triza_wanjugu.restaurants()])

    print("Number of reviews by Krystal Mark:", krystal_mark.num_reviews())

    found_customer = Customer.find_by_name("Krystal Mark")
    if found_customer:
        print("Matching customer found:", found_customer.full_name())
    else:
        print("No matching customer found.")

    matching_customers = Customer.find_all_by_given_name("Triza")
    if matching_customers:
        print("Matching customers found:")
        for customer in matching_customers:
            print(customer.full_name())
    else:
        print("No matching customers found.")

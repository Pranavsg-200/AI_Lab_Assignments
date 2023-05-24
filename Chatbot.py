def get_book():
    books = ["DSA", "OOP", "ML", "AI", "CC"]
 
    print("Hello! Welcome to our book shop. How can I assist you today?")
    print("Books that are available now are:",books)
 
    book = input("Which book are you looking for? ")
 
    book = book.upper()
    while book not in books:
 
        print("Sorry, we don't have that book. Please choose from the available options.")
        book = input("Which book would you like to buy? ")
        book = book.upper()
    return book
 
def get_quantity():
    quantity = input("How many books would you like to buy? ")
    while not quantity.isdigit() or int(quantity) <= 0:
        print("Please enter a valid quantity.")
        quantity = input("How many books would you like to buy? ")
    return int(quantity)
 
def calculate_price(book, quantity):
    prices = {"DSA": 100, "OOP": 150, "ML": 300, "AI": 450, "CC": 200}
    price = prices[book] * quantity
    return price
 
def main():
 
 
    book=get_book()
    quantity = get_quantity()
    price = calculate_price(book, quantity)
    print(f"The total price for {quantity} {book}(s) is Rs {price}")
    print("Thank you for shopping with us!")
 
# Run the chatbot
main()

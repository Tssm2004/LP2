print("Welcome to ShopBot! How can I help you today?")

while True:
    user = input("You: ").lower()

    if "price" in user:
        print("Bot: Our prices vary depending on the product. Can you specify?")
    elif "return" in user:
        print("Bot: You can return products within 30 days of delivery.")
    elif "delivery" in user:
        print("Bot: Delivery usually takes 3-5 business days.")
    elif "bye" in user or "exit" in user:
        print("Bot: Thank you for visiting! Have a great day!")
        break
    else:
        print("Bot: I'm sorry, I didn't understand that. Could you please rephrase?")

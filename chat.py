from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("My Bot")

convo = [
    'Where is my order?',
    'Order Update: Your order (Chawal, Daal, Vim Bar, Achar) of Rs. 777/- has been Shipped and will be delivered within 1 hour. Please keep your phone in Switch on mode',
    'order?',
    'Place Order',
    'Your order has been placed. Order ID: 585558. Thank you for Shopping',
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Rohit Bot , i am created by Jyoti Prakash',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in Guwahati',
    'In which language you talk?',
    'I mostly talk in english'
]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

 #answer = bot.get_response("what is your name?")
 #print(answer)

print("Welcome to Rohit Ecommerce")
while True:
    query = input()
    if query == 'exit':
        break
    answer = bot.get_response(query)
    print("Rohit Bot : ", answer)

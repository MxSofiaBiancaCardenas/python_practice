# def greet_user(first_name): # function(parameter); parameter = placeholder
#     # name = "John"
#     print(f'Hi {first_name}!')
#     # print('Hi there!')
#     print('Welcome aboard')


# print("Start")
# greet_user("John") # "John" -> argument - actual input that we supply to the function
# greet_user("Mary")
# print("Finish")

# # Positional Arguments - position is important
# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')

# print("Start")
# greet_user("John", "Smith") 
# print("Finish")

# # Keyword Arguments - position is not important
# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')

# print("Start")
# greet_user(last_name="Smith", first_name="John") 
# print("Finish")

# # Return Statement
# def square(number):
#     return number * number
#     # print(number * number)
#     # by default all functions return None

# # result = square(3)
# # print(result)
# print(square(3))

# Reusable Function
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "☹️"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">")
print(emoji_converter(message))
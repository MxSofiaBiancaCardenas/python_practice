# customer = {
#     "name": "John Smith", # key-value pair
#     "age": 30,
#     "is_verified": True
# }
# # customer["name"] = "Jack Smith"
# print(customer["name"])
# print(customer.get("name"))
# print(customer.get("birthdate", "Jan 1 1980")) # we can supply a default value
# customer["birthdate"] = "Jan 1 1980"
# print(customer["birthdate"])

# # Number Converter
# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)

# Emoji Converter
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "☹️"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
message = input("> ")
words = message.split(" ")
emoji = {
    ":)" : "😊",
    ":(" : "😞"
}
output = " "
for word in words:
    otput = emoji.get(word, word) + " "

print(output)
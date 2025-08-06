sentence = "the sky is blue "

flipped_sentence = ""
stack = []

for char in sentence:
    if char != ' ':
        stack.append(char)
    else:
        while stack:
            flipped_sentence += stack.pop()
            flipped_sentence += ' ' 

while stack:
    flipped_sentence += stack.pop()

print(" Flipped sentence:", flipped_sentence)
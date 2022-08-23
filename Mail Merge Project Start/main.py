import shutil
INPUT_DIRECTORY = r"./Input/Letters/starting_letter.txt"
search_text = "[name]"
replace_text = []
with open(r"./Input/Names/invited_names.txt") as F:
    data = F.read()
    Text = ""
    for text in data:
        if text != "\n":
            Text += text
        else:
            replace_text.append(Text)
            Text = ""
for i in range(0,len(replace_text)):
    shutil.copyfile(INPUT_DIRECTORY, f"./Output/ReadyToSend/invited_to_a_party_{replace_text[i]}")
    shutil.copy(INPUT_DIRECTORY, f"./Output/ReadyToSend/invited_to_a_party_{replace_text[i]}")
    with open(f"./Output/ReadyToSend/invited_to_a_party_{replace_text[i]}", 'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text[i])
    with open(f"./Output/ReadyToSend/invited_to_a_party_{replace_text[i]}", 'w') as file:
        file.write(data)
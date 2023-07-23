with open("./Input/Names/invited_names.txt",'r') as invited_names:
    names = invited_names.read().split('\n')
with open("./Input/Letters/starting_letter.txt", 'r') as invite_message:
    invitation = invite_message.read()

for name in names:
    with open(f".././Mail Merge Project End/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", 'w') as message:
        message.write(invitation.replace("[name]", name, 1))

import sys
import keyboard
import pyperclip

Text_File = open("LAccounts.txt", 'r+')  # Opens the text file

Line = Text_File.readlines()  # Reads the lines of the text file

normal_bind = 'ctrl'

user = [0]
password = [0]
temp = ''

for elem in Line:
    n = str(elem)
    if n.lower().__contains__('user:') or n.lower().__contains__('password:'):
        temp = ''
        for elem in n:
            if elem != ' ':
                temp += elem
            if temp.lower() == 'user:' or temp.lower() == 'password:':
                temp = ''
        if n.lower().__contains__('user:'):
            user.append(temp)
        else:
            password.append(temp)
    if n.lower().__contains__('Password Bind:'):
        temp = ''
        for ele in n:
            if ele != ' ':
                temp += ele
        if temp != 'ctrl':
            normal_bind = temp


was_pressed0 = False
was_pressed1 = False

was_pressed2 = False
was_pressed3 = False

was_pressed4 = False
was_pressed5 = False

was_pressed6 = False
was_pressed7 = False

was_pressed8 = False
was_pressed9 = False

while True:
    try:
        if keyboard.is_pressed(normal_bind + ' + 1'):
            if not was_pressed0:
                pyperclip.copy(user[0])
                was_pressed0 = True
        else:
            was_pressed0 = False
        if keyboard.is_pressed(normal_bind + ' + 2'):
            if not was_pressed1:
                pyperclip.copy(password[0])
                was_pressed1 = True
        else:
            was_pressed1 = False

        if keyboard.is_pressed(normal_bind + ' + 3'):
            if not was_pressed2:
                pyperclip.copy(user[1])
                was_pressed2 = True
        else:
            was_pressed2 = False
        if keyboard.is_pressed(normal_bind + ' + 4'):
            if not was_pressed3:
                pyperclip.copy(password[1])
                was_pressed3 = True
        else:
            was_pressed3 = False

        if keyboard.is_pressed(normal_bind + ' + 5'):
            if not was_pressed4:
                pyperclip.copy(user[2])
                was_pressed4 = True
        else:
            was_pressed4 = False

        if keyboard.is_pressed(normal_bind + ' + 6'):
            if not was_pressed4:
                pyperclip.copy(password[2])
                was_pressed5 = True
        else:
            was_pressed5 = False

        if keyboard.is_pressed(normal_bind + ' + 7'):
            if not was_pressed5:
                pyperclip.copy(user[3])
                was_pressed5 = True
        else:
            was_pressed5 = False

        if keyboard.is_pressed(normal_bind + ' + 8'):
            if not was_pressed6:
                pyperclip.copy(password[3])
                was_pressed6 = True
        else:
            was_pressed6 = False

        if keyboard.is_pressed(normal_bind + ' + 9'):
            if not was_pressed7:
                pyperclip.copy(user[4])
                was_pressed7 = True
        else:
            was_pressed7 = False

        if keyboard.is_pressed(normal_bind + ' + 0'):
            if not was_pressed8:
                pyperclip.copy(password[4])
                was_pressed8 = True
        else:
            was_pressed8 = False

        if keyboard.is_pressed('ctrl + alt + end'):
            sys.exit()
    except IndexError:
        continue

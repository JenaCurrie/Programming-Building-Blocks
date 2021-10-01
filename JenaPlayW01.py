color = input ('What is your favorite color today? ') 
if color in('cyan' , 'light blue' , 'turquoise' , 'aqua'): 
    print('\033[38;5;45m Great choice! I love ' + color + ', too! \033[0;0m')
elif color in('red' , 'scarlet' , 'orange' , 'red orange' , 'ruby'): 
    print('\033[38;5;196m Great choice! I love ' + color + ', too!\033[0;0m')
elif color in('blue' , 'navy' , 'dark blue' , 'saffire' , 'indigo', 'blurple'): 
    print('\033[1;34;40m Great choice! I love ' + color + ', too!\033[0;0m')
elif color in('black' , 'grey' , 'dark grey' , 'gray' , 'dark gray'): 
    print('\033[1;37;47m Great choice! I love ' + color + ', too!\033[0;0m')
elif color in('green' , 'emerald' , 'lime' , 'light green'): 
   print('\033[1;32;40m Great choice! I love ' + color + ', too!\033[0;0m')
elif color == 'yellow': 
    print('\033[1;33;40m Great choice! I love ' + color + ', too!\033[0;0m')
elif color in('purple' , 'violet'): 
    print('\033[38;5;92m Great choice! I love ' + color + ', too!\033[0;0m')
elif color in('hot pink' , 'magenta'):
    print('\033[38;5;200m Great choice! I love ' + color + ', too!\033[0;0m')
elif color in('pink' , 'light pink' , 'baby pink' , 'pale pink'): 
    print('\033[38;5;211m Great choice! I love ' + color + ', too!\033[0;0m')
else:
    print('Great choice! I love ' + color + ', too!')
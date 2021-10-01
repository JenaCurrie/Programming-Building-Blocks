#The other day, I was really in trouble. It all started when I saw a very
#[adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all 
# I could think to do was to [verb] over and over. Miraculously, 
# that caused it to stop, but not before it tried to [verb] 
# right in front of my family.
adjective = input ('\033[4mGive me an adjective:\033[0;0m ')
adjective2 = input ('\033[4mAnother adjective:\033[0;0m ')
animal = input ('\033[4mWhat is your favorite animal?\033[0;0m ')
verb = input ('\033[4mGive me an "-ing" verb:\033[0;0m ')
exclamation = input ('\033[4mSomething you would shout:\033[0;0m ')
adverb = input ('\033[4mTime for an adverb:\033[0;0m ')
verb2 = input ('\033[4mAnother verb:\033[0;0m ')
verb3 = input ('\033[4mOne more verb:\033[0;0m ')
print('\n')
print('\033[1mThe other day, I was really in trouble. It all started when I saw a very')
print(f'\033[1m\033[3m\033[4m{adjective}\033[0m,\033[1m \033[3m\033[4m{adjective2}\033[0m \033[1m\033[3m\033[4m{animal}\033[0m \033[1m\033[3m\033[4m{verb}\033[0m \033[1mdown the hallway. "\033[3m\033[4m{exclamation.upper()}!\033[0m\033[1m" I yelled. But all')
print(f'\033[1mI could think to do was to \033[3m\033[4m{adverb}\033[0m \033[1m\033[3m\033[4m{verb2}\033[0m\033[1m over and over. Miraculously,')
print(f'\033[1mthat caused it to stop, but not before it tried to \033[3m\033[4m{verb3}\033[0m')
print('\033[1mright in front of my family.\033[0m')
print('\n')
house = input ('What is your Hogwarts House? ')
if house in('Ravenclaw' , 'Ravinclaw' , 'ravenclaw' , 'ravinclaw'):
    trait = 'wise'
elif house in('Griffyndor', 'Gryffindor' , 'Griffendor' , 'griffyndor' , 'gryffindor' , 'griffendor'):
    trait = 'brave'
elif house in('Hufflepuff' , 'Huffelpuff' , 'huffelpuff' , 'hufflepuff'):
    trait = 'loyal'
elif house in('Slytherin' , 'Slitherin' , 'slytherin' , 'slitherin'):
    trait = 'cunning'    
print('Welcome to Hogwarts, ' + trait + ' ' + house.capitalize() + '!')
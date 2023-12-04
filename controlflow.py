
color = ''
while color != 'quit':
    color = input('Enter "green", "yellow", "red": ').lower()
    print(f'The user entered {color}')
    if color == 'green':
        print('Go!')
    elif color == 'yellow':
        print('Slow Down!')
    elif color == 'red':
        print('Stop!')
    else:
        print('Bogus!')



'''Below that code, write an if...elif...else statement that prints out one of the following messages:

If green is entered, print the message Go!
If yellow is entered, print the message Slow Down!
If red is entered, print the message Stop!
If anything else is entered, print the message Bogus!
Test the code by running it in the repl.'''
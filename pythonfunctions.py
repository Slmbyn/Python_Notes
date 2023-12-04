'''Python has lambda functions instead of arrow functions
Python lambda functions are very much like Arrow Functions in JavaScript:

They implicitly return a single expression’s value.
They are expressions so they are commonly used as “inline” arguments.
They can be assigned to a variable.
However, unlike arrow functions, they cannot have any code block - just a single expression that has its result implicitly returned.

For example:

// JavaScript
const nums = [1, 3, 2, 6, 5];
let odds = nums.filter(num => num % 2);'''

# Python
nums = [1, 3, 2, 6, 5]
odds = list( filter(lambda num: num % 2, nums) )
# Lambda functions are nifty when using Python functions such as 
# map() and filter() - just like how arrow functions are nifty when using array iterator methods.


# Python’s * Parameter Specifier (*args)
# Using the * (“star”) specifier in a parameter list allows us to pass in a varying number of positional arguments into a function:

def fn(*args):
  print( type(args) )
  for arg in args:
    print(arg)

fn(1, 2, 'SEI')
''' Output:
<class 'tuple'>
1
2
SEI
'''
# The identifier used with *, i.e., args, can be anything, however by convention, use args.

# Always use the *args parameter after any required positional parameters. For example:

def dev_skills(dev_name, *args):
  dev = {'name': dev_name, 'skills': []}
  # args will be a tuple
  for skill in args:
    dev['skills'].append(skill)
  return dev

print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))
# -> {'name': 'Alex', 'skills': ['HTML', 'CSS', 'JavaScript', 'Python']}

# Or, why not use the list() function to convert the args tuple into a list…
def dev_skills(dev_name, *args):
  dev = {'name': dev_name, 'skills': list(args)}
  return dev

'''Pythons '**' Parameter Specifier (**kwargs)
First, the reason we name the parameter kwargs is because it stands for keyword arguments.

A keyword argument is an argument with a name, and this is why keyword arguments are 
also referred to as named arguments.

By adding **kwargs at the end of the parameter list, we can access any number of keyword arguments.
'''
# For example:
def dev_skills(dev_name, **kwargs):
  # kwargs will be a dictionary! (meaning it will be an embedded dictionary and will have a key-value pair!)
  dev = {'name': dev_name, 'skills': kwargs}
  return dev

print(dev_skills('Jackie', HTML=5, CSS=3, JavaScript=4, Python=2))

# Combining Required Positional, Optional Positional (*args) & Keyword (**kwargs) Arguments:
'''You can use all three types of parameters in the same function, but 
    they have to be defined in the following order:     '''

def arg_demo(pos1, pos2, *args, **kwargs):
  print(f'Positional params: {pos1}, {pos2}')
  print('*args:')
  for arg in args:
    print(' ', arg)
  print('**kwargs:')
  for keyword, value in kwargs.items():
    print(f'  {keyword}: {value}')

arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')

'''
Output:

Positional params: A, B
*args:
  1
  2
  3
**kwargs:
  color: purple
  shape: circle
'''

'''
EXTRA *args & **kwargs INFO:
https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/

'''
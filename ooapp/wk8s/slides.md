# Programming: Object-Oriented Approach 👨‍💻️ 
### Object-Oriented Programming
* Press `Space` to navigate through the slides
* Use `Shift+Space` to go back
* Save as **PDF**:
  * Open **Chrome** then **<a href="?print-pdf#/">click here</a>**
  * Press **Ctrl+P**/**Cmd+P** to print
    * Destination: **Save as PDF**
    * Layout: **Landscape**
  * Press **Save** button
---
# Object Oriented Programming

* Object Oriented Programming (OOP) tends to be one of the major obstacles for beginners when they are first starting to learn Python.

* There are many, many tutorials and lessons covering OOP so feel free to Google search other lessons, and I have also put some links to other useful tutorials online at the end of this lecture.

* We will construct our knowledge of OOP in Python by building on the following topics:
	* Objects
	* Using the *class* keyword
	* Creating class attributes
	* Creating methods in a class
	* Learning about Inheritance
	* Learning about Polymorphism
	* Learning about Special Methods for classes
---
# Object Oriented Programming
* Lets start the lesson by remembering about the Basic Python Objects. For example:

```python
lst = [1,2,3]
```

* Remember how we could call methods on a list?

```python
lst.count(2)
```

* What we will basically be doing in this lecture is exploring how we could create an Object type like a list. We've already learned about how to create functions. So let's explore Objects in general:
---
## Objects
* In Python, *everything is an object*.
* Remember from previous lectures we can use type() to check the type of object something is:

```python
print(type(1))
print(type([]))
print(type(()))
print(type({}))
```

* So we know all these things are objects, so how can we create our own Object types? That is where the <code>class</code> keyword comes in.
---
## class
* User defined objects are created using the <code>class</code> keyword.
* The class is a blueprint that defines the nature of a future object.
* From classes we can construct instances.
* An instance is a specific object created from a particular class.
* For example, above we created the object <code>lst</code> which was an instance of a list object. 
---
## class
* Let see how we can use <code>class</code>:

```python
# Create a new object type called Sample
class Sample:
    pass

# Instance of Sample
x = Sample()

print(type(x))
```

* By convention we give classes a name that starts with a capital letter. Note how <code>x</code> is now the reference to our new instance of a Sample class. In other words, we **instantiate** the Sample class.

* Inside of the class we currently just have pass. But we can define class attributes and methods.
---
## class
* An **attribute** is a characteristic of an object.
* A **method** is an operation we can perform with the object.

* For example, we can create a class called Dog.
* An attribute of a dog may be its breed or its name, while a method of a dog may be defined by a .bark() method which returns a sound.

* Let's get a better understanding of attributes through an example.
---
## Attributes
* The syntax for creating an attribute is:
```python
self.attribute = something
```
* There is a special method called:
```python
__init__()
```
---
## Attributes
* The `__init__()` is used to initialize the attributes of an object. For example:

```python
class Dog:
    def __init__(self,breed):
        self.breed = breed
        
sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')
```
---
## Attributes
* Lets break down what we have in the code.
* The special method is called automatically right after the object has been created:
```python
    def __init__(self, breed):
```
* Each attribute in a class definition begins with a reference to the instance object.
* It is by convention named self.
* The breed is the argument.
* The value is passed during the class instantiation.
```python
     self.breed = breed
```
---
## Attributes
* Now we have created two instances of the Dog class.
* With two breed types, we can then access these attributes like this:

```python
sam.breed
frank.breed
```
* Note how we don't have any parentheses after breed; this is because it is an attribute and doesn't take any arguments.
---
## Attributes
* In Python there are also *class object attributes*.
* These Class Object Attributes are the same for any instance of the class.
* For example, we could create the attribute *species* for the Dog class.
* Dogs, regardless of their breed, name, or other attributes, will always be mammals.
* We apply this logic in the following manner:

<div style="float:left;width:50%;">
	
```python
class Dog:

	# Class Object Attribute
	species = 'mammal'

	def __init__(self,breed,name):
	    self.breed = breed
	    self.name = name

sam = Dog('Lab','Sam')

sam.name

sam.species
```

</div>
<div style="float: right;width:50%;">

* Note that the Class Object Attribute is defined outside of any methods in the class.
* Also by convention, we place them first before the init.

</div>

---

## Methods

* Methods are functions defined inside the body of a class.
* They are used to perform operations with the attributes of our objects.
* Methods are a key concept of the OOP paradigm.
* They are essential to dividing responsibilities in programming, especially in large applications.

* You can basically think of methods as functions acting on an Object that take the Object itself into account through its *self* argument.
---
## Methods
* Let's go through an example of creating a Circle class:

```python
class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2

c = Circle()

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())
```
---
## Methods
* In the \__init__ method, in order to calculate the area attribute, we had to call `Circle.pi`.
* This is because the object does not yet have its own .pi attribute, so we call the Class Object Attribute pi instead.
* In the setRadius method, however, we'll be working with an existing Circle object that does have its own pi attribute.
* Here we can use either `Circle.pi` or `self.pi`.
* Now let's change the radius and see how that affects our Circle object:

```python
c.setRadius(2)

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())
```

* Notice how we used self. notation to reference attributes of the class within the method calls.
---
## Inheritance

* Inheritance is a way to form new classes using classes that have already been defined.
* The newly formed classes are called derived classes, the classes that we derive from are called base classes.
* Important benefits of inheritance are code reuse and reduction of complexity of a program.
* The derived classes (descendants) override or extend the functionality of base classes (ancestors).
---
## Inheritance
* Let's see an example by incorporating our previous work on the Dog class:

```python
class Animal:
    def __init__(self):
        print("Animal created")
    def whoAmI(self):
        print("Animal")
    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def whoAmI(self):
        print("Dog")
    def bark(self):
        print("Woof!")

d = Dog()
d.whoAmI()
d.eat()
d.bark()
```
---
## Inheritance
* In this example, we have two classes: Animal and Dog.
* The Animal is the base class, the Dog is the derived class. 
* The derived class inherits the functionality of the base class. 
	* It is shown by the `eat()` method. 
* The derived class modifies existing behavior of the base class.
	* shown by the `whoAmI()` method. 

* Finally, the derived class extends the functionality of the base class, by defining a new `bark()` method.

---
## Polymorphism

* We've learned that while functions can take in different arguments, methods belong to the objects they act on.
* In Python, *polymorphism* refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety of different objects might be passed in.

---
## Polymorphism

* The best way to explain this is by example:

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name+' says Woof!'
    
class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name+' says Meow!' 
    
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())
```
---
## Polymorphism
* Here we have a Dog class and a Cat class, and each has a `.speak()` method.
* When called, each object's `.speak()` method returns a result unique to the object.

* There a few different ways to demonstrate polymorphism. First, with a for loop:

```python
for pet in [niko,felix]:
    print(pet.speak())
```

* Another is with functions:

```python
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)
```
* In both cases we were able to pass in different object types, and we obtained object-specific results from the same mechanism.

---
## Polymorphism
* A more common practice is to use abstract classes and inheritance.
* An abstract class is one that never expects to be instantiated.
* For example, we will never have an Animal object, only Dog and Cat objects, although Dogs and Cats are derived from Animals:

```python
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):  
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):
    def speak(self):
        return self.name+' says Meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())
```
---
## Polymorphism
* Real life examples of polymorphism include:
	* opening different file types – different tools are needed to display Word, pdf and Excel files
	* adding different objects – the `+` operator performs arithmetic and concatenation

---
## Special Methods
* Finally let's go over special methods.
* Classes in Python can implement certain operations with special method names.
* These methods are not actually called directly but by Python specific language syntax.
---
## Special Methods
* For example let's create a Book class:

```python
class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book is destroyed")

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print(len(book))
del book
```
---
## Special Methods
**The `__init__()`, `__str__()`, `__len__()` and `__del__()` methods**
* These special methods are defined by their use of underscores.
* They allow us to use Python specific functions on objects created through our class.

---
## Readings
For more great resources on this topic, check out:
* [Jeff Knupp's Post](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
* [Mozilla's Post](https://developer.mozilla.org/en-US/Learn/Python/Quickly_Learn_Object_Oriented_Programming)
* [Tutorial's Point](http://www.tutorialspoint.com/python/python_classes_objects.htm)
* [Official Documentation](https://docs.python.org/3/tutorial/classes.html)
---

## Practical Work

#### Problem 1
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

```python
class Line:
    def __init__(self,coor1,coor2):
        pass
    def distance(self):
        pass
    def slope(self):
        pass
```

```python
# EXAMPLE OUTPUT
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance() # 9.433981132056603

li.slope() # 1.6
```

---
#### Problem 2

* Fill in the class 

```python
class Cylinder:
    def __init__(self,height=1,radius=1):
        pass        
    def volume(self):
        pass    
    def surface_area(self):
        pass
```

```python
# EXAMPLE OUTPUT
c = Cylinder(2,3)

c.volume() # 56.52

c.surface_area() # 94.2
```

---

#### Problem 3

* For this exercise, create a bank account class that has two attributes:
	* owner
	* balance
* And two methods:
	* deposit
	* withdraw
* As an added requirement, withdrawals may not exceed the available balance.

---

#### Problem 3

* Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

```python
class Account:
    pass
```

```python
# 1. Instantiate the class
acct1 = Account('Jose',100)
```

```python
# 2. Print the object
print(acct1) # Account owner: Jose, Account balance: €100
```

```python
# 3. Show the account owner attribute
acct1.owner # 'Jose'
```

```python
# 4. Show the account balance attribute
acct1.balance # 100
```

```python
# 5. Make a series of deposits and withdrawals
acct1.deposit(50) # Deposit Accepted
acct1.withdraw(75) # Withdrawal Accepted
```

```python
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500) # Funds Unavailable!
```
---
# Programming: Object-Oriented Approach 👨‍💻️ 
### Functions (Cont.)
* Press `Space` to navigate through the slides
* Use `Shift+Space` to go back
* Save as **PDF**:
  * Open **Chrome** then **<a href="?print-pdf#/">click here</a>**
  * Press **Ctrl+P**/**Cmd+P** to print
    * Destination: **Save as PDF**
    * Layout: **Landscape**
  * Press **Save** button
---
# Lambda Expressions, Map, and Filter

* Now its time to quickly learn about two built in functions, filter and map.
* Once we learn about how these operate, we can learn about the lambda expression, which will come in handy when you begin to develop your skills further!

---
## map function

* The **map** function allows you to "map" a function to an iterable object.
* That is to say you can quickly call the same function to every item in an iterable, such as a list. For example:

```python
def square(num):
    return num**2

my_nums = [1,2,3,4,5]

# To get the results, either iterate through map() 
# or just cast to a list
for item in map(square,my_nums):
	print(item)
	
list(map(square,my_nums))
```
---
## map function
* The functions can also be more complex

```python
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]

mynames = ['John','Cindy','Sarah','Kelly','Mike']

list(map(splicer,mynames))
```
---
## filter function

* The filter function returns an iterator yielding those items of iterable for which function(item)
is true.
* Meaning you need to filter by a function that returns either **True** or **False**.
* Then passing that into filter (along with your iterable) and you will get back only the results that would return True when passed to the function.

```python
def check_even(num):
    return num % 2 == 0 

nums = [0,1,2,3,4,5,6,7,8,9,10]

list(filter(check_even,nums))

for n in filter(check_even,nums):
	print(n)
```
---
## lambda expression

* One of Pythons most useful (and for beginners, confusing) tools is the **lambda** expression.
* **lambda** expressions allow us to create "anonymous" functions.
* This basically means we can quickly make ad-hoc functions without needing to properly define a function using def.
* Function objects returned by running **lambda** expressions work exactly the same as those created and assigned by defs.
* There is key difference that makes lambda useful in specialized roles:
	* **lambda's body is a single expression, not a block of statements.**

---
## lambda expression

* The lambda's body is similar to what we would put in a def body's return statement.
* We simply type the result as an expression instead of explicitly returning it.
* Because it is limited to an expression, a lambda is less general that a def.
* We can only squeeze design, to limit program nesting. lambda is designed for coding simple functions, and def handles the larger tasks.

* Lets slowly break down a lambda expression by deconstructing a function:

```python
def square(num):
    result = num**2
    return result

square(2)
```

---
## lambda expression

* We could simplify it:

```python
def square(num):
    return num**2

square(2)
```

* We could actually even write this all on one line.

```python
def square(num): return num**2

square(2)
```
* This is the form a function that a lambda expression intends to replicate.
* A lambda expression can then be written as:

```python
lambda num: num ** 2

# You wouldn't usually assign a name to a lambda expression, this is just for demonstration!
square = lambda num: num **2

square(2)
```
---
## lambda expression
* So why would use this?
* Many function calls need a function passed in, such as map and filter.
* Often you only need to use the function you are passing in once, so instead of formally defining it, you just use the lambda expression.
* Let's repeat some of the examples from above with a lambda expression

```python
list(map(lambda num: num ** 2, my_nums))
```

```python
list(filter(lambda n: n % 2 == 0,nums))
```
---
## lambda expression
* Here are a few more examples, keep in mind the more comples a function is, the harder it is to translate into a lambda expression, meaning sometimes its just easier (and often the only way) to create the def keyword function.

**Lambda expression for grabbing the first character of a string:**

```python
lambda s: s[0]
```

**Lambda expression for reversing a string:**

```python
lambda s: s[::-1]
```

---
## lambda expression
* You can even pass in multiple arguments into a lambda expression.
* Again, keep in mind that not every function can be translated into a lambda expression.

```python
lambda x,y : x + y
```

* You will find yourself using lambda expressions often with certain non-built-in libraries, for example the pandas library for data analysis works very well with lambda expressions.

---

# Nested Statements and Scope 

* Now that we have gone over writing our own functions, it's important to understand how Python deals with the variable names you assign.
* When you create a variable name in Python the name is stored in a *name-space*.
* Variable names also have a *scope*, the scope determines the visibility of that variable name to other parts of your code.

* Let's start with a quick thought experiment; imagine the following code:

```python
x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())
```

* What do you imagine the output of printer() is? 25 or 50? What is the output of print x? 25 or 50?

---

# Nested Statements and Scope 

* How does Python know which **x** you're referring to in your code?
* This is where the idea of scope comes in.
* Python has a set of rules it follows to decide what variables (such as **x** in this case) you are referencing in your code.

---
# Nested Statements and Scope 
* This idea of scope in your code is very important to understand in order to properly assign and call variable names. 
* In simple terms, the idea of scope can be described by 3 general rules:
	1. Name assignments will create or change local names by default.
	2. Name references search (at most) four scopes, these are:
	    * local
	    * enclosing functions
	    * global
	    * built-in
	3. Names declared in global and non-local statements map assigned names to enclosing module and function scopes.
---
# Nested Statements and Scope 

* The statement in #2 can be defined by the LEGB rule.

* **LEGB Rule:**
	* **L:** Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
	* **E:** Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
	* **G:** Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
	* **B:** Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
---
## Quick examples of LEGB

### Local

```python
# x is local here:
f = lambda x:x**2
```
---
### Enclosing function locals
* This occurs when we have a function inside a function (nested functions)


```python
name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    def hello():
        print('Hello '+name)
    hello()

greet()
```

* Note how Sammy was used, because the hello() function was enclosed inside of the greet function!

---
### Global
* Let's test for global variables

```python
name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    def hello():
        print('Hello '+name)   
    hello()
	
greet()
print(name)
```
---
### Built-in
* These are the built-in function names in Python (don't overwrite these!)

```python
len
```
---
## Local Variables
* When you declare variables inside a function definition, they are not related in any way to other variables with the same names used outside the function – i.e. variable names are local to the function.
* This is called the scope of the variable.
* All variables have the scope of the block they are declared in starting from the point of definition of the name.

Example:

```python
x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)
```
---
## Local Variables
* The first time that we print the value of the name **x** with the first line in the function’s body, Python uses the value of the parameter declared in the main block, above the function definition.

* Next, we assign the value 2 to **x**. The name **x** is local to our function. So, when we change the value of **x** in the function, the **x** defined in the main block remains unaffected.

* With the last print statement, we display the value of **x** as defined in the main block, thereby confirming that it is actually unaffected by the local assignment within the previously called function.
---
## The `global` statement
* If you want to assign a value to a name defined at the top level of the program (i.e. not inside any kind of scope such as functions or classes), then you have to tell Python that the name is not local, but it is global.
* We do this using the <code>global</code> statement. It is impossible to assign a value to a variable defined outside a function without the global statement.
* You can use the values of such variables defined outside the function (assuming there is no variable with the same name within the function).
* However, this is not encouraged and should be avoided since it becomes unclear to the reader of the program as to where that variable’s definition is.
* Using the <code>global</code> statement makes it amply clear that the variable is defined in an outermost block.
---
## The `global` statement
* Example:

```python
x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
```

* The <code>global</code> statement is used to declare that **x** is a global variable - hence, when we assign a value to **x** inside the function, that change is reflected when we use the value of **x** in the main block.

* You can specify more than one global variable using the same global statement e.g. <code>global x, y, z</code>.

---
## Conclusion
* You should now have a good understanding of Scope (you may have already intuitively felt right about Scope which is great!)
* One last mention is that you can use the **globals()** and **locals()** functions to check what are your current local and global variables.

* Another thing to keep in mind is that everything in Python is an object!
* We can assign variables to functions just like I can with numbers!
* We will go over this again in the decorator lecture

---

# `*args` & `**kwargs`

* Work with Python long enough, and eventually you will encounter `*args` and `**kwargs`.
* These strange terms show up as parameters in function definitions. What do they do?
* Let's review a simple function:

```python
def myfunc(a,b):
    return sum((a,b))*.05

myfunc(40,60)
```

* This function returns 5% of the sum of **a** and **b**. In this example, **a** and **b** are *positional* arguments; that is, 40 is assigned to **a** because it is the first argument, and 60 to **b**. Notice also that to work with multiple positional arguments in the `sum()` function we had to pass them in as a tuple.

---

# `*args` & `**kwargs`

* What if we want to work with more than two numbers? One way would be to assign a *lot* of parameters, and give each one a default value.

```python
def myfunc(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*.05

myfunc(40,60,20)
```

* Obviously this is not a very efficient solution, and that's where `*args` comes in.
---
## `*args`

* When a function parameter starts with an asterisk, it allows for an *arbitrary number* of arguments, and the function takes them in as a tuple of values. Rewriting the above function:

```python
def myfunc(*args):
    return sum(args)*.05

myfunc(40,60,20)
```

* Notice how passing the keyword "args" into the `sum()` function did the same thing as a tuple of arguments.

* It is worth noting that the word "args" is itself arbitrary - any word will do so long as it's preceded by an asterisk. To demonstrate this:

```python
def myfunc(*spam):
    return sum(spam)*.05

myfunc(40,60,20)
```
---
## `**kwargs`

* Similarly, Python offers a way to handle arbitrary numbers of *keyworded* arguments.
* Instead of creating a tuple of values, `**kwargs` builds a dictionary of key/value pairs.
* For example:

```python
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")
        
myfunc(fruit='pineapple')

myfunc()
```
---
## `*args` & `**kwargs` combined

* You can pass `*args` and `**kwargs` into the same function, but `*args` have to appear before `**kwargs`

```python
def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass
        
myfunc('eggs','spam',fruit='cherries',juice='orange')
```

* Placing keyworded arguments ahead of positional arguments raises an exception:

```python
myfunc(fruit='cherries',juice='orange','eggs','spam')
```

* As with "args", you can use any name you'd like for keyworded arguments – "kwargs" is just a popular convention.

* That's it! Now you should understand how `*args` and `**kwargs` provide the flexibilty to work with arbitrary numbers of arguments!

---

### Practical Work 

Complete the following questions:
____
**Write a function that computes the volume of a sphere given its radius.**<br/><br/>
The volume of a sphere is given as V = 4/3 πr³

```python
def vol(rad):
    pass
# Check
vol(2)
```

---

### Practical Work 
**Write a function that checks whether a number is in a given range (inclusive of high and low)**

```python
def ran_check(num,low,high):
    pass
	
# Check
ran_check(5,2,7)
```

If you only wanted to return a boolean:

```python
def ran_bool(num,low,high):
    pass

ran_bool(3,1,10)
```

---

### Practical Work
**Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**

    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    Expected Output : 
    No. of Upper case characters : 4
    No. of Lower case Characters : 33

**HINT:** Two string methods that might prove useful – **.isupper()** and **.islower()**

```python
def up_low(s):
    pass

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
```

---

### Practical Work
**Write a Python function that takes a list and returns a new list with unique elements of the first list.**

    Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
    Unique List : [1, 2, 3, 4, 5]

```python
def unique_list(lst):
    pass

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
```

---

### Practical Work
**Write a Python function to multiply all the numbers in a list.**

    Sample List : [1, 2, 3, -4]
    Expected Output : -24

```python
def multiply(numbers):  
    pass

multiply([1,2,3,-4])
```

---
### Practical Work
**Write a Python function that checks whether a word or phrase is palindrome or not.**

**Note:** A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam, kayak, racecar or a phrase "nurses run".

**Hint:** You may want to check out the `.replace()` method in a string to help out with dealing with spaces.

Also Google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.

```python
def palindrome(s):
    pass
	
palindrome('helleh')
```

---
#### Hard:

**Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)**

    Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example : "The quick brown fox jumps over the lazy dog"

**Hint:** You may want to use .replace() method to get rid of spaces.

**Hint:** Look at the [string module](https://stackoverflow.com/questions/16060899/alphabet-range-in-python)

**Hint:** In case you want to use [set comparisons](https://medium.com/better-programming/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41)

```python
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    pass

ispangram("The quick brown fox jumps over the lazy dog") # True

string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
```
---

# Programming: Object-Oriented Approach 👨‍💻️ 
### Built-in Functions
* Press `Space` to navigate through the slides
* Use `Shift+Space` to go back
* Save as **PDF**:
  * Open **Chrome** then **<a href="?print-pdf#/">click here</a>**
  * Press **Ctrl+P**/**Cmd+P** to print
    * Destination: **Save as PDF**
    * Layout: **Landscape**
  * Press **Save** button
---
# reduce()

* Many times students have difficulty understanding reduce() so pay careful attention to this lecture.
* The function reduce(function, sequence) continually applies the function to the sequence.
* It then returns a single value. 
---
# reduce()
* If `seq = [ s1, s2, s3, ... , sn ]`, calling `reduce(function, sequence)` works like this:
	* At first the first two elements of seq will be applied to function, i.e. `func(s1,s2)`
	* The list on which `reduce()` works looks now like this: `[ function(s1, s2), s3, ... , sn ]`
	* In the next step the function will be applied on the previous result and the third element of the list, i.e. `function(function(s1, s2),s3)`
	* The list looks like this now: `[ function(function(s1, s2),s3), ... , sn ]`
	* It continues like this until just one element is left and return this element as the result of `reduce()`
---
# reduce()
* Let's see an example:

```python
from functools import reduce

lst =[47,11,42,13]
reduce(lambda x,y: x+y,lst)
```

---
# reduce()
* Lets look at a diagram to get a better understanding of what is going on here:

<img src="http://www.python-course.eu/images/reduce_diagram.png">

* Note how we keep reducing the sequence until a single final value is obtained. Let's see another example:

```python
#Find the maximum of a sequence (This already exists as max())
max_find = lambda a,b: a if (a > b) else b

#Find max
reduce(max_find,lst)
```

* Hopefully you can see how useful reduce can be in various situations.

---
# zip
<div style="float:left;width:50%;">
	
* `zip()` makes an iterator that aggregates elements from each of the iterables.

* Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
* The iterator stops when the shortest input iterable is exhausted.
* With a single iterable argument, it returns an iterator of 1-tuples.
* With no arguments, it returns an empty iterator. 

</div>
<div style="float: right;width:50%;">
	
* With a single iterable argument, it returns an iterator of 1-tuples.
* With no arguments, it returns an empty iterator. 
* `zip()` is equivalent to:

```python
def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
```
</div>

---
# zip
* `zip()` should only be used with unequal length inputs when you don’t care about trailing, unmatched values from the longer iterables. 

* Let's see it in action in some examples:

### Examples

```python
x = [1,2,3]
y = [4,5,6]

# Zip the lists together
list(zip(x,y))
```
* Note how tuples are returned.
---
### Examples
* What if one iterable is longer than the other?

```python
x = [1,2,3]
y = [4,5,6,7,8]

# Zip the lists together
list(zip(x,y))
```

* Note how the zip is defined by the shortest iterable length.
* It is generally advised not to zip unequal length iterables unless your very sure you only need partial tuple pairings.
---
### Examples
* What happens if we try to zip together dictionaries?

```python
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

list(zip(d1,d2))
```

* This makes sense because simply iterating through the dictionaries will result in just the keys.
* We would have to call methods to mix keys and values:

```python
list(zip(d2,d1.values()))
```
---
### Examples
* Finally lets use zip() to switch the keys and values of the two dictionaries:

```python
def switcharoo(d1,d2):
    dout = {}
    for d1key,d2val in zip(d1,d2.values()):
        dout[d1key] = d2val   
    return dout

switcharoo(d1,d2)
```

* You can use zip to save a lot of typing in many situations!

---

# enumerate()

* In this lecture we will learn about an extremely useful built-in function: `enumerate()`.
* Enumerate allows you to keep a count as you iterate through an object.
* It does this by returning a tuple in the form (count,element).
* The function itself is equivalent to:

```python
    def enumerate(sequence, start=0):
        n = start
        for elem in sequence:
            yield n, elem
            n += 1
```
---
## Example

```python
lst = ['a','b','c']

for number,item in enumerate(lst):
    print(number)
    print(item)
```

* `enumerate()` becomes particularly useful when you have a case where you need to have some sort of tracker. For example:

```python
for count,item in enumerate(lst):
    if count >= 2:
        break
    else:
        print(item)
```

* `enumerate()` takes an optional "start" argument to override the default value of zero:

```python
months = ['March','April','May','June']

list(enumerate(months,start=3))
```

* You should now have a good understanding of enumerate and its potential use cases.
---

# all() and any()
* `all()` and `any()` are built-in functions in Python that allow us to conveniently check for boolean matching in an iterable.
* `all()` will return True if all elements in an iterable are True.
* It is the same as this function code:

```python
    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True
```     
   
* `any()` will return True if any of the elements in the iterable are True.
* It is equivalent to the following function code:
```python
    def any(iterable):
        for element in iterable:
            if element:
                return True
        return False
``` 
---

# all() and any()
* Let's see a few examples of these functions. They should be fairly straightforward:

```python
lst = [True,True,False,True]
all(lst)
```

* Returns `False` because not all elements are True.

```python
any(lst)
```

* Returns `True` because at least one of the elements in the list is `True`

---
# complex()

* `complex()` returns a complex number with the value `real + imag*1j` or converts a string or number to a complex number. 
<br/><br/>
* If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter.
* The second parameter can never be a string.
* Each argument may be any numeric type (including complex).
* If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like `int` and `float`.
* If both arguments are omitted, returns 0j.
<br/><br/>
* If you are doing math or engineering that requires complex numbers (such as dynamics, control systems, or impedance of a circuit) this is a useful tool to have in Python.

---
# complex()
* Let's see some examples:

```python
# Create 2+3j
complex(2,3)

complex(10,1)
```

* We can also pass strings:

```python
complex('12+2j')
```

* That's really all there is to this useful function.
* Keep it in mind if you are ever dealing with complex numbers in Python!
---

# Built-in Functions Practical 

For this practical, you should use built-in functions and be able to write the requested functions in one line.

### Problem 1

* Use `map()` to create a function which finds the length of each word in the phrase (broken by spaces) and returns the values in a list.

* The function will have an input of a string, and output a list of integers.

```python
def word_lengths(phrase):    
    pass

word_lengths('How long are the words in this phrase')
```
---
### Problem 2 

* Use reduce() to take a list of digits and return the number that they correspond to.
* For example, \[1, 2, 3] corresponds to one-hundred-twenty-three.
* *Do not convert the integers to strings!* 

```python
from functools import reduce

def digits_to_num(digits):    
    pass

digits_to_num([3,4,3,2,1])
```
---
### Problem 3

Use filter to return the words from a list of words which start with a target letter.

```python
def filter_words(word_list, letter):
    pass

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')
```
---
### Problem 4

* Use `zip()` and a list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated together with connector between them.
* Look at the example output below:

```python
def concatenate(L1, L2, connector):    
    pass

concatenate(['A','B'],['a','b'],'-')
```
---
### Problem 5

* Use `enumerate()` and other skills to return a dictionary which has the values of the list as keys and the index as the value.
* You may assume that a value will only appear once in the given list.

```python
def d_list(L):    
    pass

d_list(['a','b','c'])
```
---
### Problem 6

* Use `enumerate()` and other skills from above to return the count of the number of items in the list whose value equals its index.

```python
def count_match_index(L):
    pass

count_match_index([0,2,2,1,5,5,6,10])
```

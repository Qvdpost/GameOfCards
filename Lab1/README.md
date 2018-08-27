# An intro to Object-Oriented Programming in Python
## Getting Started
Object-oriented programming is commonly used to model real-world things, like cars, and their interactions and behaviors. The objects bundle all relevant information and guarantee that their procedure (methods in case of Python) function as expected.
But before getting into the nitty gritty of OOP, let's first walk through some of the concepts you've just learned.  

<img align="left" src="../images/card_deck.png" style="padding: 10px">
We'll practice these concepts by creating a deck of 52 playing cards. Each card will be represented by an object and the deck itself will be an object too!
Interacting with the deck will be done via its procedures, or methods if you will.

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

For a quick reminder of the Python basics watch the following Doug-talk.

{% video https://www.youtube.com/watch?v=8xCzjOnfQbw&feature=youtu.be&t=1650 %}

{% next "Start: Classes and instances" %}

## Classes

Classes are blueprints for the components of your projects. They contain information on instantiating individual instances for that component, as well as procedures that allow interaction between the program and objects or between objects themselves.
To decide on what parts of a program should be contained components, consider which sets of data represent a clearly defined concept.

In this tutorial we'll walk you through creating a deck of cards. Take a look at the file `cardgame.py`. You'll find two classes already defined with their attributes in place.

A Card is represented by its suit and value, as can be seen from the `__init__`, these values can be anything however. So a deck of apples and strawberries could also be made using this same Card class.
Our Deck however uses the traditional suits (Hearts, Diamonds, Clubs and Spades) and values (Ace through King).

All these attributes are defined withing the `__init__` method, often times this is the very first method you'll define for your class.

To start out, let's create a deck. Add `deck = Deck()` to the if statement at the bottom of the file and run the script via `python cardgame.py` in the terminal.
If everything went well, nothing should've happened.. As a matter of fact, the deck has no cards at all yet!

{% next "Continue: Methods" %}

## Methods

Now let's get started with the methods. Firstly there's the `__init__`, it is called the initialisator. When you create an object the `__init__` is used to set it up with the correct values. As you can see, we've already supplied it with suits and values, but not the actual card objects yet.
To initialise the cards we're going to use a method. Let's call it `initialise_cards()`. Adding a method is like declaring a function, only at an indented level under the class it belongs to. The function can usually only be called by the class it is attached to.
Before getting into the actual code, it is advised to write a docstring for your method. 

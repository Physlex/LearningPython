import random, sys, os, django, math #Interesting that you can do that, alwaays like one - line code

playerName = 'None'

def Greetings() :
    print('Welcome, user. Please, tell me your name?')
    return

def Hello() :
    print('Howdy! ', end= '')
    print(playerName, 'Jhon') #Commas add a space in-between output values when concatenating
    return

def Name(name) :
    global playerName
    playerName = name
    Hello()
    return

def DivideByZero(zero = 0) :
    try :
        return 1 // zero
    except ZeroDivisionError :
        print('Error: Invalid argument')

def LetsTry() :
    print('Let us try something here...', end='')
    DivideByZero()
    return

Greetings()
Name(input())
DivideByZero()

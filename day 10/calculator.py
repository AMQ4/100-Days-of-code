import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from commands import clear
from art import logo

def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def devide(a,b):
  return a/b
def power(a,b):
  return a**b
def mod(a,b):
  return a%b

def calculator():
    operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':devide,
    '^':power,
    '%':mod
    }
  
    num1 = float(input("Waht's the first number? "))
    print('\n'.join(operations.keys()))
    operation = input("Pick an operation: ")
    num2 = float(input("Waht's the second number? "))
    ans = operations[operation](num1,num2)
    print(f"{num1} {operation} {num2} = {ans}" )
    
    response = input(f"Type 'y' to continue calculating with {ans}, type 'n' to start an new calculation, or press any key to exit.")
    
    while response == 'y':
        num1 = ans
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        ans = operations[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {ans}")
        response = input(f"Type 'y' to continue calculating with {ans}, type 'n' to start an new calculation, or press any key to exit.")
    
    if response == 'n':
       clear()
       calculator()
    exit(0)
print(logo)
calculator()
from termcolor import colored
from os import system

titleText = colored("""
사칙연산 스도쿠 해결 프로그램
by Woohyun Jung


""", "green")

def edit(string): 
    system("cls")
    print(titleText + string)

edit("hello world!")
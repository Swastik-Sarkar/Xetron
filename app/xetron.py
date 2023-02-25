from pyfiglet import *
from os import *
from platform import *
from sys import *


label = figlet_format('Xetron')
print(stdout("\u001b[34;1m" + label + "\u001b[0m"))
def helpdial():
  print(""" Test 
           ------
              X
        """)
main()
def main():
  cmd = input(stdout("\u001b[35;1m user" + "\u001b[33;1m @" + "\u001b[32;1m xetron" + "\u001b[31;1m ~~> " + "))
  while True:
    if cmd == 'help':
      return helpdial

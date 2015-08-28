# -*- coding: utf-8 -*-
"""
chargen.py
Problem: Generate a description for a fantasy role-playing character.
Created on Fri Aug 28 10:20:10 2015

@author: amaloney
"""
version = 0.1
Name = ""
Desc = ""
Gender = ""
Race = ""

# Prompt user for user-defined information
Name = input('What is your Name? ')
Desc = input('Describe yourself: ')
Gender = input('What Gender are you? (male / female / unsure): ')
Race = input('What fantasy Race are you? - (Pixie / Vulcan / Gelfling / Troll): ')
# Output the character sheet
fancy_line = "<~~==|#|==~~++**\@/**++~~==|#|==~~>"
print("\n", fancy_line)
print("\t", Name)
print("\t", Race, Gender)
print("\t", Desc)
print(fancy_line, "\n")


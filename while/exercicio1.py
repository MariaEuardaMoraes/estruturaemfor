# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N7wdn8xQNmo-kPIx3TuffXgfc-vdYMA6
"""

#exercico 1
nota = float(input("digite uma nota entre zero e dez: "))
while nota > 10 or nota < 0:
  nota = float(input(f"digite um valor valido: "))
print("sucesso")
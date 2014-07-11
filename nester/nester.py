#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Módulo para visuzalizar listas aninhadas. 
   Módulo nester.py"""

def print_lol(the_list, level):
  """Função para percorrer a lista e mostrar na tela.
     Tem a função print_lol usando isinstance para 
     verificar ser é uma lista
     Um segundo argumento chamado "level" é usado para inserer tabulação
     quando uma lista aninhada é encontrada"""

  for each_item in the_list:
    if isinstance(each_item, list):
      print_lol(each_item)
    else:
      for tab_stop in range(level):
        print('\t') 
      print(each_item)

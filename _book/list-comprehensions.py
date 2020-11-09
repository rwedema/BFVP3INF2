"""
Geef steeds een list comprehension voor het volgende resultaat
"""
import math
import random

#opgave 1
#start
None
#omschrijving:
#gebruik range() voor het genereren van een getallenvolgorde
#resultaat
[0, 2, 3, 4, 5, 6, 7, 8, 9]
#antwoord
l01 = ["list comprehension here"]
print(1, l01)

#opgave 2
#start
l02 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#resultaat
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
#omschrijving:
#gebruik float() voor het omzetten naar floats
#antwoord
l03 = ["list comprehension here"]
print(2, l03)

#opgave 3
#start
l04 = ['h', 'a', 'l', 'l', 'o']
#resultaat
['H', 'A', 'L', 'L', 'O']
#omschrijving:
#gebruik str.upper() voor het omzetten naar hoofdletters
#antwoord
l05 = ["list comprehension here"]
print(3, l05)

#opgave 4
#start
None
#resultaat
[0, 2, 4, 6, 8]
#omschrijving:
#gebruik range() voor het maken van een lijst van even getallen van 0 tot 10. Selecteer vervolgens de even getallen met een if statement.
#antwoord
l06 = ["list comprehension here"]
print(4, l06)

#opgave 5
#start
l07 = [0, 1, 2, 3]
str1 = "abc"
#resultaat
['a0', 'a1', 'a2', 'a3', 'b0', 'b1', 'b2', 'b3', 'c0', 'c1', 'c2', 'c3']
#omschrijving:
#gebruik nu een nested expression
#antwoord
l08 = ["list comprehension here"]
print(5, l08)

#opgave 6
#start
l09 = [0, 1, 2, 3]
str2 = "abc"
#resultaat
['a0', 'a1', 'a3', 'c0', 'c1', 'c3']
#omschrijving:
#gebruik nu een nested expression. Gebruik if om elementen met een 2 over te slaan.
#antwoord
l10 = ["list comprehension here"]
print(6, l10)

#opgave 7
#start
l11 = [1, 2, 3, 4, 5]
#resultaat
[1, 4, 9, 16, 25]
#omschrijving:
#geef de kwadraten mbv een list comprehension
#antwoord
l12 = ["list comprehension here"]
print(7, l12)

#opgave 8
#start
l13 = [4, 9, 16, 25, 36]
#resultaat
[2.0, 3.0, 4.0, 5.0, 6.0]
#omschrijving:
#geef de wortel van elk item uit de lijst in een nieuwe lijst
#antwoord
l13 = ["list comprehension here"]
print(8, l13)

#opgave 9
#start
str3 = "atcg"
l14 = ['1', '2']
#resultaat
[('a', '1'), ('a', '2'), ('t', '1'), ('t', '2'), ('c', '1'), ('c', '2'), ('g', '1'), ('g', '2')]
#omschrijving:
#maak een lijst van tuples voor elke combinatie
#antwoord
l15 = ["list comprehension here"]
print(9, l15)

#opgave 10
#start
str3 = "tcag"
#resultaat
[('t', 't', 't'), ('t', 't', 'c'), ('t', 't', 'a'), ('t', 't', 'g'), ('t', 'c', 't'), ('t', 'c', 'c'), ('t', 'c', 'a'), ('t', 'c', 'g'), ('t', 'a', 't'), ('t', 'a', 'c'), ('t', 'a', 'a'), ('t', 'a', 'g'), ('t', 'g', 't'), ('t', 'g', 'c'), ('t', 'g', 'a'), ('t', 'g', 'g'), ('c', 't', 't'), ('c', 't', 'c'), ('c', 't', 'a'), ('c', 't', 'g'), ('c', 'c', 't'), ('c', 'c', 'c'), ('c', 'c', 'a'), ('c', 'c', 'g'), ('c', 'a', 't'), ('c', 'a', 'c'), ('c', 'a', 'a'), ('c', 'a', 'g'), ('c', 'g', 't'), ('c', 'g', 'c'), ('c', 'g', 'a'), ('c', 'g', 'g'), ('a', 't', 't'), ('a', 't', 'c'), ('a', 't', 'a'), ('a', 't', 'g'), ('a', 'c', 't'), ('a', 'c', 'c'), ('a', 'c', 'a'), ('a', 'c', 'g'), ('a', 'a', 't'), ('a', 'a', 'c'), ('a', 'a', 'a'), ('a', 'a', 'g'), ('a', 'g', 't'), ('a', 'g', 'c'), ('a', 'g', 'a'), ('a', 'g', 'g'), ('g', 't', 't'), ('g', 't', 'c'), ('g', 't', 'a'), ('g', 't', 'g'), ('g', 'c', 't'), ('g', 'c', 'c'), ('g', 'c', 'a'), ('g', 'c', 'g'), ('g', 'a', 't'), ('g', 'a', 'c'), ('g', 'a', 'a'), ('g', 'a', 'g'), ('g', 'g', 't'), ('g', 'g', 'c'), ('g', 'g', 'a'), ('g', 'g', 'g')]
#omschrijving:
#maak een lijst van tuples met alle codons
#antwoord
l16 = ["list comprehension here"]
print(10, l16)

#opgave 11
#start
str3 = "tcag"
#resultaat
['ttt', 'ttc', 'tta', 'ttg', 'tct', 'tcc', 'tca', 'tcg', 'tat', 'tac', 'taa', 'tag', 'tgt', 'tgc', 'tga', 'tgg', 'ctt', 'ctc', 'cta', 'ctg', 'cct', 'ccc', 'cca', 'ccg', 'cat', 'cac', 'caa', 'cag', 'cgt', 'cgc', 'cga', 'cgg', 'att', 'atc', 'ata', 'atg', 'act', 'acc', 'aca', 'acg', 'aat', 'aac', 'aaa', 'aag', 'agt', 'agc', 'aga', 'agg', 'gtt', 'gtc', 'gta', 'gtg', 'gct', 'gcc', 'gca', 'gcg', 'gat', 'gac', 'gaa', 'gag', 'ggt', 'ggc', 'gga', 'ggg']
#omschrijving:
#maak een lijst van strings met alle codons.
#antwoord
l17 = ["list comprehension here"]
print(11, l17)

#opgave 12
#start
None
#resultaat
[[0, 1], [1, 2]]
#omschrijving:
#maak een twee-dimensionele matrix met behulp van range
#antwoord
l18 = ["list comprehension here"]
print(12, l18)

#opgave 13
#start
None
#resultaat
[[1, 2], [3, 4], [5, 6]]
#omschrijving:
#maak een twee-dimensionele matrix met behulp van range. Zorg er voor dat de getallen oplopend zijn.
#antwoord
l18 = ["list comprehension here"]
print(13, l18)

#opgave 14
#start
l19 = [[1, 2], [3, 4], [5, 6]]
#resultaat
[2, 4, 6]
#omschrijving:
#Maak een lijst van de tweede kolom van de matrix
#antwoord
l20 = ["list comprehension here"]
print(14, l20)

#opgave 15
#start
l19 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#resultaat
[1, 5, 9]
#omschrijving:
#Maak een lijst van de diagonaal van de matrix
#antwoord
l21 = ["list comprehension here"]
print(15, l21)

#opgave 16
#start
None
#resultaat
#variabel, bijv: [4, 2, 1, 1, 4, 3, 4, 3, 1, 4]
#omschrijving:
#Maak een lijst van 10 worpen met een dobbelsteen
#antwoord
l22 = ["list comprehension here"]
print(16, l22)

#opgave 17
#start
str4 = "cube"
#resultaat
[[['cube', 'cube', 'cube'], ['cube', 'cube', 'cube'], ['cube', 'cube', 'cube']], [['cube', 'cube', 'cube'], ['cube', 'cube', 'cube'], ['cube', 'cube', 'cube']], [['cube', 'cube', 'cube'], ['cube', 'cube', 'cube'], ['cube', 'cube', 'cube']]]
#omschrijving:
#Maak een 3-dimensionale matrix. Elk element bevat de string: "cube". Dimensies zijn: 3x3x3
#antwoord
l23 = ["list comprehension here"]
print(17, l23)


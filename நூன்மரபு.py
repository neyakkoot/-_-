# -*- coding: utf-8 -*-
"""நூன்மரபு.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZaNK9ZNo9YMsMmfeFSU1wTD9jYauVeR0
"""

!pip install Open-Tamil

import tamil
print("தொல்காப்பிய ஆசானுக்கு வணக்கம்")

import tamil

தொல்காப்பியம்_எழுத்ததிகாரம்_இயல்கள் = ['நூன்மரபு', 'மொழிமரபு', 'பிறப்பியல்', 'புணரியல்', 'தொகைமரபு', 'உருபியல்', 'உயிர் மயங்கியல்', 'புள்ளி மயங்கியல்', 'குற்றியலுகரப் புணரியல்']
print(தொல்காப்பியம்_எழுத்ததிகாரம்_இயல்கள்)

import tamil
நூன்மரபு = ['எழுத்துக்களின் வகை', 'மாத்திரை', 'எண்', 'வடிவு', 'மயக்கம்', 'பிற மரபுகள்']
print(நூன்மரபு)

எழுத்துக்களின்_வகை = ['முதலெழுத்து', 'சார்பெழுத்து']
print(எழுத்துக்களின்_வகை)

முதலெழுத்து = ['உயிரெழுத்து', 'மெய்யெழுத்து']
print(முதலெழுத்து)

உயிரெழுத்து = tamil.utf8.uyir_letters
print(உயிரெழுத்து)

மெய்யெழுத்து = ['க்', 'ங்', 'ச்', 'ஞ்', 'ட்', 'ண்', 'த்', 'ந்', 'ப்', 'ம்', 'ய்', 'ர்', 'ல்', 'வ்', 'ழ்', 'ள்', 'ற்', 'ன்']
#மெய்யெழுத்து = tamil.utf8.Mei_letters
print(மெய்யெழுத்து)

#மெய்யெழுத்து = ['க்', 'ங்', 'ச்', 'ஞ்', 'ட்', 'ண்', 'த்', 'ந்', 'ப்', 'ம்', 'ய்', 'ர்', 'ல்', 'வ்', 'ழ்', 'ள்', 'ற்', 'ன்']
மெய்யெழுத்து = tamil.utf8.mei_letters
print(மெய்யெழுத்து)

உயிரெழுத்து_வகை = ['குறில்', 'நெடில்']
print(உயிரெழுத்து_வகை)

உயிரெழுத்து_வகை_குறில் = tamil.utf8.kuril_letters
print(உயிரெழுத்து_வகை_குறில்)

உயிரெழுத்து_வகை_நெடில் = tamil.utf8.nedil_letters
print(உயிரெழுத்து_வகை_நெடில்)

சார்பெழுத்து = ['குற்றியலிகரம்', 'குற்றியலுகரம்', 'ஆய்தம்']
print(சார்பெழுத்து)

உயிர்_மெய் = [
    'க', 'கா', 'கி', 'கீ', 'கு', 'கூ', 'கெ', 'கே', 'கை', 'கொ', 'கோ', 'கௌ',
    'ங', 'ஙா', 'ஙி', 'ஙீ', 'ஙு', 'ஙூ', 'ஙெ', 'ஙே', 'ஙை', 'ஙொ', 'ஙோ', 'ஙௌ',
    'ச', 'சா', 'சி', 'சீ', 'சு', 'சூ', 'செ', 'சே', 'சை', 'சொ', 'சோ', 'சௌ',
    'ஞ', 'ஞா', 'ஞி', 'ஞீ', 'ஞு', 'ஞூ', 'ஞெ', 'ஞே', 'ஞை', 'ஞொ', 'ஞோ', 'ஞௌ',
    'ட', 'டா', 'டி', 'டீ', 'டு', 'டூ', 'டெ', 'டே', 'டை', 'டொ', 'டோ', 'டௌ',
    'ண', 'ணா', 'ணி', 'ணீ', 'ணு', 'ணூ', 'ணெ', 'ணே', 'ணை', 'ணொ', 'ணோ', 'ணௌ',
    'த', 'தா', 'தி', 'தீ', 'து', 'தூ', 'தெ', 'தே', 'தை', 'தொ', 'தோ', 'தௌ',
    'ந', 'நா', 'நி', 'நீ', 'நு', 'நூ', 'நெ', 'நே', 'நை', 'நொ', 'நோ', 'நௌ',
    'ப', 'பா', 'பி', 'பீ', 'பு', 'பூ', 'பெ', 'பே', 'பை', 'பொ', 'போ', 'பௌ',
    'ம', 'மா', 'மி', 'மீ', 'மு', 'மூ', 'மெ', 'மே', 'மை', 'மொ', 'மோ', 'மௌ',
    'ய', 'யா', 'யி', 'யீ', 'யு', 'யூ', 'யெ', 'யே', 'யை', 'யொ', 'யோ', 'யௌ',
    'ர', 'ரா', 'ரி', 'ரீ', 'ரு', 'ரூ', 'ரெ', 'ரே', 'ரை', 'ரொ', 'ரோ', 'ரௌ',
    'ல', 'லா', 'லி', 'லீ', 'லு', 'லூ', 'லெ', 'லே', 'லை', 'லொ', 'லோ', 'லௌ',
    'வ', 'வா', 'வி', 'வீ', 'வு', 'வூ', 'வெ', 'வே', 'வை', 'வொ', 'வோ', 'வௌ',
    'ழ', 'ழா', 'ழி', 'ழீ', 'ழு', 'ழூ', 'ழெ', 'ழே', 'ழை', 'ழொ', 'ழோ', 'ழௌ',
    'ள', 'ளா', 'ளி', 'ளீ', 'ளு', 'ளூ', 'ளெ', 'ளே', 'ளை', 'ளொ', 'ளோ', 'ளௌ'
    'ற', 'றா', 'றி', 'றீ', 'று', 'றூ', 'றெ', 'றே', 'றை', 'றொ', 'றோ', 'றௌ',

    'ன', 'னா', 'னி', 'னீ', 'னு', 'னூ', 'னெ', 'னே', 'னை', 'னொ', 'னோ', 'னௌ'
]
print(உயிர்_மெய்)

---
title: "Datasette: Madly accessible data"
author: "@catherine.devlin@tech.lgbt"
format: revealjs
---

## SQLite 

Database 

Data file format + C library 

### Access with

CLIs like sqlite3 or

    > uvx litecli shakespeare.db 

    shakespeare.db> SELECT plain_text FROM paragraph LIMIT 5;

Browser extensions

## Python access 

    import sqlite3

    with sqlite3.connect('shakespeare.db') as con:
        curs = con.cursor()
        curs.execute('SELECT title, year FROM work') 
        print(curs.fetchall())

    [('Twelfth Night', 1599), ("All's Well That Ends Well", 1602), ('Antony and Cleopatra', 1606), ('As You Like It', 1599), ('Comedy of Errors', 1589), ('Coriolanus', 1607), ('Cymbeline', 1609), ('Hamlet', 1600), ('Henry IV, Part I', 1597), ('Henry IV, Part II', 1597), ('Henry V', 1598), ('Henry VI, Part I', 1591), ('Henry VI, Part II', 1590), ('Henry VI, Part III', 1590), ('Henry VIII', 1612), ('Julius Caesar', 1599), ('King John', 1596), ('King Lear', 1605), ("Lover's Complaint", 1609), ("Love's Labour's Lost", 1594), ('Macbeth', 1605), ('Measure for Measure', 1604), ('Merchant of Venice', 1596), ('Merry Wives of Windsor', 1600), ("Midsummer Night's Dream", 1595), ('Much Ado about Nothing', 1598), ('Othello', 1604), ('Passionate Pilgrim', 1598), ('Pericles', 1608), ('Phoenix and the Turtle', 1601), ('Rape of Lucrece', 1594), ('Richard II', 1595), ('Richard III', 1592), ('Romeo and Juliet', 1594), ('Sonnets', 1609), ('Taming of the Shrew', 1593), ('Tempest', 1611), ('Timon of Athens', 1607), ('Titus Andronicus', 1593), ('Troilus and Cressida', 1601), ('Two Gentlemen of Verona', 1594), ('Venus and Adonis', 1593), ("The Winter's Tale", 1610)]


## Datasette

Made famous by [civicband](https://civic.band/)!

    > uvx datasette shakespeare.db 

Filter, query, export, publish, ...

## Datasette-lite: PyIodide power

https://lite.datasette.io/?url= 

[https://lite.datasette.io/?url=https://github.com/catherinedevlin/opensourceshakespeare/blob/master/shakespeare.db](https://lite.datasette.io/?url=https://github.com/catherinedevlin/opensourceshakespeare/blob/master/shakespeare.db)

[https://lite.datasette.io/?csv=https://github.com/nrennie/shakespeare/blob/main/data/1henryiv.csv](https://lite.datasette.io/?csv=https://github.com/nrennie/shakespeare/blob/main/data/1henryiv.csv)

## 1 URL = 1 data exploration platform

Imagine the possibilities!  

Awesome lists, Linktree sites... 

Answering Questions About Local Government

( ... business, hobbies, nonprofits, history, ... ) 


## PostgreSQL?

![Chelnik the PostgreSQL Elephant](chelnik.jpg)







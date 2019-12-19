"""
Assignment 2-B
==============

Wrap Assignment 1-B in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-ru.txt').read_text()
True
"""

def poem():
    poem_parts = [
        "В доме, который построил Джек.",
        "Которая в тёмном чулане хранится",
        "Которая часто ворует пшеницу,",
        "Который пугает и ловит синицу,",
        "Который за шиворот треплет кота,",
        "Лягнувшую старого пса без хвоста,",
        "Которая доит корову безрогую,",
        "Который бранится с коровницей строгою,",
        "Которые будят того пастуха,"
    ]
    
    poem_headers = [
        "дом, который построил Джек.",
        "пшеница,",
        "весёлая птица-синица,",
        "кот,",
        "пёс без хвоста,",
        "корова безрогая,",
        "старушка, седая и строгая,",
        "ленивый и толстый пастух,",
        "два петуха,"        
    ]
    
    poem_start = [
        "Вот ",
        "А это "
    ]
    
    final_string = ""
    
    for i in range(len(poem_parts)):
        if i in (1,2,5,6,7):
            final_string = final_string + poem_start[1]
        else:
            final_string = final_string + poem_start[0]
        final_string = final_string + poem_headers[i] + "\n"
        if i == 5:
            poem_parts[5] = "Лягнувшая старого пса без хвоста,"
        else: 
            poem_parts[5] = "Лягнувшую старого пса без хвоста," 
        for m in range(i+1):
            if i != 0:
                final_string = final_string + poem_parts[i - m]
                final_string = final_string + "\n"
        if i != 8:        
            final_string = final_string + "\n"
    
    return final_string



if __name__ == '__main__':
    import doctest
    doctest.testmod()

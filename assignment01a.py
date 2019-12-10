"""
Assignment 1-A
==============

Write fuction that generates the text below; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

>>> print(poem())
This is the house that Jack built.
---
This is the malt
That lay in the house that Jack built.
---
This is the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the cock that crowed in the morn,
That waked the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the farmer sowing his corn,
That kept the cock that crowed in the morn,
That waked the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
<BLANKLINE>
"""

def poem():
    array1 = ["This is ", "That "]
    array2 = ["lay in ", "ate ", "killed ", "worried ", "tossed ", "milked ", "kissed ",
             "married ", "waked ", "kept "]
    array3 = ["the house that Jack built.", "the malt", "the rat,", "the cat,", "the dog,",
             "the cow with the crumpled horn,", "the maiden all forlorn,", "the man all tatter'd and torn,",
             "the priest all shaven and shorn,", "the cock that crow'd in the morn,", "the farmer sowing his corn,"]
    list=""
    for i in range(len(array3)):
        list+=array1[0] + array3[i]+"\n"
        for j in range(i - 1, -1, -1):
            list+=array1[1] + array2[j] + array3[j] +"\n"
        if i < len(array3)-1 :
            list+="\n"
    return list

if __name__ == '__main__':
    import doctest
    doctest.testmod()

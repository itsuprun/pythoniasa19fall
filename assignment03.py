
def task1():
    """
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence
    on a single line.
    """
    # todo: write your code here
    return ','.join(str(i) for i in range(2002, 3200) if i % 5 != 0 and i%7 == 0)

def task2(rows, cols):
    """
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
    The element value in the i-th row and j-th column of the array should be i*j.
    Note: i=0,1.., X-1; j=0,1,¡­Y-1.

    Example:
    Suppose the following inputs are given to the program: 3, 5.
    Then, the output of the program should be:
    >>> task2(3, 5)
    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    """
    # todo: write your code here
    return [[x*y for y in range(cols)]for x in range(rows)]

def task3(password):
    """
    A website requires the users to input username and password to register.
    Write a program to check the validity of password input by users.

    Following are the criteria for checking the password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    3. At least 1 letter between [A-Z]
    4. At least 1 character from [$#@]
    5. Minimum length of transaction password: 6
    6. Maximum length of transaction password: 12

    Your program should accept a password and will check them according to the above criteria.

    Example:
    If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345
    Then, the output of the program should be:

    >>> task3('ABd1234@1')
    True
    >>> task3('a F1#')
    False
    >>> task3('2w3E*')
    False
    >>> task3('2We3345')
    False
    """
    # todo: write your code here

    return (any('a' <= i <= 'z' for i in password)
           and any('0' <= i <= '9' for i in password)
           and any('A' <= i <= 'Z' for i in password)
           and any( i  in '$#@' for i in password)
           and (6 <= len(password) <= 12)            
        )


def task4():
    """
    Write password generator function that uses the same rules as in Task 3.
    The password generator function must be able to generate all possible correct passwords.
    """
    import random
    from string import ascii_lowercase, ascii_uppercase, digits
    lenght = random.randint(6,12)
    password=['' for i in range(lenght)]
    number = digits
    lowercase = ascii_lowercase
    uppercase= ascii_uppercase
    specialSigns='$#@'

    list_pos=[i for i in range(lenght)]

    uppercase_pos= random.choice(list_pos)
    password.insert(uppercase_pos,random.choice(uppercase))
    list_pos.remove(uppercase_pos)

    lowercase_pos = random.choice(list_pos)
    password.insert(lowercase_pos, random.choice(lowercase))
    list_pos.remove(lowercase_pos)

    number_pos = random.choice(list_pos)
    password.insert(number_pos, random.choice(number))
    list_pos.remove(number_pos)

    specialSign_pos = random.choice(list_pos)
    password.insert(specialSign_pos, random.choice(specialSigns))

    for i in list_pos:
        password.insert(i, random.choice(number + lowercase + uppercase + specialSigns))
    return ''.join(password)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

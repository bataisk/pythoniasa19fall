
def task1():
    """
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence
    on a single line.
    """

    return ','.join(str(i) for i in range(2000, 3200) if i % 7 == 0 and i % 5 != 0)


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

    return [[row*col for col in range(cols)] for row in range(rows)]


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

    return (6 <= len(password) <= 12
            and any('a' <= s <= 'z' for s in password)
            and any('A' <= s <= 'Z' for s in password)
            and any('0' <= s <= '9' for s in password)
            and any(s in '#$@' for s in password))


def task4():
    """
    Write password generator function that uses the same rules as in Task 3.
    The password generator function must be able to generate all possible correct passwords.
    """

    from string import ascii_lowercase, ascii_uppercase, digits
    from random import randint, choice, sample

    all_char_sets = [ascii_lowercase, ascii_uppercase, digits, '#$@']
    all_chars = ascii_lowercase + ascii_uppercase + digits + '#$@'
    pas_len = randint(6, 12)
    result = ['' for i in range(pas_len)]

    for characters, index in zip(all_char_sets, sample(range(pas_len), 4)):
        result[index] = choice(characters)

    for i, char in enumerate(result):
        if not char:
            result[i] = choice(all_chars)

    return ''.join(result)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

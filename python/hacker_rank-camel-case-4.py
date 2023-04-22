# Enter your code here. Read input from STDIN. Print output to STDOUT

# C;V;can of coke
# S;M;sweatTea()
# S;V;epsonPrinter
# C;M;santa claus
# C;C;mirror

# S -> split
def split_text(s):
    # code here
    fix_s = s[4:].replace("()", "")

    new_s = str()

    for i, letter in enumerate(fix_s):
        if letter.isupper() and i != 0:
            new_s = fix_s[:i] + " " + fix_s[i:]

    print(new_s.lower())


def var_text(fix_s):
    fix_s = fix_s.split()
    new_s = fix_s[0]

    for word in fix_s[1:]:
        word_title = word.title()
        new_s = new_s + word_title

    return new_s

    # C -> combine


def combine_text(s):
    # code here
    fix_s = s[4:]
    new_s = str()

    # C -> Class
    if s[2] == 'C':
        fix_s = fix_s.split()
        for word in fix_s:
            word_title = word.title()
            new_s = new_s + word_title

    # M -> Method
    if s[2] == 'M':
        new_s = var_text(fix_s) + '()'

    # V -> Variable
    if s[2] == 'V':
        new_s = var_text(fix_s)

    print(new_s)


while True:

    try:
        s = input()

        if s[0] == 'S':
            split_text(s)
        elif s[0] == 'C':
            combine_text(s)
        else:
            break

    except EOFError:
        break

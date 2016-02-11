#regular expressions that work with pythex.org:

# match 'byte academy' 3 different ways
[a-z]{4}\s[a-z]{7}
\D{4}\s\D{7}
\D{12}

# an 8 character password, do not allow non word characters
# Use IGNORECASE. re.I, re.IGNORECASE
^[a-z]{8}$

# an 8 character password that has at least 1 number and 1 capital letter
^(?=.+[A-Z])(?=.+[0-9]).{8}$

#byteacademy@example.com
#byte.academy@example.com
#byteacademy22@example.co.uk
#See if you can get all three with 1 regex, but not invalid emails (not having an @, etc...)

^(?!.*([.])\1{1})(?!\A[.])(?!.*\.$)(?!.*\.@)(?!.*@\.)[^\s|@]+@[^\s|@]+\.[^\s|@]+$

var1 = 'Hello World!'
var2 = "Python Programming"

#Accessing values

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

#updating a string

print ("Updated String :- ", var1[:6] + 'Python')

#escape characters

'''
\a	0x07	Bell or alert
\b	0x08	Backspace
\cx		    Control-x
\C-x		Control-x
\e	0x1b	Escape
\f	0x0c	Formfeed
\M-\C-x		Meta-Control-x
\n	0x0a	Newline
\nnn		Octal notation, where n is in the range 0.7
\r	0x0d	Carriage return
\s	0x20	Space
\t	0x09	Tab
#\v	0x0b	Vertical tab
'''
#\x		Character x
#\xnn		Hexadecimal notation, where n is in the range 0.9, a.f, or A.F

#String operators

'''
+	Concatenation - Adds values on either side of the operator	a + b will give HelloPython
*	Repetition - Creates new strings, concatenating multiple copies of the same string	a*2 will give -HelloHello
[]	Slice - Gives the character from the given index	a[1] will give e
[ : ]	Range Slice - Gives the characters from the given range	a[1:4] will give ell
in	Membership - Returns true if a character exists in the given string	H in a will give 1
not in	Membership - Returns true if a character does not exist in the given string	M not in a will give 1
r/R	Raw String - Suppresses actual meaning of Escape characters. The syntax for raw strings is exactly the same as for normal strings with the exception of the raw string operator, the letter "r," which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and must be placed immediately preceding the first quote mark.	print r'\n' prints \n and print R'\n'prints \n
%	Format - Performs String formatting
'''

#example on Format operator

print ("My name is %s and weight is %d kg!" % ('Zara', 21))

'''
1	
%c

character

2	
%s

string conversion via str() prior to formatting

3	
%i

signed decimal integer

4	
%d

signed decimal integer

5	
%u

unsigned decimal integer

6	
%o

octal integer

7	
%x

hexadecimal integer (lowercase letters)

8	
%X

hexadecimal integer (UPPERcase letters)
9	
%e

exponential notation (with lowercase 'e')

10	
%E

exponential notation (with UPPERcase 'E')

11	
%f

floating point real number

12	
%g

the shorter of %f and %e

13	
%G

the shorter of %f and %E
'''

#String methods

'''
1	capitalize()
Capitalizes first letter of string

2	center(width, fillchar)
Returns a string padded with fillchar with the original string centered to a total of width columns.

3	count(str, beg = 0,end = len(string))
Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.

4	decode(encoding = 'UTF-8',errors = 'strict')
Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.

5	encode(encoding = 'UTF-8',errors = 'strict')
Returns encoded string version of string; on error, default is to raise a ValueError unless errors is given with 'ignore' or 'replace'.

6	endswith(suffix, beg = 0, end = len(string))
Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.

7	expandtabs(tabsize = 8)
Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.

8	find(str, beg = 0 end = len(string))
Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.

9	index(str, beg = 0, end = len(string))
Same as find(), but raises an exception if str not found.

10	isalnum()
Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.

11	isalpha()
Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.

12	isdigit()
Returns true if string contains only digits and false otherwise.

13	islower()
Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.

14	isnumeric()
Returns true if a unicode string contains only numeric characters and false otherwise.

15	isspace()
Returns true if string contains only whitespace characters and false otherwise.

16	istitle()
Returns true if string is properly "titlecased" and false otherwise.

17	isupper()
Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.

18	join(seq)
Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.

19	len(string)
Returns the length of the string

20	ljust(width[, fillchar])
Returns a space-padded string with the original string left-justified to a total of width columns.

21	lower()
Converts all uppercase letters in string to lowercase.

22	lstrip()
Removes all leading whitespace in string.

23	maketrans()
Returns a translation table to be used in translate function.

24	max(str)
Returns the max alphabetical character from the string str.

25	min(str)
Returns the min alphabetical character from the string str.

26	replace(old, new [, max])
Replaces all occurrences of old in string with new or at most max occurrences if max given.

27	rfind(str, beg = 0,end = len(string))
Same as find(), but search backwards in string.

28	rindex( str, beg = 0, end = len(string))
Same as index(), but search backwards in string.

29	rjust(width,[, fillchar])
Returns a space-padded string with the original string right-justified to a total of width columns.

30	rstrip()
Removes all trailing whitespace of string.

31	split(str="", num=string.count(str))
Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.

32	splitlines( num=string.count('\n'))
Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.

33	startswith(str, beg=0,end=len(string))
Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise.

34	strip([chars])
Performs both lstrip() and rstrip() on string

35	swapcase()
Inverts case for all letters in string.

36	title()
Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.

37	translate(table, deletechars="")
Translates string according to translation table str(256 chars), removing those in the del string.

38	upper()
Converts lowercase letters in string to uppercase.

39	zfill (width)
Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero).

40	isdecimal()
Returns true if a unicode string contains only decimal characters and false otherwise.
'''


Regular expressions often knows as regex or regexp, are powerful patterns used to research, match and manipulate strings of text. They provide a coincise and flexible means of describing complex search patterns in text.
A regular expression consists of a sequance of characters that form a search pattern. This pattern is then used to match and manipulate strings in various text-prosseing task, such as search and replace, input validation, data extractions, etc.

Here are some key concepts and syntax commonly used in regular expressions:
1. Literal characters: Regular expressions can include literal characters, such as letters, digits, and special characters. For example, the regex "apple" will match the string "apple" exactly.
2. Metacharacters: Metacharacters have special meanings and enable advanced pattern matching. Examples of metacharacters are:

- Dot (.) matches any character except a newline.
- Asterisk (*) matches zero or more occurrences of the preceding element.
- Plus sign (+) matches one or more occurrences of the preceding element.
- Question mark (?) matches zero or one occurrence of the preceding element.
- Square brackets ([ ]) define a character class, matching any single character within the brackets.
- Backslash () is used to escape metacharacters and represent special sequences.

3. Anchors: Anchors specify the position of a match within a string. Common anchors are:

- Caret (^) matches the start of a string.
- Dollar sign ($) matches the end of a string.
4. Quantifiers: Quantifiers specify how many times a pattern should occur. Examples include:

- Curly braces ({ }) specify the exact number of occurrences. For example, "a{3}" matches "aaa".
- Question mark (?), asterisk (*), and plus sign (+) are greedy quantifiers that match as much as possible.
- Adding a question mark after a greedy quantifier makes it lazy, matching as little as possible.
5. Character classes: Character classes allow matching a set of characters. Common examples are:
- \d matches any digit (0-9).
- \w matches any alphanumeric character (a-z, A-Z, 0-9, and underscore _).
- \s matches any whitespace character (space, tab, newline, etc.).

These are some questions that we shall be looking at:
0. Requirements:

The regular expression must match School
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method


1. Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method


2. Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method


3. Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method


4. Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Your regex should not contain square brackets


5. Requirements:

The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method


6. This task is brought to you by a professional advisor Neha Jain, Senior Software Engineer at LinkedIn.

Requirement:

The regular expression must match a 10 digit phone number


7. Requirement:

The regular expression must be only matching: capital letters


8. This exercise was prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on Twitter.

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

Your script should output: [SENDER],[RECEIVER],[FLAGS]
The sender phone number or name (including country code if present)
The receiver phone number or name (including country code if present)
The flags that were used
You can find a [log file here].

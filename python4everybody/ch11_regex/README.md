# Python Regular Expression Quick Guide

```
^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character

\s       Matches whitespace
\S       Matches any non-whitespace character

*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)

[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range

(        Indicates where string extraction is to start
)        Indicates where string extraction is to end

\b       Matches the empty string, but only at the start or end of a word.
\B       Matches the empty string, but not at the start or end of a word.

\d      Matches any decimal digit; equivalent to the set [0-9].
\D      Matches any non-digit character; equivalent to the set [^0-9].
```

# Unix/Linux 用户的彩蛋

> Support for searching files using regular expressions was built into the Unix operating system since the 1960s and it is available in nearly all programming languages in one form or another.

`grep` : Generalized Regular Expression Parser

```
$ grep '^From:' mbox-short.txt
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
```

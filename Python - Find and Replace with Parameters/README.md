Given a txt file containing a FORTRAN code (problem.txt) with entries that look like this:

c --- 5504 - Al (TOS210D130) universe --- <br/>
c <br/>
550401 104 -2.70 312300 -312301 -311302 <br/>
550402 102 -1.00 312300 -312301 311302 <br/>


This Python Script will do the following:

- Ask for User Input:
- If the user inputs "A", it will replace the 2nd and 3rd entries of universe 5504 with "102 -1.00". The entries must be separated by at least one space.
- If the input is "B", do it with the universe 5505.
- C --> 5506
- D --> 5507
- E --> 5508
- F --> 5509
- The user can also mix the parameters typing, for example: "ABEF", and the script will do the changes corresponding to A, B, E, F
- Then the script will save a new txt file with the name appended with the input, e.g. "problem-ABEF.txt".
- If the universe does not exist, it will print "whoops" and no file will be generated


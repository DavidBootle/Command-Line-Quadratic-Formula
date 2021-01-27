# Command Line Quadratic Formula
 Allows you to calculate solutions to quadratics from the command line. Could be useful, I don't know. Program is for Windows 10, but may work on other versions of Windows.
 
 ## Installation
 Download the file `quadform.exe` in the dist directory. This is the exe you will use to run the command. Place it in the directory you are going to use it in or add it's directory to path to access it globally.
 
 ## Usage
 The syntax is `quadform a b c` where `a`, `b`, and `c` are numbers that can be converted into a float. `a`, `b`, and `c` relate to the coefficients of the base quadratic equation, as shown: `ax^2+bx+c`.
 
 Once run, the program will output `The solutions are __ and __`. If the solutions are complex numbers, they will be displayed as `(real + (imag)j)`. For example, `3i + 2` would be displayed as `(2 + 3j)`. The program will check to see if the solution is a fraction, and if it is, it will output in fraction form. Otherwise, the solution will output either integers or decimals.
 
## Example
To get the solutions for the quadratic equation `3x^2 + 4x -15`:

```batch
> quadform 3 4 -15
The solutions are -3 and 5/3
```

# Program to find prime factors of a number

A program that take one number as an input from user via user interface. The
programs finds all possible prime factors of the entered number, but not duplicates. It
prints those numbers to screen and make an output file containing asked number and its prime
factors.
To make it faster program also creates file database to store  already requested numbers, so
there would not be need to make another search but get valid information from database. If
database file doesn’t exist, program will create it. Program  also outputs how long
it took to calculate or get prime factors.

## How ro run

python prime_factors.py

Example UI:

python prime_factors.py
Give me the number: 26541
Prime factor found: 3
Prime factor found: 983
It took 0,93 seconds to find those

Example output file content:
Prime Factors of number 26541 are
3, 983
It took 0,93 seconds to find those

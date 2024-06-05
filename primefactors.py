# Program to print out all prime factors of a number ignoring dulicates and also calculate the time
# it takes to find them

import time
import sys

def get_prime_numbers(n, prime_db_data):
    primfactors = {}
    
    # check for existing records
    if(n in prime_db_data.keys()):
         prime_keys = prime_db_data[n]
         prime_keys_list = prime_keys.split(",")
         for n in prime_keys_list:
           print('Prime factor found:', n) 
         return prime_keys_list
          
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            if d not in primfactors: # skip duplicates
               primfactors[d]=d
               print('Prime factor found:', d)                  
            n //= d
        d += 1
    if n > 1:
       if d not in primfactors:  #skip dulicates
         primfactors[n]=n
         print('Prime factor found:', n) 
    return list(primfactors.keys())

# write results to file names prime_number.dat
def writeFile(number, prime_numbers, elapsed_time):
     file_name = 'prime_number.dat'
     prime_numbers_str = ','.join(map(str, prime_numbers)) 
     try:
        file=open(file_name, 'w')
        file.write('Prime Factors of number ' + str(number) + ' are\n')
        file.write(prime_numbers_str + '\n')
        file.write('It took ' + str(elapsed_time) + ' seconds to find those\n') 
        file.close()   
     except OSError:
        print('Error writing file')

# read and store to dictionary
def read_prime_db(): 
    file_name = 'primes.db'
    data = {}
    try:
        with open(file_name, 'r') as tiedosto:
            for row in tiedosto:
                osat = row.strip().split(':')
                if len(osat) == 2:
                   data[str(osat[0])]=osat[1]
        return data
    except FileNotFoundError:
        return {}
    except Exception as e:
        return {}

# update prime number file database       
def update_prime_db(number,prime_numbers): 
    file_name = 'primes.db'
    prime_numbers_str = ','.join(map(str, prime_numbers)) 
    file=open(file_name, 'a')
    file.write(str(number) + ":" + prime_numbers_str +'\n')
    file.close() 
def getInput(userInput):
    try:
       value = int(input(userInput))
       return value
    except ValueError:
       print("Invalid input, please enter an integer")
       sys.exit(0)
             
def mainprogram():
     prime_db_data = read_prime_db() # read db into memory
     number = getInput('Give me the number:')
     start_time = time.perf_counter_ns() # nano second precision
     prime_keys = get_prime_numbers(number, prime_db_data)         
     end_time = time.perf_counter_ns()  # nano second precision
     elapsed_time = (end_time - start_time)/1000000000   # nano second precision
     print('It took %.9f seconds to find those' % elapsed_time)  
     writeFile(number,prime_keys,elapsed_time)
     if(str(number) not in prime_db_data.keys()):
         update_prime_db(number,prime_keys)


mainprogram()
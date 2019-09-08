# Functions during my journey
URL: https://docs.python.org/3/library/stdtypes.html#truth

## Built-in Functions

- bin(x)   
  x must be an integer number. bin() function will convert to a binary *string* prefixed with `0b`.  
  
   - Example and Format:  
     ```
     >>> bin(11)  
     '0b1011'
     ```

     ```
     >>>format(33, '#b')
     '0b100001'
     ```

     ```
     >>>format(21, 'b')
     '10101'
     ```

     ```
     >>>f'{55:#b}'
     '0b110111'
     ```

     ```
     >>>f'{78:b}'
     '1001110'

- format(x)  
  

- bool(x)  
  - Truth Value Tetsing. By default, an object is considered true unless its class defines either a `__bool()__()` method that returns `False` or a `__len__()` method that returns zero.  
  - The following are the most build-in objects considered false:  
    - Constants defined to be false: `None` and `False`.  
    - Zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0,1)`.  
    - Empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`  


- ord(x) and chr(i)  
  x must be string.  
  i must be integer.  
  ord(x) will return an integer representing the Unicode code point of that string.  
  chr(i) returns the string representing a character whose Unicode code point is the integer `i`
  

# Getting Started
# Create a differences.py file and convert all the Javascript functions below into Python in that file.
# The Functions
# Get Name
# Write a method that accepts a name from the user and then returns it. Here’s the javascript:

# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

user_input = input('What is your name? ')
print(user_input + "? That's a dumb name.")

# Reverse It
# Write a method that reverses a string. Here’s the javascript:


# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };

dork = 'a man, a plan, a canal, frenemies!'
reversed_dork = dork[::-1]
print(reversed_dork)


# Swap Em
# Write a method that swaps the values of two variables around. Here’s the javascript:

# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

a = 10
b = 30

a, b = b, a
print(a)
print(b)

# Multiply Array/List
# Write a method that multiplies all numbers in a given array/list and returns the final product. Here’s the javascript:

# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

numbers = [2, 3, 4, 5, 6]
product = 1

for num in numbers:
    product *= num

print(product)

#   return total;
# };
# Fizz Buzzer
# Write a method that takes a number argument and returns “fizz” if the number is divisible by three, “buzz” if the number is divisible by five, and “fizzbuzz” if it’s divisible by both. Here’s the javascript:

# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }

number = 5

if number % 3 == 0 and number % 5 == 0:
    print('fizzbuzz')
elif number % 3 == 0:
    print('fizz')
elif number % 5 == 0:
    print('buzz')
else:
    print('number')

# Nth Fibonacci
# Write a method that finds the fibonacci number at the nth position and returns it. Here is the javascript:

# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };

print("Bro, what is a Fibonacci number?  I'll come back to this one")

# Search Array/List
# Write a method that searches through an array/list for a value and returns true or false depending on whether or not the value is present in the array/list. Here is the javascript:

# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };

num_list = [1, 3, 5, 7, 9]

def search_array(arr, value):
    for item in arr:
        if item == value:
            return True
    return False
    
print(search_array(num_list, 6))
print(search_array(num_list, 5))

# Palindrome
# Write a method that checks whether or not a string is a palindrome. Here is the javascript:

# const isPalindrome = (str) => {
#   for(let i = 0; i < str.length/2; i++){
#     if(str[i] != str[str.length-i-1]){
#       return false;
#       break;
#     }
#   }
#   return true;
# };
# hasDupes
# Write a method that checks whether or not an array/list has any duplicates. Here is the javascript:

# const hasDupes = (arr) => {
#   let obj = {};
#   for (i = 0; i < arr.length; i++) {
#     if(obj[arr[i]]) {
#       return true;
#     }
#     else {
#       obj[arr[i]] = true;
#     }
#   }
#   return false;
# };


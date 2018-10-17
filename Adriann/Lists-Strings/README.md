# Lists, Strings
If your language of choice doesn't have a built-in list and/or string type (e.g. if you use C), these exercises should be 
solvable for arrays. However, some solutions are very different between an array-based list (like 
<span style="font-family:Consolas;">C++'s vector</span>) and a pointer based list (like 
<span style="font-family:Consolas;">C++'s list</span>), at least if you care about the efficiency of your code. So you 
might want to either find a library, or investigate how to implement your own linked list if your language doesn't have 
it.

---
1. Write a function that returns the largest element in a list.
2. Write a function that reverses a list, preferably in place.
3. Write a function that checks whether an element occurs in a list.
4. Write a function that returns the elements on odd positions in a list.
5. Write a function that computes the running total of a list.
6. Write a function that tests whether a string is a palindrome.
7. Write three functions that compute the sum of the numbers in a list: using a <b>for-loop</b>, a <b>while-loop</b> 
and <b>recursion</b>. (Subject to availability of these constructs in your language of choice.)
8. Write a function on <span style="font-family:Consolas;">\_all</span> that applies a function to every element of a list.
Use it to print the first twenty perfect squares. The prefect squares can be found by multiplying each natural number
with itself. The first few perfect squares are: <b>1\*1 = 1, 2\*2 = 4, 3\*3 = 9, 4\*4 = 16</b>. Twelve for example is not
a perfect square because there is no natural number <b>m</b> so that <b>m*m = 12</b>. (This question is tricky if your
programming language makes it difficult to pass functions as arguments.)
9. Write a function that concatenates two lists:
<pre>[a, b, c], [1, 2, 3] -> [a, b, c, 1, 2, 3]</pre>
10. Write a function that combines two lists by alternating values from each list:
<pre>[a, b, c], [1, 2, 3] -> [a, 1, b, 2, c, 3]</pre>
11. Write a function that merges two sorted lists into a new sorted list:
<pre>[1, 4, 6], [2, 3, 5 -> [1, 2, 3, 4, 5, 6]</pre>
12. Write a function that rotates a list by <b>k</b> elements. For example: <code>[1, 2, 3, 4, 5, 6]</code> rotated by
two becomes <code>[3, 4, 5, 6, 1, 2]</code>. Try solving this without creating a copy of the list. How many swap or move
operations do you need?
13. Write a function that computes the list of the first 100 Fibonacci numbers. The first two Fibonacci numbers are 1 and 1.
The n+1<sup>st</sup> Fibonacci number can be computing by adding the n<sup>th</sup> and the n-1<sup>th</sup> Fibonacci
number. The first few are therefore: <code>1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8 . . . </code>
14. Write a function that takes a number and returns a list of its digits. So for <b><code>2342</code></b>, it should return
<b><code>[2, 3, 4, 2]</code></b>.
15. Write functions that add, subtract, and multiply two numbers in their digit-list representation (and return a new digit
list). If you're ambitious, you can implement Karatsuba multiplication. Try different bases. What is the best base if you
care about speed? If you couldn't completely solve the prime number exercise above due to the lack of large numbers in your
language, you can now use your own library for that task.
16. Write a function that takes a list of numbers, a starting base <b>b1</b> and a target base <b>b2</b> and interprets
the list as a number in base <b>b1</b> and converts it into a number int base <b>b2</b> (in the form of a list-of-digits.
So for example: <code>[2, 1, 0]</code> in base <b>3</b> gets converted to base <b>10</b> as <code>[2, 1]</code>.
17. Implement the following sorting algorithms: Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Stooge Sort.
Check Wikipedia for descriptions.
18. Implement binary search.
19. Write a function that takes a list of strings and prints them, one per line, in a rectangular frame. For example the list
<code>["Hello", "World", "in", "a", "frame"]</code> gets printed as: NOT YET IMPLEMENTED
20. Write a function that translates a text to Pig Latin and back. English is translated to Pig Latin by taking the first
letter of every word, moving it to the end of the word by adding 'ay'. "The quick brown fox" becomes "Hetay uickqay
rownbay oxfay".

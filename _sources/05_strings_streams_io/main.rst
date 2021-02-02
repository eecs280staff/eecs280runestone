.. qnum::
   :prefix: Q
   :start: 1

.. raw:: html

   <link rel="stylesheet" href="../_static/common/css/main4.css">
   <link rel="stylesheet" href="../_static/common/css/code3.css">
   <link rel="stylesheet" href="../_static/common/css/buttons3.css">
   <link rel="stylesheet" href="../_static/common/css/exercises3.css">
   <script src="../_static/common/js/common2.js"></script>
   <script src="../_static/common/js/lobster-exercises8.bundle.js"></script>

.. raw:: html

   <style>
      .btn {
         margin: 0;
      }
      .tab-pane {
         padding: 0;
      }
   </style>

=======================================================================
Strings, Streams, and I/O
=======================================================================

This lecture is all about text, or more precisely any data that can be represented as a sequence of characters. This is a natural form for human-friendly data, but it's also used for 

TODO

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C-Style Strings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

We'll start with the most fundamental representation for a string: an **array of characters**. We'll call this a C-style string (or cstring for short), because this is the predominant form for strings in the original C language.

There's one additional trick to C-style strings - instead of keeping track of the length of the array of characters separately (e.g. in an int variable that we pass along to any array functions), we instead mark the end of the string data in the array with a special character called a **sentinel**. Any code processing the string keeps an eye out for the sentiel value to know when to stop.

Here's a brief introduction:

.. youtube:: TODO
   :divid: ch05_01_vid_intro_to_cstrings
   :height: 315
   :width: 560
   :align: center

|

To recap:

- A cstring is a sequence of characters, living in an array, terminated by a null character (:code:`\0`).
- The null character acts as a sentinel, so that code processing the cstring knows where to stop.
- When initializing a cstring from a string literal, the compiler automatically adds the null character for us.
- It's customary to work with cstrings via traversal by pointer.

There are three main options for creating a cstring:

- | :code:`const char *welcomeMsg = "Welcome to EECS 280!";`
  | Point at a string literal. We can use it, but we don't plan to modify the contents (and the compiler enforces this with the const).
- | :code:`char hexColor[] = "00274C";`
  | Create a local array to contain a *copy* of the given cstring. The example here has space for 7 characters (6 regular plus the null character). We can modify the contents however we want, but the size is fixed.
- | :code:`char filename[1024];`
  | Create a "buffer" that may hold many different cstrings (one at a time). The array contains lots of space, because some strings might be longer than others. The placement of the null character lets us know the end of the current cstring living in the buffer. For example, we might want to iterate through a list of file names and process them.

**Exercise**

   TODO

.. fillintheblank:: ch04_01_ex_arrays_and_memory
   :casei:

   Determine whether each of the following statements are true or false.
   
   |blank| Arrays can be resized if you need more space.
   
   |blank| The elements in an array are stored contiguously in memory.
   
   |blank| All elements in a particular array must be the same type.
   
   |blank| All individual array elements must be the same size in memory.
   
   |blank| Each array element lives at the same address in memory.

   - :false|f: Correct!
     :.*: Try again
   - :true|t: Correct!
     :.*: Try again
   - :true|t: Correct!
     :.*: Try again
   - :true|t: Correct!
     :.*: Try again
   - :false|f: Correct!
     :.*: Try again

|

.. admonition:: Walkthrough

   .. reveal:: ch04_01_revealwt_arrays_and_memory
  
      **false** Arrays can be resized if you need more space.
   
      **true** The elements in an array are stored contiguously in memory.
      
      **true** All elements in a particular array must be the same type.
      
      **true** All individual array elements must be the same size in memory.
      
      **false** Each array element lives at the same address in memory.

|

-----------------------------------------------------------------------
Processing C-style Strings
-----------------------------------------------------------------------

For almost any operation we would like to perform on a cstring, the basic idea is that we set up a traversal by pointer loop that iterates until it happens upon the null character. Let's take a look at how this plays out in code and a few examples.

.. youtube:: TODO
   :divid: ch05_01_vid_processing_cstrings
   :height: 315
   :width: 560
   :align: center

|


-----------------------------------------------------------------------
The :code:`<cstring>` Library
-----------------------------------------------------------------------

Because cstrings are just built on fundamental types like arrays, :code:`char`, and pointers, you don't need to include any libraries to use them. However, many common operations for cstrings are available as functions in the :code:`<cstring>` Library, which you can :code:`#include` at the top of your files if you need them. You can find documentation for these in a number of places, but online resources like `http://www.cplusplus.com/reference/cstring/ <http://www.cplusplus.com/reference/cstring/>`_ are generally a good place to start.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C++ Strings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

TODO

.. youtube:: DyEOyWsHAUc
   :divid: ch04_02_vid_arrays_pointers_pointer_arithmetic
   :height: 315
   :width: 560
   :align: center

|



**Exercise**

TODO? Probably just save for later with I/O exercise

.. admonition:: Walkthrough

   .. reveal:: ch04_02_revealwt_arrays_pointers_pointer_arithmetic
  
      .. youtube:: LaBI6fgTOAM
         :divid: ch04_02_wt_arrays_pointers_pointer_arithmetic
         :height: 315
         :width: 560
         :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Command Line Arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

TODO

.. youtube:: ffPi8C1tXek
   :divid: ch04_03_vid_pointer_comparisons
   :height: 315
   :width: 560
   :align: center

|

To get an argument out of :code:`argv`, you generally just use indexing, e.g. :code:`argv[x]` where :code:`x` is the index of the argument you want. Remember that the argument at index :code:`0` is just the name of the executable, so your "real" arguments will start indexed at :code:`1`.

Once you have an argument, there are three things you might want to do with it:

- | :code:`string redactWord = argv[1];`
  | Immediately convert it to a C++ string (e.g. by storing in a :code:`string` variable). C++ strings are MUCH easier to work with and support convenient operators like :code:`==`.
- | :code:`ifstream fin(argv[2]);`
  | :code:`ofstream fout(argv[3]);`
  | Use it directly somewhere that a cstring is readily accepted. For example, an :code:`ifstream` or :code:`ofstream` can be constructed from a cstring with the name of an input/output file.
- | :code:`int redactLength = atoi(argv[4]);`
  | For arguments you want to interpret as a number (rather than a "string of digits"), convert it to an :code:`int` using :code:`atoi()` or to a :code:`double` using :code:`atof()`.

- 

**Exercise**

.. fillintheblank:: ch04_03_ex_pointer_comparisons
   :casei:

   Given an array and some pointers:

   .. code-block:: cpp

      int main() {
        int arr[5] = { 5, 4, 3, 2, 1 };
        int *ptr1 = arr + 2;
        int *ptr2 = arr + 3;
      }

   Write true or false for each of these comparisons

   |blank| :code:`ptr1 == ptr2`
   
   |blank| :code:`ptr1 == ptr2 - 1`
   
   |blank| :code:`ptr1 < ptr2`
   
   |blank| :code:`*ptr1 < *ptr2`
   
   |blank| :code:`ptr1 < arr + 5`

   - :false|f: Correct!
      :.*: Try again
   - :true|t: Correct!
      :.*: Try again
   - :true|t: Correct!
      :.*: Try again
   - :false|f: Correct!
      :.*: Try again
   - :true|t: Correct!
      :.*: Try again

|

.. admonition:: Walkthrough

   .. reveal:: ch04_03_revealwt_pointer_comparisons
  
      **false** :code:`ptr1 == ptr2`
      
      **true** :code:`ptr1 == ptr2 - 1`
      
      **true** :code:`ptr1 < ptr2`
      
      **false** :code:`*ptr1 < *ptr2`
      
      **true** :code:`ptr1 < arr + 5`

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Traversal by Pointer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 4

There are two fundamental ways to approach sequential access of the elements in an array using a loop, which we might also call "traversal" or "iteration" through the array's elements:

- Traversal by **Index**: Start an index variable (e.g. :code:`i`) at :code:`0`, increase it by 1 on each iteration of the loop, and plug :code:`i` into an indexing operation to find each element of the array.
- Traversal by **Pointer**: Start a pointer (e.g. :code:`ptr`) at the beginning of an array, move it forward one space in memory on each iteration, and dereference it along the way to visit each element of the array.

.. youtube:: NtnOo1MNoCE
   :divid: ch04_04_vid_traversal_by_pointer
   :height: 315
   :width: 560
   :align: center

|

Neither of traversal by pointer or traversal by index is fundamentally better or more efficient. You should use the one that feels more natural to you, unless there's a requirement for you to do otherwise. For many people, in most use cases, that's probably traversal by index.

However, we're taking a look at traversal by pointer now because:

1. It's another interesting thing you can do with pointers.
2. It is customarily used in certain contexts, like with C-style strings, which we'll look at next time.
3. It's conceptually similar to traversal by *iterator*, which we'll learn about later on in the course.

**Exercise**

Which of the following code snippets correctly implement traversal by pointer?

.. shortanswer:: ch04_04_ex_traversal_by_pointer_01

   Does this code snippet correctly implement traversal by pointer over the array `arr` to print out each of the array's elements? If not, what's wrong with it? Why does this cause a problem?

   .. code-block:: cpp

      int arr[5] = {1,2,3,4,5};
      
      for(int *ptr = 0; ptr < 5; ++ptr) {
         cout << *ptr << endl;
      }

.. shortanswer:: ch04_04_ex_traversal_by_pointer_02

   Does this code snippet correctly implement traversal by pointer over the array `arr` to print out each of the array's elements? If not, what's wrong with it? Why does this cause a problem?

   .. code-block:: cpp

      int arr[5] = {1,2,3,4,5};
      
      for(int *ptr = arr; ptr < arr + 5; ++ptr) {
         cout << ptr << endl;
      }

.. shortanswer:: ch04_04_ex_traversal_by_pointer_03

   Does this code snippet correctly implement traversal by pointer over the array `arr` to print out each of the array's elements? If not, what's wrong with it? Why does this cause a problem?

   .. code-block:: cpp

      int arr[5] = {1,2,3,4,5};
      
      for(int *ptr = arr; ptr < ptr + 5; ++ptr) {
         cout << *ptr << endl;
      }

Surprise! Each of the code snippets in the questions about contains a mistake. If you didn't find this, double check the ones you hadn't found yet, take a look at the code on `Lobster <https://lobster.eecs.umich.edu>`_ in exercise :file:`L04.2_traversal_by_pointer`, or check out the walkthrough video.

.. admonition:: Walkthrough

   .. reveal:: ch04_04_revealwt_traversal_by_pointer
  
      .. youtube:: PEgsl2a30Sc
         :divid: ch04_04_wt_traversal_by_pointer
         :height: 315
         :width: 560
         :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Array Parameters and Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 5

When working with arrays, it's often helpful to write helper functions that process the arrays in some way, perhaps using a loop to iterate through each element and perform some operation.

An example of this would be a function that prints out an array...

.. youtube:: esTbqG1K24U
   :divid: ch04_05_vid_array_functions_and_parameters
   :height: 315
   :width: 560
   :align: center

|

Two big takeaways here:

1. The compiler turns array parameters into pass-by-pointer behind the scenes. That gives us a pointer we can use to access the original array. This is similar to pass-by-reference, but technically different.
2. Because of 1., the only thing passed into an array function is a pointer to the first element. That means we have to pass the size of the original array as a separate parameter.


**Exercise**

Write a function called :code:`maxValue` that finds the value of the maximum element in the array. Here's an example of how you might use the function:

.. code-block:: cpp

   int main(){
     int arr[4] = {2, 3, 6, 1};
     int m = maxValue(arr, 4); // Pass ptr to first elem of arr, plus size
     cout << m << endl; // prints 6
   }

This exercise is available on `Lobster <https://lobster.eecs.umich.edu>`_ as :code:`L04.3_maxValue`. Lobster includes a few checkpoints for the individual elements of traversal-by-pointer to help you track your progress.

.. shortanswer:: ch04_05_ex_array_functions_and_parameters

   Paste your finished code for the exercise here.

   

.. admonition:: Walkthrough

   .. reveal:: ch04_05_revealwt_array_functions_and_parameters
  
      .. youtube:: lJ7cLJwddYI
         :divid: ch04_05_wt_array_functions_and_parameters
         :height: 315
         :width: 560
         :align: center

|
.. qnum::
   :prefix: Q
   :start: 1

.. raw:: html

   <script src="../_static/common/js/common2.js"></script>

.. raw:: html

   <style>
      .btn {
         margin: 0;
      }
      .tab-pane {
         padding: 0;
      }
   </style>

======================================================================
Arrays
======================================================================

You'll often want to represent containers or sequences of data in your programs, and how to do this in a way that makes the data easily (for you) and efficiently (for the computer) accessible is one of the fundamental questions in the *data structures*. In C++, there are a lot of options, and we'll take a look at many throughout the course. These same sorts of data structures are applicable in most any programming language and thinking through which data structures to use for a particular problem is one of the fundamentals of good programming.

To start, we'll focus on **arrays**, which are the most basic container for sequential data and also one of the most ubiquitous. In fact, *many* other containers, including :code:`vector` and :code:`string`, are actually built on top of arrays! (We'll come back to this later.)

We'll also see that arrays provide very efficient access to data in a couple different ways:

- **Sequential Access**: Iterating through a sequence of elements from start to end.
- **Random Access**: Accessing an element at a particular index (i.e. position) in the sequence.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Arrays and Memory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

Arrays are a low-level abstraction over memory that we can fit into the memory model we've been building up so far...

.. youtube:: 4r_X4JyNLT0
   :divid: ch04_01_vid_arrays_and_memory
   :height: 315
   :width: 560
   :align: center

|

**Exercise**

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

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Arrays, Pointers, and Pointer Arithmetic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

Because an array is essentially just a sequence of objects (one for each element in the array) that are laid out contiguously in memory, we can leverage pointers (i.e. addresses) to work with arrays. Here's one example, informally:

   How does array indexing work? For example, how does :code:`arr[7]` know where to find the memory object for the element at index 7? Well, let's say we can find the address of the first element in the array, and call it :math:`A`. Then, we also know that :code:`arr` contains integers, which each take up 4 bytes in memory. Then, because arrays are always contiguous in memory, we can compute that :code:`arr[7]` is :math:`7*4` bytes from the beginning of the array. It's address should then be :math:`A + 7 * 4`.

Let's take a look at the details of how this works in code, including the relationship between arrays and pointers and building up to array indexing.

.. youtube:: DyEOyWsHAUc
   :divid: ch04_02_vid_arrays_pointers_pointer_arithmetic
   :height: 315
   :width: 560
   :align: center

|

.. admonition:: Heads Up!

   Unlike the informal example before the video, when you use pointer arithmetic in code, you can just write something like :code:`arr + i`. You don't need to specify how many bytes each array element takes, since the compiler already knows this from the type of the pointer (e.g. an :code:`int *` points into an array of :code:`int`, and the compiler knows how many bytes an :code:`int` will take up on its target machine architecture).

**Exercise**

Trace this code and draw a memory diagram as you go. Once you're finished, use your diagram to answer the question below.

.. code-block:: cpp

   int main() {
     int arr[5] = {6, 3, 2, 4, 5};
     int *a = arr;
     int *b = arr + 2;
     int *c = b + 1;
     int *d = &arr[1];
   
     ++a;
     --b;
     c = d;
     c += 2;
   
     cout << *a << endl;
     cout << *(a + 2) << endl;
     cout << (a - d) << endl;
     cout << (b - c) << endl;
     cout << b[2] << endl;
     cout << *(arr+5) << endl;
   }

.. fillintheblank:: ch04_02_ex_arrays_pointers_pointer_arithmetic

   What values are printed for each of the expressions sent to :code:`cout` at the end of the program? If the expression results in undefined behavior, write "undefined".

   |blank| :code:`*a`
   
   |blank| :code:`*(a + 2)`
   
   |blank| :code:`(a - d)`
   
   |blank| :code:`(b - c)`
   
   |blank| :code:`b[2]`
   
   |blank| :code:`*(arr+5)`

   - :3: Correct!
     :.*: Try again
   - :4: Correct!
     :.*: Try again
   - :0: Correct!
     :.*: Try again
   - :-2: Correct!
     :.*: Try again
   - :4: Correct!
     :.*: Try again
   - :undefined: Correct!
     :.*: Try again


To check your work, find the file :file:`L04.pointer_arithmetic` in the EECS 280 code on `Lobster <https://lobster.eecs.umich.edu>`_. You can use the simulation to check your diagram and to see the correct output for each expression. If you'd like, you can also make a personal copy of the code and change it around to answer any "what-if" questions or get more practice predicting the program's behavior.


.. admonition:: Walkthrough

   .. reveal:: ch04_02_revealwt_arrays_pointers_pointer_arithmetic
  
      .. youtube:: LaBI6fgTOAM
         :divid: ch04_02_wt_arrays_pointers_pointer_arithmetic
         :height: 315
         :width: 560
         :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Pointer Comparisons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

Just like we can do arithmetic with pointers in a natural way, shifting addresses back and forth, we can also implement pointer comparisons in terms of addresses. Basically, :code:`ptr1 < ptr2` will be true if and only if :code:`ptr1` points to an address that is numerically lower than the address :code:`ptr2` points to. Or, put simply, if :code:`ptr1` is pointing somewhere before :code:`ptr2` in memory.

Here's a video of me saying that, plus a couple additional details/restrictions :). 

.. youtube:: ffPi8C1tXek
   :divid: ch04_03_vid_pointer_comparisons
   :height: 315
   :width: 560
   :align: center

|

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

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Traversal by Pointer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Array Parameters and Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
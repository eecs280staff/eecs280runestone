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

============================================================================================
The Call Stack and Procedural Abstraction
============================================================================================

This chapter is all about functions, but from two different, complementary perspectives:

1. Expanding our conceptual model of program execution and memory to include functions.
2. Understanding how functions and procedural abstraction contribute to good program design.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Intro to Lobster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

Before we start, let me cover a few basics for the `Lobster <https://lobster.eecs.umich.edu>`_ program visualization tool, which we'll use throughout several lecture examples and exercises in the future.

.. youtube:: SyYblfASLlE
   :divid: ch02_01_vid_intro_to_lobster
   :height: 315
   :width: 560
   :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Functions and The Call Stack
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

The memory allocated for each function is generally called an **activation record** or (more commonly) a **stack frame**. Each function takes up a certain amount of memory that depends on how many local variables it may need to store, and this memory is allocated and freed as needed during the program.

Because of the way that functions call work (i.e. the called function has to finish and return before you can start back up in the original function), it's natural to use a stack to represent the memory frames for each function. Whichever function is called most recently is added to the top of the stack, and will always be removed before any other functions that were already on the stack (this is called the "Last In First Out" or "LIFO" property).

.. youtube:: jT077RVOUgk
   :divid: ch02_02_vid_functions_and_the_call_stack
   :height: 315
   :width: 560
   :align: center

|

**Exercise**

Consider the following code, which is also available on `Lobster <https://lobster.eecs.umich.edu>`_ as :file:`L02.2_call_stack` in the eecs280 exercises. Trace through the code either manually or using the Lobster simulation and answer the questions below.

.. code-block:: cpp

   #include <iostream>
   using namespace std;
   
   int min(int x, int y) {
     if (x < y){ return x; }
     else{ return y; }
   }
   
   int minOf3(int x, int y, int z) {
     int a = min(x, y);
     int b = min(y, z);
     return min(a, b);
   }
   
   int main() {
     int a = 3;
     int b = 4;
     int c = 5;
   
     // prints 3
     cout << minOf3(a, b, c);
   }

.. shortanswer:: ch02_02_ex_functions_and_the_call_stack_01

   Which function has the largest stack frame (in terms of memory use)? How can you tell? Is this a compile-time property or a runtime property?

.. shortanswer:: ch02_02_ex_functions_and_the_call_stack_02

   What is the maximum amount of memory on the (call) stack needed by the program at any one given time? Assume an :code:`int` takes up 4 bytes, and that the memory to store local :code:`int` objects is the only memory used by the program. 

.. shortanswer:: ch02_02_ex_functions_and_the_call_stack_03

   How many different stack frames are created for the :code:`min()` function throughout the execution of the program?


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Parameter Passing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

Two primary mechanisms for parameter passing are pass-by-value and pass-by-reference. Let's take a look at the differences between the two, as well as how they relate to function stack frames.

.. youtube:: xetnP9gQXEY
   :divid: ch02_03_vid_parameter_passing
   :height: 315
   :width: 560
   :align: center

|

You can find examples of both the pass-by-value and pass-by-reference versions of :code:`swap()` on `Lobster <https://lobster.eecs.umich.edu>`_ as :file:`L02.3_swap` in the eecs280 exercises.

**Exercise**

.. fillintheblank:: ch02_03_ex_parameter_passing

   Consider this code:

   .. code-block:: cpp

      #include <iostream>
      using namespace std;
      
      int func(int x, int &y, int &z) {
        x = z;
        y = z;
        return z + 1;
      }
      
      int main() {
        int a = 1;
        int b = 2;
        int c = 3;
        
        int d = func(a, b, c);
      }

   What are the values of each variable at the end of the main function?
   
   |blank| :code:`a`
   
   |blank| :code:`b`
   
   |blank| :code:`c`
   
   |blank| :code:`d`

   - :1: Correct!
     :.*: Try again
   - :3: Correct!
     :.*: Try again
   - :3: Correct!
     :.*: Try again
   - :4: Correct!
     :.*: Try again


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Procedural Abstraction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 4

Turning now to our second, higher-level point, how can we use functions to implement effective procedural abstractions that make our code easier to write, understand, and maintain?

.. youtube:: WVqOirVNBqI
   :divid: ch02_04_vid_procedural_abstraction
   :height: 315
   :width: 560
   :align: center

|

**Exercise**

.. fillintheblank:: ch02_04_ex_procedural_abstraction

   Categorize each of the following according to whether they are part of the interface or implementation (write "interface" or "implementation" in each box).
   
   |blank| Function declaration in .h file
   
   |blank| Function definition in .cpp file
   
   |blank| Code inside the function's curly braces
   
   |blank| Which input values are valid or invalid for the function
   
   |blank| Comments inside the function to clarify tricky lines of code
   
   |blank| RME comment before the function declaration in .h file

   - :interface: Correct!
     :.*: Try again
   - :implementation: Correct!
     :.*: Try again
   - :implementation: Correct!
     :.*: Try again
   - :interface: Correct!
     :.*: Try again
   - :implementation: Correct!
     :.*: Try again
   - :interface: Correct!
     :.*: Try again









^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Project 1 File Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 5



.. youtube:: a26xmgSPE6U
   :divid: ch02_05_vid_project1_file_structure
   :height: 315
   :width: 560
   :align: center

|



^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RMEs (Interface Specification Comments)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 6



.. youtube:: pQKP0SucFgY
   :divid: ch02_06_vid_rmes
   :height: 315
   :width: 560
   :align: center

|
   


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 7



.. youtube:: mpmqISAUacI
   :divid: ch02_07_vid_testing
   :height: 315
   :width: 560
   :align: center

|
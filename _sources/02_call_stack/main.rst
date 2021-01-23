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


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Intro to Lobster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

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



.. youtube:: jT077RVOUgk
   :divid: ch02_02_vid_functions_and_the_call_stack
   :height: 315
   :width: 560
   :align: center

|

**Exercise**

Consider the following code, which is also available on Lobster as :file:`L02.2_call_stack` in the eecs280 exercises. Trace through the code either manually or using the Lobster simulation and answer the questions below.

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



.. youtube:: xetnP9gQXEY
   :divid: ch02_03_vid_parameter_passing
   :height: 315
   :width: 560
   :align: center

|

You can find examples of both the pass-by-value and pass-by-reference versions of :code:`swap()` on Lobster as :file:`L02.3_swap` in the eecs280 exercises.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Procedural Abstraction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 4



.. youtube:: WVqOirVNBqI
   :divid: ch02_04_vid_procedural_abstraction
   :height: 315
   :width: 560
   :align: center

|




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
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

=======================================================================
Abstract Data Types in C
=======================================================================

.. TODO

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Introduction to ADTs in C
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

.. TODO

.. youtube:: sX2-rECyB8M
   :divid: ch07_01_vid_intro_to_adts_in_c
   :height: 315
   :width: 560
   :align: center

|

.. TODO

**Exercise**

Let's say we want to add a function to scale a triangle by a given factor. Here's an example:

.. code-block:: cpp

   struct Triangle {
     double a, b, c;
   };
   
   int main() {
     Triangle t1 = { 2, 2, 2 };
     cout << Triangle_perimeter(&t1) << endl; // prints 6

     Triangle_scale(&t1, 2); // Scale up by a factor of 2

     cout << Triangle_perimeter(&t1) << endl; // prints 12
   }

Which of the implementations of :code:`Triangle_scale()` below are correct? For each that is not correct, explain what's wrong with it.

.. shortanswer:: ch07_01_ex_triangle_scale_01

   If this implementation is correct, write "correct". Otherwise, explain what's wrong with it.

   .. code-block:: cpp

      // Implementation #1
      void Triangle_scale(const Triangle *tri, double s) {
        tri->a *= s;
        tri->b *= s;
        tri->c *= s;
      }

.. shortanswer:: ch07_01_ex_triangle_scale_02

   If this implementation is correct, write "correct". Otherwise, explain what's wrong with it.

   .. code-block:: cpp

      // Implementation #2
      void Triangle_scale(Triangle *tri, double s) {
        a *= s;
        b *= s;
        c *= s;
      }


.. shortanswer:: ch07_01_ex_triangle_scale_03

   If this implementation is correct, write "correct". Otherwise, explain what's wrong with it.

   .. code-block:: cpp

      // Implementation #3
      void Triangle_scale(double s) {
        t1.a *= s;
        t1.b *= s;
        t1.c *= s;
      }


.. shortanswer:: ch07_01_ex_triangle_scale_04

   If this implementation is correct, write "correct". Otherwise, explain what's wrong with it.

   .. code-block:: cpp

      // Implementation #4
      void Triangle_scale(Triangle *tri, double s) {
        tri->a *= s;
        tri->b *= s;
        tri->c *= s;
      }


.. shortanswer:: ch07_01_ex_triangle_scale_05

   If this implementation is correct, write "correct". Otherwise, explain what's wrong with it.

   .. code-block:: cpp

      // Implementation #5
      void Triangle_scale(Triangle tri, double s) {
        tri.a *= s;
        tri.b *= s;
        tri.c *= s;
      }

.. admonition:: Walkthrough

   .. reveal:: ch07_01_revealwt_triangle_scale
  
      .. code-block:: cpp
   
         // Implementation #1
         // **Incorrect** - there should not be a const on the Triangle
         // parameter because the function needs to modify its members
         void Triangle_scale(const Triangle *tri, double s) {
           tri->a *= s;
           tri->b *= s;
           tri->c *= s;
         }
   
      .. code-block:: cpp
   
         // Implementation #2
         // **Incorrect** - the member variables a, b, and c must be
         // accessed through the pointer tri, e.g. tri->a
         void Triangle_scale(Triangle *tri, double s) {
           a *= s;
           b *= s;
           c *= s;
         }
   
      .. code-block:: cpp
   
         // Implementation #3
         // **Incorrect** - t1 is not in scope for this function.
         // Instead, a pointer to the triangle to work with should
         // be passed in to the function (e.g. pointing at t1).
         void Triangle_scale(double s) {
           t1.a *= s;
           t1.b *= s;
           t1.c *= s;
         }
   
      .. code-block:: cpp
   
         // Implementation #4
         // **Correct**
         void Triangle_scale(Triangle *tri, double s) {
           tri->a *= s;
           tri->b *= s;
           tri->c *= s;
         }
   
      .. code-block:: cpp
   
         // Implementation #5
         // **Incorrect** - because the triangle is passed by
         // value, the scaling modification is made to a copy
         // and the original triangle remains unchanged
         void Triangle_scale(Triangle tri, double s) {
           tri.a *= s;
           tri.b *= s;
           tri.c *= s;
         }

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ADT Initialization and Representation Invariants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

.. TODO

.. youtube:: cvtrJPdnZsY
   :divid: ch07_02_vid_representation_invariants
   :height: 315
   :width: 560
   :align: center

|

.. TODO

**Exercise**


.. shortanswer:: ch07_02_ex_representation_invariants_01

   Brainstorm three representation invariants for the Matrix ADT from project 2. (At least one of these should involve the data array.)

   **Data Representation**

   .. code-block:: cpp

      const int MAX_MATRIX_WIDTH = 500;
      const int MAX_MATRIX_HEIGHT = 500;
      
      struct Matrix{
        int width;
        int height;
        int data[MAX_MATRIX_WIDTH *
                 MAX_MATRIX_HEIGHT];
      };


   **Representation Invariants**


.. shortanswer:: ch07_02_ex_representation_invariants_02

   Brainstorm three representation invariants for the Image ADT from project 2. (At least one of these should involve the channel members.)

   **Data Representation**

   .. code-block:: cpp

      const int MAX_INTENSITY = 255;

      struct Image {
        int width;
        int height;
        Matrix red_channel;
        Matrix green_channel;
        Matrix blue_channel;
      }

   **Representation Invariants**


In patricular, I recommend watching the walkthrough video here, since the solution is used to introduce some new concepts/examples.

.. admonition:: Walkthrough

   .. reveal:: ch07_02_revealwt_representation_invariants
  
      .. youtube:: Wl4e6fAJs-U
         :divid: ch07_02_wt_representation_invariants
         :height: 315
         :width: 560
         :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Interfaces and Implementations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

.. TODO

.. youtube:: GSjBT7UusRU
   :divid: ch07_03_vid_interfaces_and_implementations
   :height: 315
   :width: 560
   :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Composing ADTs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 4

.. TODO

.. youtube:: WO91KyakW-I
   :divid: ch07_04_vid_composing_adts
   :height: 315
   :width: 560
   :align: center

|

.. TODO


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Testing ADTs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 5

In EECS 280, we'll use a simple unit-testing framework for projects 2 and beyond. It provides some nice features that you don't get by using :code:`assert()` for tests. For example, the unit-testing framework can run all of your test cases and tell you which ones pass and which ones fail. A regular :code:`assert()` would just crash the program on the first failure, without giving you feedback about the rest of the tests.

You can find a full tutorial for the framework linked from the project 2 specification or our course website.

For now, let me give you a very brief introduction. The general idea is the same as writing tests with plain old :code:`assert()` - prepare some input, run an operation on it, and compare to expected output. But the syntax for using the framework is a bit different.

Here's a simple test that makes sure 2 + 2 = 4.

.. code-block:: cpp

   TEST(test_addition) {
      ASSERT_EQUAL(2 + 2, 4);
   }

You define each test using the :code:`TEST(...)` syntax, with the name you want to give to the test inside the parentheses. Then, put the testing code inside a set of curly braces, using one of several special :code:`ASSERT_` macros instead of a regular :code:`assert()`. The example above uses :code:`ASSERT_EQUAL`, but there are several options, including :code:`ASSERT_NOT_EQUAL`, :code:`ASSERT_TRUE` for boolean conditions, :code:`ASSERT_ALMOST_EQUAL` for comparing :code:`double` values, etc.

At the top of any test files, you'll want to make sure to :code:`#include` the framework, and you'll also need to add a call to :code:`TEST_MAIN()` at the bottom of the file. Don't worry about that for now, and see the unit test framework tutorial and project 2 specification/files for more details.

.. youtube:: pUla-V9vLGw
   :divid: ch07_05_vid_testing_adts
   :height: 315
   :width: 560
   :align: center

|


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Test-Driven Development
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 6

.. TODO

.. youtube:: KmuSmyR-3Bk
   :divid: ch07_06_vid_test_driven_development
   :height: 315
   :width: 560
   :align: center

|

.. TODO


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Testing with :code:`istringstream` and :code:`ostringstream`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 7

.. TODO

.. youtube:: 7EBHrVxDe0w
   :divid: ch07_07_vid_testing_with_stringstreams
   :height: 315
   :width: 560
   :align: center

|


**Exercise**

Let's add a :code:`Triangle_print` function for the :code:`Triangle` ADT.

.. code-block:: cpp

   struct Triangle {
     double a;
     double b;
     double c;
   };
   
   void Triangle_print(ostream &os, const Triangle * tri) {
     os << "Triangle:" << endl;
     os << " side a: " << tri->a << endl;
     os << " side b: " << tri->b << endl;
     os << " side c: " << tri->c << endl;
   }

For example, for a triangle with side lengths of 3, 4, and 5, the function would print:

.. code-block:: none

   Triangle:
    side a: 3
    side b: 4
    side c: 5

.. shortanswer:: ch07_07_ex_testing_with_stringstreams

   Write a test for :code:`Triangle_print` that creates a :code:`Triangle` with side lengths 3, 4, and 5 and uses a :code:`ostringstream` to verify the output produced by a call to :code:`Triangle_print` is exactly the same as the example output shown above.

.. admonition:: Walkthrough

   .. reveal:: ch07_07_revealwt_testing_with_stringstreams
  
      .. youtube:: uyGsgTXdosw
         :divid: ch07_07_wt_testing_with_stringstreams
         :height: 315
         :width: 560
         :align: center

|
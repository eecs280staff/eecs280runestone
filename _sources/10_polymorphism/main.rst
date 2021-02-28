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
      #ch10_02_ex_upcast_downcast input {
         width: 100% !important;
      }
   </style>

======================================================================
Polymorphism
======================================================================

Today's lecture is all about polymorphism, which makes our code more flexible and enables even just a single line of code to potentially do many different things in different situations.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Introduction to Polymorphism and Function Overloading
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

.. youtube:: cOpLOkKZlfE
   :divid: ch10_01_vid_function_overloading
   :height: 315
   :width: 560
   :align: center

|

----------------------------------------------------------------------
Operator Overloading
----------------------------------------------------------------------

We can also apply the concept of overloading to *operators* as well. For example, the :code:`+` operator means one thing when it's used on :code:`int`, something else when it's used on `string`, and yet another thing when it's used for pointer arithmetic!

In C++, we can also define what an operator should do if used on our own custom classes.

.. TODO

.. youtube:: 4ETw1p8brbc
   :divid: ch10_01_vid_operator_overloading
   :height: 315
   :width: 560
   :align: center

|

**Exercise**

Let's upgrade :code:`Pixel` from project 2 to a :code:`class` and add some overloaded operators:

- An overloaded :code:`<<` operator that prints a pixel in the format :code:`rgb(R,G,B)`
- An overloaded :code:`-` operator that computes the squared difference of two pixels

Note that both operators are implemented as non-member functions. Starter code (and a few more instructions in the comments) is available on `Lobster <https://lobster.eecs.umich.edu>`_ (L10.1_Pixel). Implement the operators so that the code in main works correctly.

.. shortanswer:: ch10_01_ex_pixel_operators

   Paste your finished code in the box below.


.. TODO walkthrough

.. admonition:: Walkthrough

   .. reveal:: ch10_01_revealwt_pixel_operators
  
      Here's a sample implementation:

      .. code-block:: cpp

         #include <iostream>
         using namespace std;
         
         class Pixel {
         public:
           const int r;
           const int g;
           const int b;
           
           Pixel(int r, int g, int b)
             : r(r), g(g), b(b) { }
           
         };
         
         int squared_difference(const Pixel &p1, const Pixel &p2);
         
         // TASK 1: Add an overloaded operator- that
         // returns the squared difference between two
         // pixels (you can just call squared_difference
         // in your implementation)
         
         int operator-(const Pixel &p1, const Pixel &p2) {
           return squared_difference(p1, p2);
         }
         
         // TASK 2: Add an overloaded operator<< that
         // prints out the pixel in this format:
         //   rgb({R},{G},{B})
         ostream &operator<<(ostream &os, const Pixel &p) {
           cout << "rgb(" << p.r << ", " << p.g
                << ", " << p.b << ")";
           return os;
         }
           
         int main() {
           Pixel p1(174, 129, 255);
           Pixel p2(166, 226, 46);
           
           cout << "p1: " << p1 << endl; // p1: rgb(174,129,255)
           cout << "p2: " << p2 << endl; // p2: rgb(166,226,46)
           
           cout << "sq diff: " << p2 - p1 << endl; // sq diff: 531
         }
         
         // From processing.cpp in P2 starter code
         int squared_difference(const Pixel &p1, const Pixel &p2) {
           int dr = p2.r - p1.r;
           int dg = p2.g - p1.g;
           int db = p2.b - p1.b;
           // Divide by 100 is to avoid possible overflows
           // later on in the algorithm.
           return (dr*dr + dg*dg + db*db) / 100;
         }

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Subtype Polymorphism
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

While function overloading allows us to conveniently reuse a name for many different functions with different signatures, it doesn't fundamentally change our programming - we could have just named the functions differently (e.g. :code:`max_double`, :code:`max_int`, :code`max_Card`, etc.).

Subtype polymorphism, on the other hand, is a game-changer. It works hand-in-hand with inheritance and essentially allows us to have a variable of a base type (e.g. :code:`Bird`) and then have that same variable potentially refer to any of the different derived types (e.g. :code:`Chicken`, :code:`Duck`, :code:`Eagle`, etc.), often changing which kind it refers to throughout the course of the program!

----------------------------------------------------------------------
Upcasts and Downcasts
----------------------------------------------------------------------

.. TODO

.. youtube:: wVdKXkTgrbg
   :divid: ch10_02_vid_upcasting_and_downcasting
   :height: 315
   :width: 560
   :align: center

|

.. TODO

**Exercise**

Consider the variables :code:`a`, :code:`b`, and :code:`c` below, and assume the :code:`Duck` and :code:`Chicken` classes are both derived from the :code:`Bird` base class.

.. code-block:: cpp

   int main() {
     Bird b("Bonnie");
     Chicken c("Carlos");
     Duck d("Dinesh");
   }

.. fillintheblank:: ch10_02_ex_upcast_downcast
   :casei:

   Consider each of the following code snippets. Each involves upcasts or downcasts, some with pointers and some with references (note that the rules for references are the same as for pointers - upcasts are safe but downcasts are not!). If the compiler would allow the code, write "ok". Otherwise, write "error" and a very brief explanation of the problem.
   
   .. list-table::
     :align: left
   
     * - .. code-block:: cpp
         
            Bird *bPtr = &b;
            Chicken *cPtr = bPtr;

   
       - |blank|
   
     * - .. code-block:: cpp
         
            Bird *bPtr = &b;
            bPtr = &d;
            bPtr = &c;

   
       - |blank|
   
     * - .. code-block:: cpp
         
            Bird &bRef = c;
            Chicken &cRef = bRef;

   
       - |blank|
   
     * - .. code-block:: cpp
         
            Bird &bRef = d;
   
       - |blank|
   
     
   - :.*error.*: Correct! (error - downcast from :code:`Bird*` to :code:`Chicken*`)
     :.*: Try again
   - :.*ok.*: Correct! (ok - as a :code:`Bird*`, :code:`b` can point to any of the objects)
     :.*: Try again
   - :.*error.*: Correct! (error - downcast from :code:`Bird&` to :code:`Chicken&`)
     :.*: Try again
   - :.*ok.*: Correct! (ok - a :code:`Bird&` is allowed to refer to a :code:`Duck`)
     :.*: Try again


----------------------------------------------------------------------
Virtual Functions
----------------------------------------------------------------------
.. TODO

We've now got a way (i.e. using pointers/references) to have a polymorphic variable that can potentially point to any type derived from a particular base, but there's still something missing...

.. youtube:: otALFLY4FWI
   :divid: ch10_02_vid_virtual_functions
   :height: 315
   :width: 560
   :align: center

|

**Exercise**

Shown below are a hierarchy of fruit-based classes and a main function that makes member function calls on a variety of fruit objects and pointers. Note that the :code:`f1()` function is non-virtual and the :code:`f2()` function is virtual.

.. list-table::
  :align: left

  * - .. code-block:: cpp
      
         class Fruit {
         public:
           int f1() { return 1; }
           virtual int f2() { return 2; }
         };
         
         class Citrus : public Fruit {
         public:
           int f1() { return 3; }
           int f2() override { return 4; }
         };
         
         class Lemon : public Citrus {
         public:
           int f1() { return 5; }
           int f2() override { return 6; }
         };

    - .. code-block:: cpp
         :linenos:
      
         int main() {
           Fruit fruit;
           Citrus citrus;
           Lemon lemon;
           Fruit *fPtr = &lemon;
           Citrus *cPtr = &citrus;
        
           int result = 0;
           cout << fruit.f2() << endl;
           cout << citrus.f1() << endl;
           cout << fPtr->f1() << endl;
           cout << fPtr->f2() << endl;
           cout << cPtr->f2() << endl;
           cPtr = &lemon;
           cout << cPtr->f1() << endl;
           cout << cPtr->f2() << endl;
         }

.. fillintheblank:: ch10_02_ex_virtual_functions
   :casei:

   What number is printed by each of the following lines in :code:`main()`?
   
   .. list-table::
     :align: left
   
     * - Line 9: |blank|
       - Line 10: |blank|
   
     * - Line 11: |blank|
       - Line 12: |blank|

     * - Line 13: |blank|
       - Line 15: |blank|
   
     * - Line 16: |blank|
       - ..
     
   - :2: Correct!
     :.*: Try again
   - :3: Correct!
     :.*: Try again
   - :1: Correct!
     :.*: Try again
   - :6: Correct!
     :.*: Try again
   - :4: Correct!
     :.*: Try again
   - :3: Correct!
     :.*: Try again
   - :6: Correct!
     :.*: Try again


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Polymorphism and Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

----------------------------------------------------------------------
Overriding
----------------------------------------------------------------------
.. TODO

.. youtube:: tuMG7pBZyYU
   :divid: ch10_03_vid_overriding
   :height: 315
   :width: 560
   :align: center

|

----------------------------------------------------------------------
Pure Virtual Functions and Abstract Classes
----------------------------------------------------------------------
.. TODO

.. youtube:: gzfM9pPR_DA
   :divid: ch10_03_vid_pure_virtual
   :height: 315
   :width: 560
   :align: center

|

----------------------------------------------------------------------
The Liskov Substitution Principle
----------------------------------------------------------------------
.. TODO

.. youtube:: tVmY2Mm37CM
   :divid: ch10_03_vid_liskov_substitution_principle
   :height: 315
   :width: 560
   :align: center

|

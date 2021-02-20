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
Inheritance
=======================================================================


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Miscellaneous Topic: Delegating Constructors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

.. TODO

.. youtube:: 3ZjP0D6J4K4
   :divid: ch09_01_vid_delegating_constructors
   :height: 315
   :width: 560
   :align: center

|

**Exercise**

Write another ADT to using a class to represent a :code:`Rectangle`. This will be similar to the :code:`Triangle` ADT we've been looking at so far, but to get the most out of this exercise, we suggest starting the code for :code:`Rectangle` from scratch and only using :code:`Triangle` as a reference where needed.

Your :code:`Rectangle` class should have:

- A default constructor that makes a :code:`1` x :code:`1` rectangle.
- A constructor that takes one side length, :code:`s`, and makes an :code:`s` x :code:`s` rectangle.
- A constructor that takes both a width and height.
- Member functions for computing the :code:`area` and :code:`perimeter`. (They take no parameters.)
- A :code:`scale` member function that takes one parameter and scales by that factor.

Make sure to:

- Think about which members should be :code:`public` vs. :code:`private`
- Use delegating constructors wherever possible
- Use :code:`const` wherever appropriate

.. shortanswer:: ch09_01_ex_rectangle

   Feel free to write your code in the box here or on `Lobster <https://lobster.eecs.umich.edu>`_.

.. admonition:: Walkthrough

   .. reveal:: ch09_01_revealwt_rectangle
  
      Here's an example implementation of :code:`Rectangle`:

      .. code-block:: 

         class Rectangle {
         private:
           double w, h;
           // INVARIANTS: w > 0 && h > 0
         
         public:
           Rectangle()
            : Rectangle(1, 1) { }
         
           Rectangle(double s)
            : Rectangle(s, s) { }
         
           Rectangle(double w_in, double h_in)
            : w(w_in), h(h_in) {
             check_invariants();
           }
         
           double area() const {
             return w * h;
           }
           
           double perimeter() const {
             return 2 * (w + h);
           }
         
           void scale(double s) {
             w *= s;
             h *= s;
             check_invariants();
           }
         
         private:
           void check_invariants() {
             assert(w > 0 && h > 0);
           }
         };

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Introduction to Inheritance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

.. TODO

.. youtube:: fMMKT-LlREA
   :divid: ch09_02_vid_inheritance_basics
   :height: 315
   :width: 560
   :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Inheritance With Birds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

.. TODO

.. youtube:: J75zMbO3eV0
   :divid: ch09_03_vid_inheritance_with_birds
   :height: 315
   :width: 560
   :align: center

|


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Inheritance Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 4

.. TODO

.. youtube:: 8jULLGraPN0
   :divid: ch09_04_vid_inheritance_details
   :height: 315
   :width: 560
   :align: center

|


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exercises
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 5

**Debugging Compile Errors with Inheritance**

.. mchoice:: ch09_05_ex_compile_errors
   :answer_a: Only chickens can cross roads.
   :answer_b: A base class constructor call is missing somewhere.
   :answer_c: A private member variable is accessed in the wrong place.
   :answer_d: One of the classes forgets to declare its base class.
   :answer_e: A const is missing somewhere.
   :correct: c

   Check out the file :file:`L09.2_Birds_compile` on `Lobster <https://lobster.eecs.umich.edu>`_. It has several **compile errors**. Take a look at the error messages for each and see if you can determine why the error is being given and what the conceptual mistake is that the programmer made. To give you some specifics to look for, here are some descriptions of errors. All except for one are in the given code. Which one of these is NOT an error in the given code?



**Debugging Runtime Errors with Inheritance**

.. mchoice:: ch09_05_ex_runtime_errors
   :answer_a: Bird names print out with memory junk.
   :answer_b: The Chicken constructor never calls the Bird constructor.
   :answer_c: Ducks end up with a random number of ducklings.
   :answer_d: Chickens should say bawwk, not tweet.
   :correct: b

   Check out the file :file:`L09.3_Birds_runtime` on `Lobster <https://lobster.eecs.umich.edu>`_. It has several **runtime errors**. Work through the code carefully in the simulation to see if you can identify the places where the program goes astray. What would you need to change in the code to fix the issues? To give you some specifics to look for, here are some descriptions of errors. All except for one are in the given code. Which one of these is NOT an error in the given code?







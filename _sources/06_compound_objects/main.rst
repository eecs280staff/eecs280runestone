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
Const and Compound Objects
=======================================================================

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :code:`const` Keyword
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

.. youtube:: qgb6usquy1M
   :divid: ch06_01_vid_intro_to_const
   :height: 315
   :width: 560
   :align: center

|


**Exercise**

.. fillintheblank:: ch06_01_ex_intro_to_const
   :casei:

   Provided the declarations below, which of the following assignments cause a compiler error? Keep in mind, the compiler will give an error for any line that either attempts to change a :code:`const` object or that would puts a :code:`const` object at risk of being changed in the future. (Write "ok" or "error".)

   .. code-block:: cpp
   
      int x = 3;
      int const * a = &x;
      int const b = x;
      int * const c = &x;
      int const &d = x;

   :code:`*a = 5;` |blank|
   
   :code:`b = 5;` |blank|
   
   :code:`*c = 5;` |blank|
   
   :code:`c = &x;` |blank|
   
   :code:`d = x;` |blank|
   
   :code:`a = &b;` |blank|
   
   :code:`x = 5;` |blank|

   - :error: Correct!
     :.*: Try again
   - :error: Correct!
     :.*: Try again
   - :ok: Correct!
     :.*: Try again
   - :error: Correct!
     :.*: Try again
   - :error: Correct!
     :.*: Try again
   - :ok: Correct!
     :.*: Try again
   - :ok: Correct!
     :.*: Try again

.. admonition:: Walkthrough

   .. reveal:: ch06_01_revealwt_intro_to_const
  
      .. youtube:: lBxmj_6kDPM
         :divid: ch06_01_wt_intro_to_const
         :height: 315
         :width: 560
         :align: center

|

-----------------------------------------------------------------------
:code:`const` Conversions
-----------------------------------------------------------------------

.. youtube:: TXvWYNNWoCI
   :divid: ch06_01_vid_const_conversions
   :height: 315
   :width: 560
   :align: center

|

For any function call, the compiler also has to make sure to protect :code:`const` objects that would be passed by reference or by pointer (i.e. and could be changed). The compiler's rule is that it will only allow a function to be called on a :code:`const` object if the parameters also include the necessary :code:`const` keywords to continue protecting that object. Essentially, only functions that "promise" not to change their parameters are allowed to be called on :code:`const` objects/variables.

.. fillintheblank:: ch06_01_ex_const_parameters
   :casei:

   Consider these function signatures and some variables declared in a :code:`main()` function.

   .. code-block:: cpp
   
      void strFunc1(const char *str);
      void strFunc2(char *str);
      void intFunc3(int a);

      int main() {
        const char strA[6] = "hello";
        char strB[6] = "apple";
        const int num = 3;
        
        // Consider adding function calls here.
      }

   Which of the following function calls would the compiler allow you to add to the end of :code:`main()`? (Write "ok" or "error".)

   :code:`strFunc1(strA);` |blank|
   
   :code:`strFunc1(strB);` |blank|
   
   :code:`strFunc2(strA);` |blank|
   
   :code:`strFunc2(strB);` |blank|
   
   :code:`intFunc3(num);` |blank|

   - :ok: Correct!
     :.*: Try again
   - :ok: Correct!
     :.*: Try again
   - :error: Correct!
     :.*: Try again
   - :ok: Correct!
     :.*: Try again
   - :ok: Correct!
     :.*: Try again

.. admonition:: Walkthrough

   .. reveal:: ch06_01_revealwt_const_parameters
  
      .. youtube:: W0mgKroO-_Y
         :divid: ch06_01_wt_const_parameters
         :height: 315
         :width: 560
         :align: center

|


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Intro to :code:`struct`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

.. youtube:: jY5AQytp2qI
   :divid: ch06_02_vid_intro_to_structs
   :height: 315
   :width: 560
   :align: center

|


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:code:`struct` Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

.. youtube:: GNupNtyHiBA
   :divid: ch06_03_vid_struct_functions
   :height: 315
   :width: 560
   :align: center

|


**Exercise**

Each of the following implementations of :code:`Person_birthday()` has a problem - some will not compile and others will not work as expected. Describe what the problem is and one way to fix it.

.. shortanswer:: ch06_03_ex_struct_functions_01

   .. code-block:: cpp
   
      // Version 1
      void Person_birthday(const Person *p) {
        ++p->age;
      }

.. shortanswer:: ch06_03_ex_struct_functions_02

   .. code-block:: cpp
   
      // Version 2
      void Person_birthday(Person p) {
        ++p.age;
      }


.. shortanswer:: ch06_03_ex_struct_functions_03

   .. code-block:: cpp
   
      // Version 3
      void Person_birthday(Person *p) {
        *(p.age)++;
      }


.. shortanswer:: ch06_03_ex_struct_functions_04

   .. code-block:: cpp
   
      // Version 4
      void Person_birthday(Person &p) {
        ++p->age;
      }




.. admonition:: Walkthrough

   .. reveal:: ch06_03_revealwt_struct_functions
  
      .. code-block:: cpp
   
         // Version 1
         // There shouldn't be a const in the parameter,
         // since this function IS intended to change
         // the Person it's called on.
         void Person_birthday(const Person *p) {
           ++p->age;
         }

      .. code-block:: cpp
      
         // Version 2
         // The pass-by-value parameter should be pass-by-reference,
         // otherwise, we can't adjust the original Person's age.
         void Person_birthday(Person p) {
           ++p.age;
         }

      .. code-block:: cpp
      
         // Version 3
         // The parentheses here are misplaced. They need to be
         // placed as (*p).age++, otherwise the compiler attempts
         // to do the ++ before the *, which won't work.
         void Person_birthday(Person *p) {
           *(p.age)++;
         }

      .. code-block:: cpp
      
         // Version 4
         // The -> operator can be used as a convenient shorthand
         // for member variable access through a pointer, but not
         // through a reference. For a reference, just use the .
         // operator directly like: ++p.age
         void Person_birthday(Person &p) {
           ++p->age;
         }

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Composing Data Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 4

.. youtube:: UalcvZP9gB4
   :divid: ch06_04_vid_composing_data_types
   :height: 315
   :width: 560
   :align: center

|
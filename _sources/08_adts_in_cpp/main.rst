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
Abstract Data Types in C++
=======================================================================

**Exercise**

Let's start today with a quick exercise that helps motivate the transition we'll make from C-Style to C++ Style ADTs.

Consider the code here that creates and uses a C-style ADT, specifically the :code:`Triangle` ADT from last time:

.. code-block:: cpp
   :linenos:

   int main() {
     Triangle t;
     Triangle_init(&t, 3, 4, 5);
     cout << Triangle_perimeter(&t) << endl;
     Triangle_scale(&t, 2);
     cout << t.a << endl;
   }

.. list-table::
  :align: left

  * - .. shortanswer:: ch08_00_ex_warm_up_01

         What would happen if the programmer forgot to write line 2?

    - .. shortanswer:: ch08_00_ex_warm_up_02
        
         What would happen if the programmer forgot to write line 3?

  * - .. shortanswer:: ch08_00_ex_warm_up_03
        
         Which parameter do all of the :code:`Triangle` functions have in common?

    - .. shortanswer:: ch08_00_ex_warm_up_04
         
         What's wrong with line 6? Does the compiler give us an error here?



.. admonition:: Walkthrough

   .. reveal:: ch08_00_revealwt_warm_up
  
      .. youtube:: HhA8b7MFySo
         :divid: ch08_00_wt_warm_up
         :height: 315
         :width: 560
         :align: center

|

As we move onward to the C++ style for ADTs, we'll use :code:`class` rather than :code:`struct` and also use built-in features of the language (i.e. things that C++ adds beyond C) to support good practices in a more robust way. In particular, a :code:`class` in C++ gives us:

1. | **Member Functions**
   | Both data (i.e. member variables) and behaviors (i.e. member functions) for an ADT are encapsulated as members of a :code:`class`.
2. | **Access Specifications**
   | Give :code:`public` access to an ADT's interface, e.g. functions we want other parts of our code to call while at the same time restricting internal details like raw member data to :code:`private` access.
3. | **Constructors**
   | Use constructors to ensure ADTs are *always* initialized (rather than having to separately call an init function).

We'll take a look at each of these in detail...

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Introduction to Classes and Member Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

.. youtube:: Ht1tMUc0OIs
   :divid: ch08_01_vid_member_functions
   :height: 315
   :width: 560
   :align: center

|

.. TODO

**Exercise**

Consider another member function, :code:`halfPerimeter()`, which is intended to return a value that is half of the triangle's perimeter. The (questionable) algorithm we choose for our implementation is to first shrink the triangle in half and then return its perimeter.

.. code-block:: cpp

   class Triangle {
   private:
     double a, b, c;
   
   public:
     double perimeter() const { ... }
     void scale(double s) { ... }
     void shrink(double s) { ... }
   
     double halfPerimeter() const {
       shrink(2);
       return perimeter();
     }
   };
   
   int main() {
     Triangle t1(3, 4, 5);
     cout << t1.halfPerimeter();
   }



.. list-table::
  :align: left

  * - .. shortanswer:: ch08_01_ex_half_perimeter_01

         The lines :code:`shrink(2);` and :code:`return perimeter();` call member functions, but what object are they called on?

    - .. shortanswer:: ch08_01_ex_half_perimeter_02
        
         The compiler says there's some kind of :code:`const` error with the :code:`shrink(2);` line. Will adding :code:`const` to the signature of :code:`shrink` fix the problem? (Hint: Nope. But why not?)

  * - .. shortanswer:: ch08_01_ex_half_perimeter_03
        
         Let's remove the :code:`const` on :code:`halfPerimeter()`. Now the code compiles. Are there any situations in which calling :code:`halfPerimeter()` wouldn't compile now?

    - .. shortanswer:: ch08_01_ex_half_perimeter_04
         
         The call to :code:`t1.halfPerimeter()` compiles now, but what's wrong with the code? What does this mean about using :code:`const` and the algorithm for :code:`halfPerimeter()`?

.. admonition:: Walkthrough

   .. reveal:: ch08_01_revealwt_half_perimeter
  
      .. youtube:: Bk3y7udPIgk
         :divid: ch08_01_wt_half_perimeter
         :height: 315
         :width: 560
         :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Member Accessibility and Constructors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

.. TODO

.. youtube:: 6zE7z1UNW_k
   :divid: ch08_02_vid_member_accessibility_and_constructors
   :height: 315
   :width: 560
   :align: center

|

.. TODO

**Exercise**

Consider the :code:`class` below, used as an ADT for a cup of coffee.

.. code-block:: cpp

   class Coffee {
   private:
     int creams;
     int sugars;
     bool isDecaf;
   
   public:
     // Regular coffee with creams/sugars
     Coffee(int creams, int sugars);
   
     // This ctor specifies regular/decaf
     Coffee(int creams, int sugars,
            bool isDecaf);
   
     // Adds one more cream to the coffee
     void addCream();
   
     // Adds one more sugar to the coffee
     void addSugar();
   
     // Prints a description of the coffee
     void print() const;
   };


.. fillintheblank:: ch08_02_ex_coffee
   :casei:

   Consider each of the following code snippets that we might write in a :code:`main` function to use the :code:`Coffee` class? If the compiler would allow the code, write "ok". Otherwise, write "error" and a very brief explanation of the problem.
   
   .. list-table::
     :align: left
   
     * - .. code-block:: cpp
         
            Coffee c1;
            c1.addCream();
            c1.print();
   
       - |blank|
   
     * - .. code-block:: cpp
         
            Coffee c2(2, 2);
            if (c2.isDecaf) {
              c2.print();
            }
   
       - |blank|
   
     * - .. code-block:: cpp
         
            Coffee c3(2, 2, false);
            c3.addCream();
            c3.print();
   
       - |blank|
   
     * - .. code-block:: cpp
         
            const Coffee c4(0, 0);
            c4.addCream();
            c4.print();
   
       - |blank|
   
     * - .. code-block:: cpp
         
            Coffee c5(true);
            c5.addSugar();
            c5.print();
   
       - |blank|

   - :.*error.*: Correct! (error - no default constructor)
     :.*: Try again
   - :.*error.*: Correct! (error - can't access private member :code:`isDecaf`)
     :.*: Try again
   - :ok: Correct!
     :.*: Try again
   - :.*error.*: Correct! (error - can't call :code:`.addCream()` on :code:`c4` because it is :code:`const`)
     :.*: Try again
   - :.*error.*: Correct! (error - no constructor taking a single :code:`bool`)
     :.*: Try again

.. admonition:: Walkthrough

   .. reveal:: ch08_02_revealwt_coffee
  
      .. youtube:: LzqPCH-gKik
         :divid: ch08_02_wt_coffee
         :height: 315
         :width: 560
         :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Composing C++ ADTs (Classes as Members)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

.. TODO

.. youtube:: pH8OPd_adQw
   :divid: ch08_03_vid_composing_cpp_adts
   :height: 315
   :width: 560
   :align: center

|

**Exercise**

Here again is the :code:`Professor` class from the video:

.. code-block:: cpp

   class Coffee {
   public: 
     Coffee(int creams, int sugars);
     Coffee(int creams, int sugars,
            bool isDecaf);
   };
   class Triangle {
   public:
     Triangle();
     Triangle(double side);
     Triangle(double a_in, double b_in,
              double c_in);
   };
   
   class Professor {
   private:
     string name;
     vector<string> students;
     Coffee favCoffee;
     Triangle favTriangle;
     ...
   };

Consider several possible constructors for the :code:`Professor` class. Which compile successfully? For those that don't compile, explain why (including which member is not initialized correctly).

.. list-table::
  :align: left

  * - .. shortanswer:: ch08_03_ex_classes_as_members_01

         .. code-block:: cpp

            Professor(const string &name)
             : name(name) { }

    - .. shortanswer:: ch08_03_ex_classes_as_members_02

         .. code-block:: cpp

            Professor(int creams, int sugars)
             : favCoffee(creams, sugars) { }

  * - .. shortanswer:: ch08_03_ex_classes_as_members_03

         .. code-block:: cpp

            Professor(const string &name,
                      const string &student)
             : name(name) {
              students.push_back(student);
            }


    - .. shortanswer:: ch08_03_ex_classes_as_members_04

         .. code-block:: cpp

            Professor(const Coffee &coffee)
             : name("Laura"),
              favCoffee(coffee),
              favTriangle(3, 5) { }

.. admonition:: Walkthrough

   .. reveal:: ch08_03_revealwt_classes_as_members
  
      .. youtube:: VSLPLyI3LHk
         :divid: ch08_03_wt_classes_as_members
         :height: 315
         :width: 560
         :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Default Initialization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 4

.. TODO

.. youtube:: R7orvELKSVQ
   :divid: ch08_04_vid_default_initialization
   :height: 315
   :width: 560
   :align: center

|

.. TODO


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Best Practices for ADTs with Classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 5

.. TODO

.. youtube:: TnnE_tRlkQ0
   :divid: ch08_05_vid_best_practices_for_classes
   :height: 315
   :width: 560
   :align: center

|

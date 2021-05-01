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
Structural Recursion
======================================================================

TODO

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Recursion on Lists
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

.. TODO

.. youtube:: TODO
   :divid: ch19_01_vid_recursion_on_lists
   :height: 315
   :width: 560
   :align: center

|
.. TODO

**Exercise**

Fill in the code for the :code:`grow()` function for :code:`UnsortedSet`:

.. code-block:: cpp

   template <typename T>
   class UnsortedSet {
   ...
   private:
     T *elts;
     int capacity;
     int elts_size;
    
     // Changes underlying representation to use a
     // dynamic array of 2 * capacity elements
     void grow() {
       // TODO: WRITE YOUR CODE HERE
   
   
   
   
     }
   };

Using the following algorithm:

1. Make a new array with twice as much capacity
2. Copy elements over
3. Update capacity
4. Destroy old array
5. Point elts to the new array

If you would like, you can find this exercise on `Lobster <https://lobster.eecs.umich.edu>`_ (:file:`L14.2_IntSet`).

.. shortanswer:: ch19_02_ex_grow

   Paste a copy of your implementation here.

.. admonition:: Walkthrough

   .. reveal:: ch19_02_revealwt_grow
  
      .. youtube:: TODO
         :divid: ch19_02_wt_grow
         :height: 315
         :width: 560
         :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Growable Containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

.. TODO

.. youtube:: TODO
   :divid: ch19_02_vid_growable_containers
   :height: 315
   :width: 560
   :align: center

|

.. TODO

**Exercise**

Fill in the code for the :code:`grow()` function for :code:`UnsortedSet`:

.. code-block:: cpp

   template <typename T>
   class UnsortedSet {
   ...
   private:
     T *elts;
     int capacity;
     int elts_size;
    
     // Changes underlying representation to use a
     // dynamic array of 2 * capacity elements
     void grow() {
       // TODO: WRITE YOUR CODE HERE
   
   
   
   
     }
   };

Using the following algorithm:

1. Make a new array with twice as much capacity
2. Copy elements over
3. Update capacity
4. Destroy old array
5. Point elts to the new array

If you would like, you can find this exercise on `Lobster <https://lobster.eecs.umich.edu>`_ (:file:`L14.2_IntSet`).

.. shortanswer:: ch19_02_ex_grow

   Paste a copy of your implementation here.

.. admonition:: Walkthrough

   .. reveal:: ch19_02_revealwt_grow
  
      .. youtube:: TODO
         :divid: ch19_02_wt_grow
         :height: 315
         :width: 560
         :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dynamic Resource Invariants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

.. TODO

.. youtube:: TODO
   :divid: ch19_03_vid_dynamic_resource_invaraints
   :height: 315
   :width: 560
   :align: center

|

.. TODO

**Exercise**

.. TODO: what can RAII do for us and what can it not?

.. fillintheblank:: ch19_03_ex_dynamic_resource_invariants
   :casei:

   Which of these functions leak memory? Write either "ok" or "memory leak". You should assume the constructors and destructor for :code:`UnsortedSet` are defined (correctly) as earlier.
   
   .. list-table::
     :align: left
   
     * - .. code-block:: cpp
         
            void func() {
              UnsortedSet<int> s1;
              s1.insert(2);
              s1.insert(3);
            }

   
       - |blank|
   
     * - .. code-block:: cpp
         
            void func() {
              UnsortedSet<int> *s3
                = new UnsortedSet<int>; 
              s3->insert(2);
              s3->insert(3);
            }

   
       - |blank|
   
     * - .. code-block:: cpp
         
            void func() {
              UnsortedSet<int*> s2;
              s2.insert(new int(2));
              s2.insert(new int(3));
            }


       - |blank|
   
     * - .. code-block:: cpp
         
            void func() {
              UnsortedSet<int> *s4
                = new UnsortedSet<int>; 
              s4->insert(2);
              s4->insert(3);
              delete s4;
            }

       - |blank|
     
   - :.*ok.*: Correct! (The set will internally store the inserted numbers in a dynamic array and its destructor will clean that up.)
     :.*: Try again
   - :.*memory leak.*: Correct! (The set's destructor can clean up its own internal memory when it is destroyed, but the problem is the set itself is never destroyed since it's created with :code:`new` but never freed with :code:`delete`.)
     :.*: Try again
   - :.*memory leak.*: Correct! (The set can clean up the dynamic array it uses to store the pointers to the :code:`2` and :code:`3`, but it only cleans up that array - it doesn't know to clean up the objects created with :code:`new` in :code:`main()`.)
     :.*: Try again
   - :.*ok.*: Correct! (The set itself is created on the heap and cleaned up with :code:`delete`, and the internal array it uses is also cleaned up when its destructor is called as a result of the :code:`delete`.)
     :.*: Try again

.. admonition:: Walkthrough

   .. reveal:: ch19_03_revealwt_dynamic_resource_invariants
  
      .. youtube:: TODO
         :divid: ch19_03_wt_dynamic_resource_invariants
         :height: 315
         :width: 560
         :align: center

|


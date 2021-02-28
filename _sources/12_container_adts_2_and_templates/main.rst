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
Container ADTs, Part 2 and Templates
======================================================================

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Time Complexity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

As we're asessing the fitness of a data structure for a given task, it's helpful to determine its **time complexity**, which quantifies how well it performs as the size of the data set we're working with scales up.

.. youtube:: sOC4Nizvh4I
   :divid: ch12_01_vid_time_complexity
   :height: 315
   :width: 560
   :align: center

|

**Exercise**

Determine whether each of the :code:`IntSet` functions below has :math:`O(1)` constant time complexity or :math:`O(n)` linear time complexity. Explain your reasoning. 

.. shortanswer:: ch12_01_ex_intset_time_complexity_01
   
   Does this function have :math:`O(1)` constant time complexity or :math:`O(n)` linear time complexity? Explain your reasoning.

   .. code-block:: cpp
      
      // IntSet constructor
      IntSet::IntSet()
       : elts_size(0) { }

.. shortanswer:: ch12_01_ex_intset_time_complexity_02
   
   Does this function have :math:`O(1)` constant time complexity or :math:`O(n)` linear time complexity. Explain your reasoning.

   .. code-block:: cpp
      
      IntSet::size() {
        return elts_size;
      }

.. shortanswer:: ch12_01_ex_intset_time_complexity_03
   
   Does this function have :math:`O(1)` constant time complexity or :math:`O(n)` linear time complexity. Explain your reasoning.

   .. code-block:: cpp
      
      int IntSet::indexOf(int v) const {
        for (int i = 0; i < elts_size; ++i) {
          if (elts[i] == v) {
        	   return i;
          }
        }
        return -1;
      }


.. shortanswer:: ch12_01_ex_intset_time_complexity_04
   
   Does this function have :math:`O(1)` constant time complexity or :math:`O(n)` linear time complexity. Explain your reasoning.

   .. code-block:: cpp
      
      bool IntSet::contains(int v) const {
        return indexOf(v) != -1;
      }


.. shortanswer:: ch12_01_ex_intset_time_complexity_05
   
   Does this function have :math:`O(1)` constant time complexity or :math:`O(n)` linear time complexity. Explain your reasoning.

   .. code-block:: cpp
      
      void IntSet::insert(int v) {
        assert(size() < ELTS_CAPACITY);
        if (contains(v)) {
          return;
        }
        elts[elts_size] = v;
        ++elts_size;
      }


.. shortanswer:: ch12_01_ex_intset_time_complexity_06
   
   Does this function have :math:`O(1)` constant time complexity or :math:`O(n)` linear time complexity. Explain your reasoning.

   .. code-block:: cpp
      
      void IntSet::remove(int v) {
        if (!contains(v)) {
          return;
        }
        elts[indexOf(v)] = elts[elts_size - 1];
        --elts_size;
      }


.. admonition:: Walkthrough

   .. reveal:: ch12_01_revealwt_time_complexity
  
      .. youtube:: LU8JMGBOLBM
         :divid: ch12_01_wt_time_complexity
         :height: 315
         :width: 560
         :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A Sorted :code:`IntSet`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

Let's make a key change to the fundamental strategy and data representation for our set - keeping all the elements in sorted order - and see if we can improve the performance of the data structure...

.. youtube:: -ljA2Ecmn74
   :divid: ch12_02_vid_member_non_member_operator_overloads
   :height: 315
   :width: 560
   :align: center

|

.. TODO

**Exercise**

Implement the :code:`insert()` member function for the :code:`SortedIntSet` class. If the given value is not already in the set, it should be inserted into the :code:`elts` array at the appropriate position to maintain the sorting invariant. Elements greater than the inserted value will need to be shifted to the right to create the space to insert the element. :code:`elts_size` should also increase by 1. However, if the value is already in the array, :code:`insert()` does nothing.

Starter code is available on `Lobster <https://lobster.eecs.umich.edu>`_ (:file:`L12.1_SortedIntSet`). The :code:`main()` function provided includes testing code to verify your implementation.

Use the strategy described in the video/text above to shift over enough elements to make room for the inserted value, and don't forget (like I did in the video!) to call :code:`contains()` as a helper function first to verify the number isn't already in the set (and just :code:`return;` early if it is already there).

.. shortanswer:: ch12_02_ex_sortedintset_insert

   Paste your code for the :code:`insert()` function in the box below.

.. admonition:: Walkthrough

   .. reveal:: ch12_02_revealwt_sortedintset_insert
  
      .. youtube:: TR4nYlsL74g
         :divid: ch12_02_wt_sortedintset_insert
         :height: 315
         :width: 560
         :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

.. TODO

.. youtube:: vQRn75mtf0w
   :divid: ch12_03_vid_templates
   :height: 315
   :width: 560
   :align: center

|

.. TODO

**Exercise**

Fill in the blanks to make the function work as intended (the :code:`main` function shows examples).

.. code-block:: cpp

   template <______________>
   void fillFromArray( ______________ set, ______________ arr, int n) {
     for (int i = 0; i < n; ++i) {
       ______________
     }
   }
   int main() {
     UnsortedSet<int> set1;
     int arr1[4] = { 1, 2, 3, 2 };
     fillFromArray(set1, arr1, 4); // set1 now contains 1, 2, 3
     UnsortedSet<char> set2;
     char arr2[3] = { 'a', 'b', 'a' };
     fillFromArray(set2, arr2, 3); // set2 now contains 'a', 'b'
   }


.. shortanswer:: ch12_03_ex_sortedintset_insert

   Record your answer below by copy/pasting the code above and filling in the blanks.

(Note that Lobster does not support user-defined templates, so unfortunately you won't be able to try out the code there.)

.. admonition:: Walkthrough

   .. reveal:: ch12_03_revealwt_sortedintset_insert
  
      .. youtube:: Fid4TlI19oI
         :divid: ch12_03_wt_sortedintset_insert
         :height: 315
         :width: 560
         :align: center

|
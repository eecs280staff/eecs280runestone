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
Iterators
======================================================================

Abstraction is quite likely the most powerful tool in programming. We've seen it applied as "procedural abstraction" (i.e. functions) and in "abstract data types" (i.e. classes), and we'll add another today - abstracting the process of "iteration" or "traversal" over a sequence or a container. To do this, we'll first define a common *interface* for iteration. But not all containers will naturally conform to this interface - traversing over an array looks a whole lot different than traversing over a linked list. So, we'll define custom objects called "iterators" for each different kind of sequence or container that act as the "tour guide" that conforms to our common interface but handles the container-specific details behind the scenes.

Ironically - the description above is quite abstract, and probably doesn't make much sense now. Come back and read it again after the chapter, once we've gone through some specific examples! Or, if you prefer a pun to irony - iterators are a subject where you have to iterate over the concept a few times before all the parts make sense together. Let's call this iteration 1. :)

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Warm Up Exercise
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 0

Let's take a look at two functions that traverse and print out different kinds of containers:

.. list-table::
   :align: left

   * - .. code-block:: cpp
      
         // Array traversal by pointer
         void print(int *begin, int size) {
           int *end = begin + size;
           for (int *p = begin; p != end; ++p) {
             cout << *p;
           }
         }

     - .. code-block:: cpp
      
         // Linked list traversal via next pointers
         void print (Node *begin) {

           for (Node *p = begin; p; p = p->next) {
              cout << p->datum;
           }
         }

.. fillintheblank:: ch17_00_warm_up
   :casei:

   Briefly answer the following questions. (A word or short phrase is sufficient!)
   
   .. list-table::
     :align: left
   
     * - 
       - Array Traversal
       - Linked List
   
     * - Which variable tracks the current position in the container?
       - |blank|
       - |blank|
   
     * - How is it initialized?
       - |blank|
       - |blank|
   
     * - How do we move it to the next item in the container? 
       - |blank|
       - |blank|
   
     * - How do we know we have reached the last item in the container?
       - |blank|
       - |blank|
   
     * - How do we access the value of the current item in the container?
       - |blank|
       - |blank|

   - :.*: Complete
   - :.*: Complete
   - :.*: Complete
   - :.*: Complete
   - :.*: Complete
   - :.*: Complete
   - :.*: Complete
   - :.*: Complete
   - :.*: Complete
   - :.*: Complete

.. TODO walkthrough

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Iterators: The Big Idea
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

It would be nicer if we could write a **single** version of :code:`print()` that could operate on both arrays and linked lists (and vectors and sets and other containers!). As we alluded to above - we'll need a common abstraction for iteration, which can be used by :code:`print()` regardless of the container type. As a preview, here's what that function will look like:

.. code-block:: cpp

   template <typename IterType>
   void print(IterType begin, IterType end) {
     for (IterType it = begin; it != end; ++it) {
       cout << *it;
     }
   }

What is this doing? At a high level, we've got a function template that can be flexible to accommodate different :code:`IterType` types. When used with a specific container, :code:`IterType` will match to the type of **iterator** that container provides. Recall that an iterator is supposed to act like a "tour guide" for a container. With that in mind, we can roughly interpret the rest of the code - we've peforming different operations on the iterator, expecting it to take us through the container's elements. :code:`*it` should give us access to the current element. :code:`++it` should move the iterator onward to the next one.

The last piece of the puzzle is how we get the :code:`begin` and :code:`end` iterators to pass into the function. Basically, we ask the container to provide them for us by calling member functions. Here's an example using STL containers, which define these and iterator types, combined with the :code:`print()` function defined above:

.. code-block:: cpp

   int main() {
     std::vector<int> vec;
     std::list<double> list;
     std::set<string> set;
 
     // Assume some elements are added to the containers above.
     // The code below will then print out the elements for each!
     print(vec.begin(), vec.end());
     print(list.begin(), list.end());
     print(set.begin(), set.end());
   }

We could call this iteration 2! We presume that containers have objects called **iterators** that we can get by calling :code:`.begin()` and :code:`.end()` functions, and that those iterators will support operations like :code:`*`, :code:`++`, etc. to take us on a tour through the element's containers.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Building an Iterator for a Linked List
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

Let's fill in some more details and work through an example of actually creating an iterator for our linked list class...

.. youtube:: SJQhjiOtDq0
   :divid: ch17_02_vid_linked_list_iterator
   :height: 315
   :width: 560
   :align: center

|

We'll call that iteration 3! Now we've seen the inside implementation details of how we build an iterator for a linked list, the magic behind the abstraction of the iterator interface.

**Exercise**

As we finish building the :code:`Iterator` class, a reasonable question is whether we need to define custom versions of the "Big Three" functions (i.e. copy constructor, assignment operator, and destructor). After all, the iterator does contain a pointer to a dynamically allocated :code:`Node`, which is one of the "hints" that a class *might* need custom Big Three implementations.

Let's work through a couple exercises to assess the situation. First, let's think about shallow vs. deep copies. Consider the code below, and draw out a memory diagram, tracing through the code to the final state of memory (assuming the built-in implementation of the copy constructor for :code:`Iterator`, which will use a shallow copy).

.. code-block:: cpp

   int main() {
     List<int> list;
     list.push_back(1);
     list.push_back(2);
     list.push_back(3);

     List<int>::Iterator it1 = list.begin();
     ++it1;

     List<int>::Iterator it2 = it1;
     ++it2;

     // Draw memory at this point
   }

.. shortanswer:: ch17_02_ex_iterator_big_three_01

   Consider your diagram...does everything look as it should, even though the copy of the iterator did not also result in a deep copy of the node it was pointing to?

We can also consider whether :code:`Iterator` needs a custom implementation of the destructor, perhaps something like shown below:

.. code-block:: cpp

   class Iterator {
     friend class List;
   public:
     // Public default constructor
     Iterator()
      : node_ptr(nullptr) { }

     // Potential custom destructor - should we add this???
     ~Iterator() {
       delete node_ptr;
     }
   private:
     // private constructor
     Iterator(Node *np) : node_ptr(np) { }

     // Member variable - pointer to the current node
     Node *node_ptr;
   };

.. shortanswer:: ch17_02_ex_iterator_big_three_02

   Consider the same :code:`main()` program from earlier, referring back to your diagram. If we were to add a custom destructor that also deletes the :code:`Node` the iterator is pointing to, what would happen at the end of this main function when destructors run for :code:`it1`, :code:`it2`, and :code:`list`? (i.e. Would we get any memory errors? If so, what kind?)

.. admonition:: Walkthrough

   .. reveal:: ch17_02_revealwt_iterator_big_three
  
      .. youtube:: 7Rz6HG0Gzyc
         :divid: ch17_02_wt_iterator_big_three
         :height: 315
         :width: 560
         :align: center

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Generalizable Function Templates Using Iterators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

Finally, we'll take a look back at our original goal - write flexible functions that treat iteration via iterators as an abstraction so that they aren't fixed to work with only a single kind of container.

.. youtube:: nhJD-ilWD-o
   :divid: ch17_03_vid_iterator_function_templates
   :height: 315
   :width: 560
   :align: center

|


**Exercise**

Consider each of several potential implementations of a generic :code:`length()` function that takes in begin/end iterators and computes the length of the sequence they point to (using traversal by iterator and counting the number of steps). We would like the :code:`length()` function to be useable with any container that supports an iterator interface. So, we could use it like this:

.. code-block:: cpp

   int main() {
     List<int> list; // assume it's filled with some numbers
     cout << length(list.begin(), list.end()) << endl;
   }

Or like this!

.. code-block:: cpp

   int main() {
     std::vector<Card> cards; // assume it's filled with some cards
     cout << length(cards.begin(), cards.end()) << endl;
   }

Determine which of the following potential implementations of :code:`length()` are correct. Write "correct" or "incorrect". If they are not correct, additionally describe what's wrong with them.

.. shortanswer:: ch17_03_ex_iterator_length_01

   .. code-block:: cpp

      template <typename Iter_type>
      int length(Iter_type begin, Iter_type end) {
        int count = 0;
        List<int>::iterator it = begin;
        while(it != end) {
          ++count;
          ++it;
        }
        return count;
      }

.. shortanswer:: ch17_03_ex_iterator_length_02

   .. code-block:: cpp

      template <typename Iter_type>
      int length(Iter_type begin, Iter_type end) {
        int count = 0;
        for(Iter_type it = begin; it < end; ++it) {
          ++count;
        }
        return count;
      }

.. shortanswer:: ch17_03_ex_iterator_length_03

   .. code-block:: cpp

      template <typename Iter_type>
      int length(Iter_type begin, Iter_type end) {
        int count = 0;
        while(begin != end) {
          ++count;
          ++begin;
        }
        return count;
      }

.. shortanswer:: ch17_03_ex_iterator_length_04

   .. code-block:: cpp

      template <typename Iter_type>
      int length(Iter_type begin, Iter_type end) {
        return end - begin;
      }


.. admonition:: Walkthrough

   .. reveal:: ch17_03_revealwt_iterator_length
  
      .. youtube:: BWCJpKM-fD8
         :divid: ch17_03_wt_iterator_length
         :height: 315
         :width: 560
         :align: center

|


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Iterator Validity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 4

One last thing... Iterators are kind of like "fancy pointers", and we've got the concept of a "dangling pointer" (a pointer to an object that's no longer safe to use). We have a parallel concept for iterators, referred to as an "invalid", "invalidated", or "dangling" iterator.

.. youtube:: BLqkNZEMjEs
   :divid: ch17_04_vid_iterator_validity
   :height: 315
   :width: 560
   :align: center

|
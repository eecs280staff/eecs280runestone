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

===========================================================================================
Pointers
===========================================================================================

The fundamental idea of pointers is that we might like to work with **addresses** of objects in our programs as well as just their **values/data**. Why? Pretty much the same reason we use addresses anywhere else - sometimes we need to work **indirectly**. For example, in the "real world", an address book refers to the places that people live, but it doesn't literally contain those places! (That wouldn't even make sense.) Likewise, in a program we might want several different parts of our code to refer to the same data structure, but we don't want them all to literally have a local copy of that data. It would be better to know the address of the data and just go look it up when we need to.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Addresses and Pointers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

First, let's take a look at how we can find out the address of variables/objects in our program using the :code:`&` operator.

.. youtube:: e364_zq4nxU
   :divid: ch03_01_vid_addresses_and_pointers
   :height: 315
   :width: 560
   :align: center

|

**Exercise**

Consider the program below and answer a few questions.

.. code-block:: cpp

   int main() {
     int x = 4;
     int y = 7;
     double z = 1.5;

     int *ptr1 = &x;
     int *ptr2 = &y;
   }

.. admonition:: Pro Tip

   You can open this chapter of Runestone in another window or tab to view the code/questions side-by-side without having to scroll up and down.

.. shortanswer:: ch03_01_addresses_and_pointers_01

   If you added the line :code:`cout << ptr2 << endl;` to the end of :code:`main`, what would be printed?

.. shortanswer:: ch03_01_addresses_and_pointers_02

   Suppose you added the line :code:`ptr1 = &ptr2;` to the end of :code:`main`. Would the compiler allow this? If so, what would the effect of that line be?

.. shortanswer:: ch03_01_addresses_and_pointers_03

   Suppose you added the line :code:`ptr1 = ptr2;` to the end of :code:`main`. Would the compiler allow this? If so, what would the effect of that line be?

.. shortanswer:: ch03_01_addresses_and_pointers_04

   Would it be possible to change the value of :code:`z` using either of the two pointers declared in :code:`main`? If so, how? If not, why not?


.. admonition:: Walkthrough

   .. reveal:: ch03_01_revealwt_addresses_and_pointers
  
      .. youtube:: 1isxB18kdlY
         :divid: ch03_01_wt_addresses_and_pointers
         :height: 315
         :width: 560
         :align: center

|




^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Using Pointers and The Dereference Operator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

Now that we've got addresses, let's take a look at how to use those addresses to get back to the original object. This is called "dereferencing" a pointer - if we imagine a pointer as an arrow pointing to an object, dereferencing is just following the arrow.

.. youtube:: Kpotc1G6lkQ
   :divid: ch03_02_vid_using_pointers
   :height: 315
   :width: 560
   :align: center

|

A reminder on terminology: when working with pointers and addresses instead of objects themselves, we can say we are working with those objects *indirectly* or using *indirection*.

- The :code:`&` operator takes the address of an object, adding a layer of indirection to obtain a pointer.
- The :code:`*` operator peels away a layer of indirection, following a pointer to the object it points to.

**Exercise**

Trace this code and draw a memory diagram as you go. Once you're finished, use your diagram to answer the question below. (Note the assumed addresses in a comment for each variable.)

.. admonition:: Pro Tip

   Try to get lots of practice drawing memory diagrams now! You'll thank yourself later on some of the more complex projects, and it's also a great way to prep for exams.

.. code-block:: cpp

   int main() {
     int x = 1;      // Assume x is allocated at address 0x2710
     int y = 1;      // Assume x is allocated at address 0x2714
     int *ptr = &x;  // Assume x is allocated at address 0x2718
     
     x = 2;
     *ptr = 3;
     
     ptr = &y;
     *ptr = 4;
   
     // Your diagram should represent memory at this point
   
     cout << "x = " << x << endl;
     cout << "y = " << y << endl;
   
     cout << "ptr = " << ptr << endl;
     cout << "*ptr = " << *ptr << endl;
    
     cout << "&x = " << &x << endl;
     cout << "&ptr = " << &ptr << endl;
     
     cout << "*&x = " << *&x << endl;
     cout << "&*ptr = " << &*ptr << endl;
   }


.. fillintheblank:: ch03_02_using_pointers

   What values are printed for each of the expressions sent to :code:`cout` at the end of the program?

   |blank| :code:`x`
   
   |blank| :code:`y`
   
   |blank| :code:`ptr`
   
   |blank| :code:`*ptr`
   
   |blank| :code:`&x`
   
   |blank| :code:`&ptr`
   
   |blank| :code:`*&z`
   
   |blank| :code:`&*ptr`

   - :3: Correct!
     :.*: Try again
   - :4: Correct!
     :.*: Try again
   - :0x2714: Correct!
     :.*: Try again
   - :4: Correct!
     :.*: Try again
   - :0x2710: Correct!
     :.*: Try again
   - :0x2718: Correct!
     :.*: Try again
   - :3: Correct!
     :.*: Try again
   - :0x2714: Correct!
     :.*: Try again

To check your work, find the file :file:`L03.1_pointers` in the EECS 280 code on `Lobster <https://lobster.eecs.umich.edu>`_. You can use the simulation to check your diagram and to see the correct output for each expression. If you'd like, you can also make a personal copy of the code and change it around to answer any "what-if" questions or get more practice predicting the program's behavior.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Null and Uninitialized Pointers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

A regular pointer contains the address of some other object in your program, and will lead you to that object when you dereference it. But there are a few exceptional cases we should consider:

.. youtube:: s7BuhZjdYSY
   :divid: ch03_03_vid_null_and_uninitialized_pointers
   :height: 315
   :width: 560
   :align: center

|

To recap:

- **Uninitialized pointers**: Just like with any other (primitive) variable, if you don't initialize a pointer, it's value is determined by memory junk. That means it's pointing randomly off into space.
- **Null pointers**: Sometimes we want to definitively say "this pointer isn't pointing to anything right now", and the way to do that is point it at address :code:`0`.

Some more examples:

.. code-block:: cpp

   int x = 3;

   int *ptr1 = &x; // Initialized with the address of x, this pointer points to x
   *ptr1 = 10;     // Follows ptr1 to x and sets x to 10

   int *ptr2;      // Uninitialized pointer, points at some random address (eeeewww)
   *ptr2 = 10;     // Follows ptr2 off to some random part of memory and slaps down a 10
                   // causing undefined behavior depending on how important that memory was

   int *ptr2 = nullptr; // Null pointer, "not pointing at anything right now"
   *ptr2 = 10;          // Tries to write a 10 to address 0 in memory, which will almost
                        // certainly crash (easier to debug than undefined behavior though!)

Something else to consider - how do we safely use null pointers? Basically, if a pointer in our program might be null (i.e. sometimes it might not be pointing at anything), we'll often need to check for that in our control flow logic. For example:

.. code-block:: cpp

   // Assume we have a pointer called ptr that might be null

   if (ptr != nullptr) {
     // If we get in here, it's safe to dereference and do something with *ptr
   }

There's also a cute way to check whether a pointer is null - just throw the pointer itself in the :code:`if` condition. This works because the :code:`if` will try to conver it to a :code:`bool`, and it just so happens that non-null pointers will convert to :code:`true` and null pointers will convert to :code:`false`. (Kind of like the way nonzero numbers convert to :code:`true` and :code:`0` converts to :code:`false`.)

.. code-block:: cpp

   // Assume we have a pointer called ptr that might be null

   if (ptr) { // How cute! :D
     // If we get in here, it's safe to dereference and do something with *ptr
     // That's because ptr would only turn into a true if it wasn't null
   }

**Exercise**

For each of the following code snippets, briefly describe what the **last** line of code does. (For example, "sets the value of a to 3" or "dereferences a null pointer - program crashes".)

.. shortanswer:: ch03_03_null_and_uninitialized_pointers_01

   .. code-block:: cpp

      int main() {
        int a = 2;
        int *ptr1 = nullptr;
        int *ptr2;

        *ptr1 = 4; // What does this line do?
      }

.. shortanswer:: ch03_03_null_and_uninitialized_pointers_02

   .. code-block:: cpp

      int main() {
        int a = 2;
        int *ptr1 = nullptr;
        int *ptr2;

        ++*ptr2; // What does this line do?
      }

.. shortanswer:: ch03_03_null_and_uninitialized_pointers_03

   .. code-block:: cpp

      int main() {
        int a = 2;
        int *ptr1 = nullptr;
        int *ptr2;

        *ptr2 = a; // What does this line do?
      }

.. shortanswer:: ch03_03_null_and_uninitialized_pointers_04

   .. code-block:: cpp

      int main() {
        int a = 2;
        int *ptr1 = nullptr;
        int *ptr2;

        ptr2 = &a; // What does this line do?
      }


.. admonition:: Walkthrough

   .. reveal:: ch03_03_revealwt_null_and_uninitialized_pointers
  
      .. youtube:: 3PDShlC7wr4
         :divid: ch03_03_wt_null_and_uninitialized_pointers
         :height: 315
         :width: 560
         :align: center

|


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Pass-by-Pointer Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 4

We can achieve an effect similar to pass-by-reference by using a pointer instead. Here's the basic idea - just like with pass-by-reference, we want to work with the original object (e.g. in a :code:`main` function) without making a copy when we pass it in as a parameter. So, instead of passing the original object, we pass its address as a pointer parameter. That parameter is technically copied, but who cares! A copy of an address will still get you back to the original location.

Check out this video to see it in action:

.. youtube:: T0SN1PxaIVk
   :divid: ch03_04_vid_pass_by_pointer
   :height: 315
   :width: 560
   :align: center

|

**Exercise**

Load up the :code:`L03.3_swap-by-pointer` exercise on `Lobster <https://lobster.eecs.umich.edu>`_. The code contains a broken :code:`swap` function that doesn't actually do anything. Fix it by modifying the function to use pass-by-pointer, so that you can swap the original objects through pointer parameters. Once you're done, the values of the original variables in main should be swapped correctly! (Note that Lobster will show a completed checkpoint once you've got the right output, and may also try to give you some hints along the way if you run into any bugs.)

.. shortanswer:: ch03_04_ex_pass_by_pointer

   Paste your finished code for the exercise here.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Pointer Mischief
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 5

Check out the code in the :file:`L03.4_pointer_mischief` exercise on `Lobster <https://lobster.eecs.umich.edu>`_. (The code is also included below.) The code uses a dubious function to get the address of the variable :code:`a`, calls a random function to print :code:`42` (this is definitely not a trick :D ), and then prints out :code:`a` through the address we got earlier. But all is not as it seems! What happens? Write your explanation in the box below. (Don't worry if you're not sure what happens - take some time and give it your best guess - I'll explain what's going in in the video farther below.)

.. code-block:: cpp

   #include <iostream>
   using namespace std;
   
   int * getAddress(int x) {
     return &x;  // It's a trap!
   }
   
   void printAnInt(int someInt) {
     cout << someInt << endl;
   }
   
   int main() {
     int a = 3;
     int *ptr = getAddress(a);
     printAnInt(42);
     cout << *ptr << endl;
   }

.. shortanswer:: ch03_05_ex_pointer_mischief

   Why doesn't the code work as expected? What happens instead?

Once you're finished, go ahead and watch this video for a debrief on the exercise:

.. youtube:: v6ovLP_EOgM
   :divid: ch03_05_vid_pointer_mischief
   :height: 315
   :width: 560
   :align: center

|
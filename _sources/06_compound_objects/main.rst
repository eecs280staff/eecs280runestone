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

=======================================================================
Strings, Streams, and I/O
=======================================================================

This lecture is all about strings, streams, and input/output (I/O). Fundamentally, these all involve processing data represented as sequences of characters, perhaps the text of a book, an encrypted message, or even the source code for one of our programs as it's about to be digested by the compiler!

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C-Style Strings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 1

We'll start with the most fundamental representation for a string: an **array of characters**. We'll call this a C-style string (or cstring for short), because this is the predominant form for strings in the original C language.

There's one additional trick to C-style strings - instead of keeping track of the length of the array of characters separately (e.g. in an int variable that we pass along to any array functions), we instead mark the end of the string data in the array with a special character called a **sentinel**. Any code processing the string keeps an eye out for the sentiel value to know when to stop.


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

Here's a brief introduction:

.. youtube:: 0z_SYTVQnA0
   :divid: ch05_01_vid_intro_to_cstrings
   :height: 315
   :width: 560
   :align: center

|

To recap:

- A cstring is a sequence of characters, living in an array, terminated by a null character (:code:`\0`).
- The null character acts as a sentinel, so that code processing the cstring knows where to stop.
- When initializing a cstring from a string literal, the compiler automatically adds the null character for us.
- It's customary to work with cstrings via traversal by pointer.

There are three main options for creating a cstring:

- | :code:`const char *welcomeMsg = "Welcome to EECS 280!";`
  | Point at a string literal. We can use it, but we don't plan to modify the contents (and the compiler enforces this with the const).
- | :code:`char hexColor[] = "00274C";`
  | Create a local array to contain a *copy* of the given cstring. The example here has space for 7 characters (6 regular plus the null character). We can modify the contents however we want, but the size is fixed.
- | :code:`char filename[1024];`
  | Create a "buffer" that may hold many different cstrings (one at a time). The array contains lots of space, because some strings might be longer than others. The placement of the null character lets us know the end of the current cstring living in the buffer. For example, we might want to iterate through a list of file names and process them.

-----------------------------------------------------------------------
Processing C-style Strings
-----------------------------------------------------------------------

For almost any operation we would like to perform on a cstring, the basic idea is that we set up a traversal by pointer loop that iterates until it happens upon the null character. As the pointer walks through the string, we perform whatever data processing or modifications we need by dereferencing the pointer to work with individual characters.

It's generally a good idea to wrap up this kind of work in a function that can be reused wherever we need it. Let's take a look at how this plays out in code with a few examples.

.. youtube:: lhoW6iwCl9M
   :divid: ch05_02_vid_processing_cstrings
   :height: 315
   :width: 560
   :align: center

|

**Exercise**

Write the function :code:`strcpy` described at the end of the video above.

This exercise is available on `Lobster <https://lobster.eecs.umich.edu>`_ as :code:`L05.2_strcpy`.

.. shortanswer:: ch05_01_ex_strcpy

   Paste your finished code for the exercise here.

   

.. admonition:: Walkthrough

   .. reveal:: ch05_01_revealwt_strcpy
  
      .. youtube:: KOS5Oe2FvO0
         :divid: ch05_01_wt_strcpy
         :height: 315
         :width: 560
         :align: center

|

-----------------------------------------------------------------------
The :code:`<cstring>` Library
-----------------------------------------------------------------------

Because cstrings are just built on fundamental types like arrays, :code:`char`, and pointers, you don't need to include any libraries to use them. However, many common operations for cstrings are available as functions in the :code:`<cstring>` Library, which you can :code:`#include` at the top of your files if you need them. You can find documentation for these in a number of places, but online resources like `http://www.cplusplus.com/reference/cstring/ <http://www.cplusplus.com/reference/cstring/>`_ are generally a good place to start.

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C++ Strings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

You may have worked with the C++ :code:`string` type in your intro programming course or other previous experience. If not, or if you're primarily familiar with strings from a different language, we encourage you to check out one of several tutorials or documentation resources available online. (If you didn't take one of the intro courses here at UM, please also feel free to reach out and I can connect you with the material on :code:`string` from one of those courses.)

In general, you should prefer to use C++ :code:`string` where you can. It's an easier datatype to work with than a cstring and supports intuitive string operators like :code:`==`, :code:`<`, :code:`+`, :code:`=`, etc. Basically it works well and doesn't have some of the unpredictable quirks. (Contrast this to the fact that by its nature as an array of characters, cstring variables won't work with any of the operators just mentioned.)

Why are we learning about cstrings if they're so...un-useful?

- Sometimes you need to use them, for example, command-line arguments (see below) rely on cstrings.
- It's an interesting look into a low-level representation of a string, very much similar to the way a C++ :code:`string` is actually implemented internally.
- The notion of a sentinel-terminated sequence generalizes and will show up elsewhere.
- More practice with pointers! Yay. :)

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File Input and Output Streams
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

.. youtube:: CLW-DIZ5AOw
   :divid: ch05_03_vid_input_and_output_streams
   :height: 315
   :width: 560
   :align: center

|

For reference, here is the final example from the video:

.. code-block:: cpp

   #include <iostream>
   #include <string>
   #include <fstream>
   
   using namespace std;
   
   int main() {
   
     string inName = "in.txt";
     string outName = "out.txt";
   
     cout << "Copying from " << inName << " to " << outName << endl;
   
     string wordToRemove;
     cout << "What word would you like to remove? ";
     cin >> wordToRemove;
   
     ifstream fin(inName);
     ofstream fout(outName);
     if ( !fin.is_open() ) {
       cout << "Unable to open " << inName << endl;
       return 1;
     }
     
     if ( !fout.is_open() ) {
       cout << "Unable to open " << outName << endl;
       return 1;
     }
   
     string word;
     while (fin >> word) {
       if (word != wordToRemove) { fout << word << " "; }
       else { fout << "*****" << " "; }
     }
   
     fin.close();
     fout.close();
   }

Here's another example, which also showcases the :code:`stoi()` function, which converts from a :code:`string` to the :code:`int` value that it represents. In this case, we want to read a sequence of numbers from the user via :code:`cin` and add them together. The user may enter as many numbers as they like and then types :code:`"done"` to indicate they are finished. Because we need to accommodate both numbers and a string, we use the most general type - :code:`string` and then convert to an :code:`int` where appropriate using :code:`stoi`.

.. code-block:: cpp

   #include <iostream>
   #include <string>
   
   using namespace std;
   
   int main() {
     int sum = 0;
     string word;
     while (cin >> word && word != "done") {
       sum += stoi(word);
     }
     cout << "sum is " << sum << endl;
   }

This example is also available on `Lobster <https://lobster.eecs.umich.edu>`_ as :file:`L05.3_cin_sum`

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Command Line Arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 4

.. youtube:: mXJA13Go9qk
   :divid: ch05_04_vid_command_line_arguments
   :height: 315
   :width: 560
   :align: center

|

To get an argument out of :code:`argv`, you generally just use indexing, e.g. :code:`argv[x]` where :code:`x` is the index of the argument you want. Remember that the argument at index :code:`0` is just the name of the executable, so your "real" arguments will start indexed at :code:`1`.

Once you have an argument, there are three things you might want to do with it:

1. | :code:`string wordToRemove = argv[1];`
   | Immediately convert it to a C++ string (e.g. by storing in a :code:`string` variable). C++ strings are MUCH easier to work with and support convenient operators like :code:`==`.
2. | :code:`ifstream fin(argv[2]);`
   | :code:`ofstream fout(argv[3]);`
   | Use it directly somewhere that a cstring is readily accepted. For example, an :code:`ifstream` or :code:`ofstream` can be constructed from a cstring with the name of an input/output file.
3. | :code:`int redactLength = atoi(argv[4]);`
   | For arguments you want to interpret as a number (rather than a "string of digits"), convert it to an :code:`int` using :code:`atoi()` or to a :code:`double` using :code:`atof()`. (Or, if you already converted to a C++ :code:`string`, use :code:`stoi()` or :code:`stod()`.)

If you like, you can always start with option #1. It's almost never a bad idea to go ahead and switch over to a C++ :code:`string` where you can.

Again, for reference, here's the final code for the redact example, modified to use command line arguments as shown in the video.

.. code-block:: cpp

   #include <iostream>
   #include <string>
   #include <fstream>
   
   using namespace std;
   
   int main(int argc, char *argv[]) {
   
     // Usage message shown if the user runs with incorrect command line args
     if (argc != 5) {
       cout << "Usage: redact WORD INFILE OUTFILE NUM_STARS" << endl;
       return 1;
     }
   
     string inName = argv[2];
     string outName = argv[3];
   
     cout << "Copying from " << inName << " to " << outName << endl;
   
     string wordToRemove = argv[1];
     int numStars = atoi(argv[4]); // to double - atof()
     string replacement(numStars, '*'); // e.g. numStars is 3, makes ***
   
     ifstream fin(inName);
     ofstream fout(outName);
     if ( !fin.is_open() ) {
       cout << "Unable to open " << inName << endl;
       return 1;
     }
     
     if ( !fout.is_open() ) {
       cout << "Unable to open " << outName << endl;
       return 1;
     }
   
     string word;
     while (fin >> word) {
       if (word != wordToRemove) { fout << word << " "; }
       else { fout << replacement << " "; }
     }
   
     fin.close();
     fout.close();
   }

-----------------------------------------------------------------------
The Structure of :code:`argv`
-----------------------------------------------------------------------

.. youtube:: fRfxPaOX7b4
   :divid: ch05_04_vid_argv_structure
   :height: 315
   :width: 560
   :align: center

|
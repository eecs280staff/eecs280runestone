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

=================
Intro to EECS 280
=================

Welcome to EECS 280! We're glad to have you here!

.. image:: img/crabster_sign.png
   :width: 250
   :align: center
   :alt: Hi

|

This "book" contains chapters for each of Prof. Juett's EECS 280 lectures, broken down into small chunks with a video for each and sometimes additional exercises for you to practice and confirm your understanding.

I believe this is a great way to engage with the material! (It's not only for those who can't make the live lecture times.) You can set your own pace and reread/rewatch any part you like. But, just as with in-class exercises in live lectures, working through the exercises in Runestone is essential! Make sure you're an active learner - listening to me only goes so far, and you're the biggest factor in your learning.

You're welcome (and encouraged!) to work with others on the lectures, discussing the videos/examples or working through exercises together. I'll also start a Piazza thread for each lecture where you can ask questions, discuss exercises, etc. Please also feel free to come see me in office hours with any questions!


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Big Picture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 2

What's EECS 280 all about? Why are we here? Why do we care?

.. youtube:: d_aE2QjQyAI
  :divid: ch01_02_vid_big_picture
  :height: 315
  :width: 560
  :align: center

|


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Course Essentials and Grading
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 3

Let's take a look at the major parts of the course, including resources and websites you'll use to engage with the course and how the overall course is graded.

.. youtube:: lLU6RRCZHFw
  :divid: ch01_03_vid_course_essentials
  :height: 315
  :width: 560
  :align: center

|

Don't worry if this all seems a bit overwhelming. There are a lot of different components to the course and a bunch of different resources to get used to. You can find everything from `eecs280.org <https://eecs280.org>`_, and we'll try to keep you up-to-date with the most relevant material. I also highly encourage that you ask questions if you're feeling lost - on Piazza, Discord, in office hours, in lab, etc.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Lab Groups and Exercises
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 4

Lectures are followed up with labs, where you work with a small group of other students to explore and pratice the material further.

.. youtube:: EZ8ZAvGU-ss
  :divid: ch01_04_vid_lab_groups_and_exercises
  :height: 315
  :width: 560
  :align: center

|

Feedback from former students generally indicates that lab is often where the "real" learning happens. We do the best we can in lecture, but often times the hands-on experience in lab is what makes things click.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Projects and Autograder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 5

You get to exercise the skills you learn in lecture and lab in 5 programming projects throughout the course, designed to solidify your understanding and give you a chance to build some neat applications with real-world appeal!

.. youtube:: CY21lS9FQtA
  :divid: ch01_05_vid_projects_and_autograder
  :height: 315
  :width: 560
  :align: center

|

**Oops!** In the video above, I said "*everything in 280 is due at 8pm*". I should have said, "*the projects are due at 8pm, and everything else is due at 11:59pm*". (Also, we're technically in EDT rather than EST - ugh, timezones are hard.)


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Collaboration and Honor Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 6

We want you to learn with and from each other! Enjoying the class with others and having a network you can reach out to for help is highly encouraged. At the same time, we want to make sure everyone has an opportunity to learn for themselves and that nobody takes credit for someone else's work. We follow the UM CoE Honor Code.

.. youtube:: nxYgqqXjIhc
  :divid: ch01_06_vid_collaboration_and_honor_code
  :height: 315
  :width: 560
  :align: center

|

Let's have a conversation about how all this applies in 280. Linked here is a form with examples of several different scenarios that students might run into - what are your thoughts? How do we evaluate them with dual goals of collaboration and academic integrity?

`https://docs.google.com/forms/d/e/1FAIpQLSdCuRr919prkQG1xPKevc62MRYihYp9v9zPciVKJTFqSKNgKg/viewform?usp=sf_link <https://docs.google.com/forms/d/e/1FAIpQLSdCuRr919prkQG1xPKevc62MRYihYp9v9zPciVKJTFqSKNgKg/viewform?usp=sf_link>`_

After you fill out the form, you should be able to see how others responded here:

`https://docs.google.com/forms/d/e/1FAIpQLSdCuRr919prkQG1xPKevc62MRYihYp9v9zPciVKJTFqSKNgKg/viewanalytics <https://docs.google.com/forms/d/e/1FAIpQLSdCuRr919prkQG1xPKevc62MRYihYp9v9zPciVKJTFqSKNgKg/viewanalytics>`_

Please feel free to discuss your throughts in the Piazza Q/A thread (linked at the top of this page). If you're curious what I think...I'll plan to join the conversation in that thread.



^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Variables and References
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 7

It's time to dive into our first course material. Let's take a look at the connections between the code we write and what the program does at runtime. In particular:

- How do variables correspond to data in memory?
- What is a reference, and how does it differ from a regular variable?

.. youtube:: mpAO5F1rrlw
  :divid: ch01_07_vid_variables_and_references
  :height: 315
  :width: 560
  :align: center

|


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Scope and Lifetimes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 8

More questions!

- Why does the compiler have such strict rules on variable scope?
- How long does the data stored in a variable "hang around" at runtime?
- What is "memory junk" and where does it come from?

.. youtube:: 95KtAgkkHQU
  :divid: ch01_08_vid_scope_and_lifetimes
  :height: 315
  :width: 560
  :align: center

|


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Getting Help in EECS 280
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 9

A valuable skill in 280 is knowing how and when to ask for help! (This applies to the "real world" as well! That's why sites like `https://stackoverflow.com/ <https://stackoverflow.com/>`_ exist and are so popular. Real people ask for help all the time!)

.. youtube:: Fl64YLuRB2Q
  :divid: ch01_09_vid_getting_help
  :height: 315
  :width: 560
  :align: center

|


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Wrapping Up and Next Steps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. section 10

.. mchoice:: ch01_01_ex_compile_errors
  :answer_a: Select this one
  :answer_b: DO NOT select this one
  :answer_c: DO NOT select this one
  :answer_d: DO NOT select this one
  :correct: a
  :feedback_a: Good job!
  :feedback_b: Seriously, you won't get any credit for selecting this one...
  :feedback_c: Seriously, you won't get any credit for selecting this one...
  :feedback_d: Seriously, you won't get any credit for selecting this one...

  First, select answer A below. This lecture didn't have any "real" exercises, so we'll use this to measure your completion for lecture 1.


Let's take a look at what's coming next!

.. youtube:: TlsM1jxpKDQ
  :divid: ch01_10_vid_wrapping_up
  :height: 315
  :width: 560
  :align: center

|
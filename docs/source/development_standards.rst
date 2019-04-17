Development Standards
=====================

The value of software solutions is often clear and immediate. But many
are surprised when their project’s timeline and costs begin to spiral
out of control. Sometimes you can slow this freefall so it only takes
more use of the software to recover the costs, but it can also lead to
disaster. We know this routine very well. And we are passionate about
reducing these risks.

In the sphere of FOSS, it is important to live and breathe software
quality. When we publish open source code, we expose ourselves to more
unknowns. More clients, more use cases, and more reasons to change. For
the project to remain relevant, it must adapt quickly and reliably while
also adding value.

We also embrace the unknowns of a diverse group of contributors.
Different skill levels, experience, and opinions on how to write
software. When a project can align the power of diversity toward a
common vision, awesome things can happen.

These standards are a guide to help the project meet its long-term goals
and deliver value to the community. On this topic we have strong
convictions. And we have experienced the costs of failure to follow
them.

We also arn’t perfect, so we write these down and focus code review on
these standards.

These standards are also here so future you and other contributors have
an easier time writing new features or fixing defects.

Code Style
----------

We follow PEP-8 formatting with some modifications. The modifications
bring formatting more in line with Google’s Python style guide and some
quality of life improvements. We also use Google style docstrings.

*Please use our auto formatter configuration file.* When in doubt,
follow the conventions in the module you are working in.

Readability
-----------

Everyday writing is hard. Capturing the right tone, words, and structure
to communicate clearly and concisely isn’t trivial. And that’s using a
tool (written human language) that’s been in active development for
thousands of years.

Programming languages don’t make communication any easier with all the
symbols and *OddBall* *waysOf* *jamming_words_together*. How we name and
structure our code has a profound influence on readability. And
readability influences velocity and quality.

   “Indeed, the ratio of time spent reading vs. writing is well over
   10:1. We are constantly reading old code as part of the effort to
   write new code. Because this ratio is so high, we want the reading of
   code to be easy, even if it makes the writing harder. Of course
   there’s no way to write code without reading it, so making it easy to
   read actually makes it easier to write.”

*Martin, Robert C. The Robert C. Martin Clean Code Collection
(Collection) (Robert C. Martin Series). Pearson Education. Kindle
Edition.*

In the context of FOSS, it is particularly important to consider the
effect of poor readability on your community. Given an unknown audience
of great diversity, we ought to make special effort to ensure the
meaning of our code is self-evident.

Here are some rules of thumb we like to follow:

   **The Sentence Check:**
   Read your code out loud. If someone not familiar with the project
   could understand you, it should be good. This is easier with higher
   level policies and interfaces than with low level details, of course.

   **Universal Readability > Idioms > Conventions:**
   Prioritize universal understanding over idiomatic code or
   conventions.

   Many languages have unique ways of doing things, or idioms. If those
   idioms interfere with readability and supply no other significant
   value, avoid using them. A one-line Python list comprehension can be
   beautiful. But, can quickly turn into a tangled mess if it grows
   beyond a single line.

   Many conventions exist to serve needs that are outdated or
   unnecessary. We will touch on common conventions later.

   **Comments are Red Flags:**
   Specifically, comments that describe *what* the code is doing show
   the code isn’t expressive enough. If the code is expressive, then the
   comment will be redundant and become another axis of change, defects,
   and waste.

   This guideline doesn’t apply to docstring comments or comments that
   describe *why* a contributor took a specific approach. When we write
   controversial code, a good comment describing why we wrote it is
   especially useful.

Names
~~~~~

As a software engineer, you spend much of your time reading code. When
you aren’t reading, you will be naming things. Variables, methods,
classes, modules, packages, and tests. The quality of your names has a
direct effect on the productivity of your peers and future you.

A name should communicate what, how, and why in as few words as
possible.

Variables
~~~~~~~~~

Variable names should be nouns separated by underscores. Either singular
or plural depending on context. You can usually name a list of employee
objects, *employees.* Context, such as scope and the variables within
the scope, can inform other decision about variable names. Variables
should be more descriptive and verbose when they occupy a broader scope.
Global variables should then supply all the needed context within their
name. Consider: *globals.DATABASE_TIMEOUT_IN_SECONDS* vs.
*database.connection.settings.timeout*. Both timeout variables are
appropriately descriptive within their scope.

You should avoid encodings, prefixes, suffixes, and pointless
conventions. This includes:

-  Type “hints” in the name. If you have two collections in the same
   scope that hold the same things but in different collection types,
   then please use some typing information in the name. Otherwise, the
   type “hint” becomes noise and in some cases disinformation. The
   variable *full_name_string* is no more informative than *full_name*.
   Neither is *employee_object* more informative than *employee*.

-  Conventions like Hungarian notation and *m\_* for members do not add
   value.

Conventions that can help:

Single letter variables can work well in little algorithms that carry
history and meaning. For example, incrementors can be, “\ *i*.” And
formulas can use their common variable letters, such as:

In Python:

.. code-block:: python
   :linenos:

    a = 3
    b = 5
    c = math.sqrt(a \*\* 2 + b \*\* 2)
    print(str(c))

However, you may also consider using more descriptive names for those
without specific knowledge.

**Example:**

.. code-block:: python
   :linenos:

    adjacent = 3
    opposite = 4
    hypotenuse = math.sqrt(adjacent \*\* 2 + opposite \*\* 2)
    sine = opposite / hypotenuse

You may also use the common access level intention hints that are common
in the Python community. A single leading underscore to communicate that
clients shouldn’t use this member outside of the class. If it is
important that clients do not easily access the member, go ahead and
name mangle it with a leading double underscore.

Please use all caps for constants.

Classes, Modules, Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~

All high-level collections should also be nouns. The higher-level you
go, the more bias you should express toward using problem domain names.
The lower level you go, bias toward solution domain names. Looking at
the root of your project, you should be able to clearly understand what
problem the software is trying to solve. As you click into the folders
and then the modules you should see more of how the engineers have
chosen to solve the problem.

**Example:**

-  gamebench_client

   -  api

      -  api_facade.py

      -  entity_request_mediator.py

      -  requests

         -  interfaces

            -  requests_library_adapter.py

            -  request_builder.py

         -  parameters

            -  parameter_builder.py

            -  parameter_director.py

         -  methods

            -  method_factory.py

         -  urls

            -  url_builder.py

            -  url_director.py

      -  entities

         -  entity_factory.py

         -  metrics

            -  metric_factory.py

            -  cpu.py

            -  gpu.py

         -  sessions

            -  session.py

   -  settings

      -  defaults.py

      -  custom.py

When using a design pattern or common structural elements, use the
common names for these. Examples: *URLLibAdapater*, *RequestBuilder*,
*UserModel*, or *UserView*.

Packages and Modules
^^^^^^^^^^^^^^^^^^^^

Use all lowercase words separated by underscores. Singular or plural
based on context.

Classes
^^^^^^^

Use *CamelCase* nouns. Singular or plural based on context. The more
specific a class becomes, the more verbose its name will become.
Consider *User*, *EmployeeUser*, *AcmeCorpEmployeeUser*. Each covers a
specific set of behaviors and data and the name becomes more verbose. If
you use a class far away from its definition or the path does not supply
good context, you should also consider a more descriptive name over a
concise name if refactoring the structure isn’t practical.

Methods
^^^^^^^

Methods are actions, so they should be verbs. Use lowercase underscore
separated words. A method should either ask a question (query), ask for
data (query), or issue a command that changes state. A method should not
be both a query and command. So be sure that your name matches the
action type to avoid confusion.

**Query and Command Separation:**

.. code-block:: python
   :linenos:

    class User:
        def __init__(self, first_name, last_name):
            self.first_name = str.strip(first_name)
            self.last_name = str.strip(last_name)
            self._is_active = True

    def get_full_name(self):
    """ Query the full name of the user."""
        space = " "
        full_name = space.join([
            str.title(self.first_name),
            str.title(self.last_name)
            ])

        return full_name

    def activate(self):
    """Change state of user to active."""
        self._is_active = True

    def deactivate(self):
    """Change state of user to inactive."""
        self._is_active = False

    def is_active(self):
    """Query user's active status."""
        return self._is_active

Avoid This:

.. code-block:: python
   :linenos:

    def activate (self):
    """Change state of user to active and return user._is_active."""
        self._is_active = True

        return self._is_active

In command methods, use exceptions to communicate failure rather than
different returns.

Be consistent when using words that have little distinction. For
example, what is the difference between get and fetch? We default to
using “get” for query methods until we find another name with a
meaningful and unambiguous distinction that fits the context. One might
argue that get_full_name() isn’t a pure getter. We tend to agree.
Someone might name it, concatenate_first_and_last_names(). The problem
is that “concatenate” sounds like a command that changes state and does
not return anything.

There is processing but no state change and we want the full name
returned. We are preferring *clarity of intent* over perfect accuracy or
conformity to convention. Depending on the scope of this methods use,
you might even name it my_user.get_first_and_last_as_full_name().

The Python standard library doesn’t always do this. For example,
*str.join()* returns the joined elements of the iterable given in the
arguments into a string using the string object calling it as the
separator. It is a confusing method if you aren’t familiar with it. It
sounds like a command but returns data and the caller occupies an odd
role. For greater clarity, a *to_string()* method on the iterable class
and/or *from_iterable()* on the string class. Ideally, both would be
available.

To get a sense of clarity, try reading the following code out loud:

.. code-block:: python
   :linenos:

    full_name = space.join([
        str.title(self.first_name),
        str.title(self.last_name)
        ])

*“Full name equals space join stir title first name and stir title last
name.”* The choice to use “str” is historical and a barrier to entry for
those new to our field. As is “char,” “int,” and all other abbreviated
words. Consider these alternatives:

.. code-block:: python
   :linenos:

    def get_full_name(self):
        full_name = self.first_name.get_title_cased() +
            " " +
            self.last_name.get_title_cased()

        return full_name

    def get_full_name(self):
        full_name_items = [
            self.first_name.as_title_cased(),
            self.last_name.as_title_cased()
            ]
        full_name = String.create_from_list(name_elements, separated_by=" ")

        return full_name

The first reads: *“Full name equals first name get title cased plus
space plus last name get title cased.”*

The second reads: *“Full name items equals first name as title cased and
last name as title cased. Full name equals a string created from list of
full name items separated by a space.”*

Both examples are much closer to spoken English. And you can see there
is quite a bit of latitude to carefully consider names. With just a few
*minor* interpretations, these really could read as a normal
sentence\ *. “The full name is a string created from a list of name
elements separated by a space.”* As you write your code, try to find
ways to reduce the amount of interpretation needed and your intent will
become clearer.

**Examples:**

*my_string = some_list_object.to_string([separator])* which would return
a new string object.

*my_string = String.from_iterable(iterable[, separator])* This would be
an override of *String.__init__()*.

This isn’t a judgement of Python. We love Python and enjoy it the most
of all interpreted languages. We also recognize that this would be a
substantial change. We also recognize the historical context that this
appears to come from.

The method, *str.join()* is a good example of how names and structure
can influence the learning curve through readability. When learning
curves are low, everyone can be more effective more quickly.

You will also notice in the query and command separation examples there
are two setters for the active property. We aren’t against setters as a
convention, but if there is an opportunity to make code more semantic,
we like it. In this case, calling a method with no arguments and a name
expressing clear intent is a straightforward way to reduce silly bugs
and increase readability.

.. code-block:: python
   :linenos:

    new_hire = Employee.from_full_name(full_name)
    new_hire.set_active(True)
    new_hire.save()

# vs:

.. code-block:: python
   :linenos:

    new_hire = Employee.from_full_name(full_name)
    new_hire.activate()
    new_hire.save()
# even better, but this comes later.

.. code-block:: python
   :linenos:

    human_resources_facade.onboard_new_hire(full_name)

Automated Tests
---------------

We passionately believe quality automated tests are critical to the
success of any software project.

   “The third of W. Edwards Deming’s fourteen points for management
   states, ‘Cease dependence on inspection to achieve quality. Eliminate
   the need for inspection on a mass basis by building quality into the
   product in the first place’ (Deming 2000). In continuous delivery, we
   invest in building a culture supported by tools and people where we
   can detect any issues quickly, so that they can be fixed straight
   away when they are cheap to detect and resolve.”

*Forsgren PhD, Nicole. Accelerate: The Science of Lean Software and
DevOps: Building and Scaling High Performing Technology Organizations.
IT Revolution Press. Kindle Edition.*

We also believe that how we distribute our effort across the test levels
can have profound effects on the usefulness and value of the tests. We
solve for how to spend effort by understanding when testing creates
value. Finally, we need to understand what parts of the process of
development, testing, and fixing defects are the most expensive.

Google has published a nice little article on this topic:
https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html

Ideal Distribution of Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The lower level the test, the faster it runs, the more quickly you get
feedback, and the defect is more isolated. This means faster fixes. Aim
to have 70% of your tests be unit level tests. A unit is simply the
smallest container of organization. In our case, that is a method or
function.

Pull requests must have all *applicable* test levels covered before
maintainers merge it to master.

Coverage
~~~~~~~~

The ideal coverage is 100%. With a language like Python, 100% can be
possible. CI checks enforce 95% coverage from the entire suite. You do
not need to add unit tests for these things:

-  Objects that you cannot call directly.

-  Trivial methods. Methods that have no branching logic and only use
   the simplest of statements. Example:

..
.. code-block:: python
   :linenos:

    def get_name(self):
        return self.name

-  3\ :sup:`rd`-party libraries, unless you suspect they are defective.

.. _section-1:

Recommended Approach
~~~~~~~~~~~~~~~~~~~~

There are competing approaches to writing tests. Given the goal of fast
feedback and the Lean principle of building quality into production
processes, test-driven development is the clear winner. We have noted
some confusion about what is and isn’t test-driven development (TDD).

Here is the short story:

-  There is no single magic potion to make clean higher quality code.
   You must exercise multiple disciplines to reach the goal. TDD is just
   one of them.

-  TDD as we recommend practicing it, is super Lean. *TDD has several
   cycles* that cover the entire scope of the application from
   line-to-line all the way up to architectural considerations.

-  TDD doesn’t mean you can skip planning and design altogether. Have a
   big picture in mind. But don’t force your design to work. Through the
   full TDD cycle, you will gain information that will better inform
   your structure.

Test-Driven Development (TDD):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When we talk about TDD, we are talking about a multi-cycle process. The
cycles of TDD have distinct goals. An engineer must use all the cycles
well to realize the full benefits of TDD.

Second-by-Second:
^^^^^^^^^^^^^^^^^

The focus here is brutally simply: *Make it work!* And at *any* cost.
You will move through this cycle several times before a unit test is
complete.

1. Write a failing test before any production code.

2. No more test code than you need to create a failure.

3. No more production code than you need to pass the failing test.

The tests you write at the beginning of the second-by-second cycle will
be ugly. And the production code you write will be too. Just make them
pass. Don’t resist this.

If you get stuck at any point in this cycle, either because you cannot
make the test pass or because you feel like you must write a bunch of
untested production code, your test is wrong. The test definition might
be incorrect, or the test covers too much of the problem. *Think smaller
and focus on what you know first.*

Minute-by-Minute:
^^^^^^^^^^^^^^^^^

This is the first step where you will begin to focus on making it
“right.” You will move through the complete cycle about once per unit
test.

The refactor step is a common point of failure. Sometimes we speed right
past it and then only later realize our code is gross. Always keep your
eye out to remove duplication and improve readability once your code
works, but not before. *Focus* on one problem at a time. Moving on to
make a new unit test pass without refactoring only makes the work to
clean it up bigger and riskier. And that’s not Lean.

Refactoring must be a continuous activity part of the minute-by-minute
process of creating software if we are to make *software that works and
can change easily*. There is not going to be time later. There is no
tomorrow. There is only now…

10 Minute Cycle – Generalize:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here we apply even more effort toward making it right. Within this
cycle, you will be applying the `Transformation Priority
Premise <https://en.wikipedia.org/wiki/Transformation_Priority_Premise>`__.
Look for overly specific production code and then generalize it. Your
tests and test suite should become more specific and detailed, but your
production code should also become more general.

Here, you might again find yourself stuck. If that happens, you need to
start removing tests until you can take a different approach with
different tests.

Hour-by-Hour – Architecture and Design:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Finally, we make things right within the context of bigger design
buckets. A focus on the small or local problem can blind you to the fact
you are crossing architectural boundaries or violating SOLID principles.
You should take time every hour or so to analyze your design, but don’t
make changes unless all your tests are passing.

We will talk about architecture and object-oriented design in a later
section.

Scope of a Unit Test
~~~~~~~~~~~~~~~~~~~~

In traditional QA language, a unit is the smallest measure. Typically,
this would be a method. Following TDD, you will make your production
code increasingly general as your test become more specific. This means
you start out with a unit test covering one method but then you break
that method into smaller units as you extract out logic. That original
unit test is still covering the refactored code. This is a decision
point.

One path would suggest that you mock out the behavior of the new methods
for isolation. Another would be to ensure that your current unit test is
supplying all the behavioral coverage needed and stop there. The correct
response is a judgement call. And there are trade offs. The more you
mock, the more you couple your tests to implementation. The less you
mock the less isolation you achieve.

There are real dangers to both. Coupling tests to implementation can
lead to overly fragile tests. But insufficient isolation can reduce the
benefit of unit level testing. The ideal test pyramid is a guide to help
you, so are your fellow engineers. So, talk it through, weigh the risks
and benefits, and decide.

Documentation
-------------

If we write our code well, how we intend others to use it should be as
self-evident as how it works. That’s a nice goal, but let’s not lean
into that too much. Many of the words we use in programming are
overloaded or not universally understood. Our documentation aims to
reduce those risks while reducing the risk of spending too much time on
documentation that might change too often to be useful. Here is our
approach:

-  We write docstrings as part of the development process for everything
   but the most trivial code. We include everything a client would need
   to know to use the code and what to expect from it.

-  We write or update user documentation as needed. We include only what
   a user needs to understand what we believe is the ideal way for them
   to use the software. For example, a user should only ever need to
   interact with the entity factory method and the objects it returns to
   them. So, we document this method and the objects it returns with
   realistic use cases and examples.

-  We also document where we have designed the software to be
   extendable. For example, if you can only use a specific HTTP library
   for security reasons, we will supply examples of how you can replace
   the Requests library.

-  We document the parts of the software that you can change through
   configuration settings.

As you work on features and bug fixes, you will be creating and updating
docstrings. You should also cross-reference the documentation to be sure
that your changes don’t create buggy documents.

All documentation must be in a format understood by Sphinx. Please use
reStructuredText as the markup language. See the “Resources” section for
links.

Object Oriented Design and Software Architecture
------------------------------------------------

Our goal with design and architectural decisions is to reduce coupling
and improve understanding of the system. To create working software is
not enough. We must also create software that is easy to change and
adapt to different environments.

Object Design
~~~~~~~~~~~~~

How we design our objects influences how easily others understand our
software and how easy it is to change. As an engineer gains more skill,
they will learn diverse ways to exploit object-oriented techniques to
achieve these goals.

The Starting Point: Cohesion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To begin, our classes tend to reflect reality in some logical way. A car
class has properties like make, model, year, and color. And methods like
accelerate and brake. As a start, this is okay but quickly starts to
fall apart as we try to model this class closer to real cars. For
example, not all cars have four wheels, 5-speed manual transmissions, or
run on gasoline. Most cars steer with just the front two wheels, but
some have 4-wheel active or passive steering.

As we add more configurations, these configurations then introduce
changes to what behaviors are possible and how you implement those
behaviors. If we stay in this mode of thinking, we will up end with a
giant class full of if statements, huge methods, and bugs.

If you are new to OOP, we suggest thinking about class design in terms
of cohesiveness rather than a logical reflection of the real world. This
should lead to more but smaller highly focused classes and fewer
parameters in constructors and other methods.

Look for these warning signs:

-  Methods with more than 3 or 4 parameters. These might reveal to you a
   class in hiding.

-  Methods that don’t act on any properties or supply a high-level
   interface to other methods in the class. These might reveal to you
   feature envy. The method might better belong in another existing
   class or a new class.

-  A group of methods act on a group of properties and another group of
   methods on another group of properties. These might reveal to you a
   class in hiding.

The Next Step – SOLID
^^^^^^^^^^^^^^^^^^^^^

It is helpful to have a framework of principles to guide us toward
highly cohesive classes and make design decisions that help us reduce
rigidity and fragility in our software. We like Dr. Martin’s collection
of object-oriented design principles for their relative simplicity and
the easy to remember acronym.

Single Responsibility Principle (SRP)
'''''''''''''''''''''''''''''''''''''

A class should have one and only one reason to change. An easy
illustration is a report. The format of the report and the calculations
that create the data within it are distinct reasons to change. These
responsibilities should live in different classes.

Open-Closed Principle (OCP)
'''''''''''''''''''''''''''

You should be able to extend a class’ behavior without changing the
class. For example, you should be able to add support for Python’s
urllib without changing any code related our implementation of the
Requests library. GamebenchClient.api.requests is open for extension.
You would implement a new concrete adapter inheriting from the adapter’s
ABC and enter a custom setting for request library path.

The result of designs that conform to this principle is the ability to
add new features without changing already working code.

Liskov Substitution Principle (LSP)
'''''''''''''''''''''''''''''''''''

Methods that use or refer to a base class must be able to use objects of
derived classes without knowing anything has changed. This one can be
obvious when you have a bunch of if, elif, else statements figuring out
how to work with derivatives. However, you can violate this one more
subtly too. If you find yourself changing the base class definition to
accommodate a new derivative, it is a sign you might be violating this
principle.

Interface Segregation Principle (ISP)
'''''''''''''''''''''''''''''''''''''

You should not force a client to depend on methods it does not use. What
this means is that you should be defining small interfaces specific to a
client. If you find that your interface has methods used by one client
and a group of methods used by another, split them out into different
interfaces. For example, we don’t want our interfaces that handle
creating URLs and other request parameters to know anything about the
Requests library’s interface. We certainly don’t want an import
dependency. So, we have used the adapter pattern to conform the two
interfaces. If we need to conform another HTTP library to our module, we
simply derive another adapter.

This principle further guides us toward pluggability and software that
is simple to change.

Dependency Inversion Principle (DIP)
''''''''''''''''''''''''''''''''''''

Always depend on abstractions, not concrete classes. If you consistently
apply OCP and LSP, you will arrive at this dependency inversion
principle. You will know you are violating this principle when you
change one thing and must change many others, you make one change that
breaks other areas that might even be unrelated, and you cannot reuse
your module in another piece of software.

One of the places we see this principle most violated is in web
applications that use an ORM. If your core business logic has direct
dependencies on your framework, you couple the code that has the most
value to a trivial detail. The cost to change is incredibly high. The
solution is to provide an interface that allows you to swap ORMs with
relative ease and keep the ORM imports out of your critical business
logic.

We measure abstractness as the distance from I/O. There are other ways
to think about it, but this is the most straightforward way we have
found. The closer a module or class is to inputs or outputs, the more
concrete it is. A file reader/writer, HTTP request/response, and device
drivers are good examples of the most concrete details.

This principle applies between classes, modules, and the entire
architecture of the software.

Step Three: Common Problems w/ Common Solutions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After some time designing objects, you will find common problems that
you will need to solve. A frequent problem ought to have a common
solution. This is where design patterns come in to save the day. Diving
into design patterns is outside the scope of this document, but you will
see solution domain names related to design patterns all throughout this
project. You will also likely run into a reviewer asking you to use a
certain pattern when creating a new feature.

We encourage you to study all the design patterns, when to use which,
and practice design pattern katas. One problem you will run into is with
examples. For some reason, many examples are much too general and
unrealistic. This is a shame. You end up having to synthesize
information you read with the example given and the realities you know.
If you are not very experienced, these examples might even feel
pointless. Don’t fear. Practice helps and we are here to help too.

One thing you will notice in common with many of the design patterns is
the use of “has-a” rather than “is-a” object relationships. A request
object *has a* mediator object. A metrics object *has a* mediator
object. This is a powerful concept worth exploration and practice. Go
for it.

See the “Resources” section for more information on design patterns.

Is this Pythonic?
^^^^^^^^^^^^^^^^^

Python is an interpreted language, so some of the advantages of these
principles aren’t relevant. Specifically, source code dependencies do
not mean we have to suffer recompiling or building many modules when we
could have used dependency inversion to only rebuild one. However, that
isn’t the only benefit of these principles. It is just a massive one
when you are working in huge complex software projects that need many
teams working on distinct parts of the system.

We still get the benefits of a more intuitive structure, loose coupling,
and more freedom to solve problems that only appear after our software
is in use by customers. Let’s say we release a web application and find
that we really need to switch to a horizontal scaling database like
OrientDB. Oh no! We developed our software using Django and adding
OrientDB support would take a long time. We are victims of our own
success. To make it worse, we followed “web MVC” advice and put all
kinds of business logic in the model! Woe to the fat model! Woe to tight
coupling!

All we needed to do to protect ourselves was to separate and isolate our
core business logic from all other concerns and dependencies. Then
create an interface for PyOrient OGM. That’s a much smaller lift that
figuring out how to extend the Django ORM to work with OrientDB. We’ve
investigated it. Which should tell you that some of us have made
mistakes like this and learned from it.

Python also gives you incredible power to solve problems using
polymorphism. We have multiple inheritance. We have functions that are
objects. We can override fundamental behaviors of Python. That’s cool.
Some might say Python trusts us too much, but that means we need to take
care to be responsible professionals.

*Within the best of our knowledge and skills, we commit to do no harm to
function or structure. And the maintainers can help you make the same
commitment.*

Design Red Flags
^^^^^^^^^^^^^^^^

*Fragility:* Your change is causing tests to fail in modules you didn’t
change. Or Refactoring causes many tests to fail.

*Rigidity:* To add a new little feature, you must change code in many
places.

*Train Wrecks:* Object.object.object.method().method().choo_choo

*Tight Coupling:* Logic for real world processes occupying the same
space as or depending directly on frameworks, databases, drivers, and
other I/O modules.

Resources
---------

Awesome Authors:
~~~~~~~~~~~~~~~~

`Robert C. Martin (Uncle
Bob) <https://www.amazon.com/Robert-C.-Martin/e/B000APG87E?ref=sr_ntt_srch_lnk_2&qid=1551285619&sr=8-2>`__:
One of the original signers of the Agile Manifesto. *The* Clean Coder.

`Martin
Fowler <https://www.amazon.com/Martin-Fowler/e/B000AQ6PGM?ref=dbs_a_def_rwt_sims_vu00_r0_c0>`__:
One of the original signers of the Agile Manifesto. Author of a
fantastic book on refactoring.

`Kent
Beck <https://www.amazon.com/Kent-Beck/e/B000APC0EY?ref=dbs_a_def_rwt_sims_vu00_r0_c1>`__:
One of the original signers of the Agile Manifesto, creator of Extreme
Programming, pioneer of design patterns, and test-driven development.

Testing
~~~~~~~

`Google: Just Say No to More End-to-End
Tests <https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html>`__

`Kinds of Tests: Uncle Bob – First Class
Tests <https://blog.cleancoder.com/uncle-bob/2017/05/05/TestDefinitions.html>`__

Test-Driven Development:
~~~~~~~~~~~~~~~~~~~~~~~~

`Uncle Bob: The Three Laws of TDD <https://youtu.be/AoIfc5NwRks>`__
(video)

`Uncle Bob: The Pragmatics of
TDD <https://blog.cleancoder.com/uncle-bob/2013/03/06/ThePragmaticsOfTDD.html>`__

`Uncle Bob: Giving Up on
TDD <https://blog.cleancoder.com/uncle-bob/2016/03/19/GivingUpOnTDD.html>`__

`Martin Fowler: Mocks Aren’t
Stubs <https://martinfowler.com/articles/mocksArentStubs.html>`__

Object-Oriented Design
~~~~~~~~~~~~~~~~~~~~~~

`SOLID Principles <https://en.wikipedia.org/wiki/SOLID>`__

`Design Principles and Design
Patterns <https://web.archive.org/web/20150906155800/http:/www.objectmentor.com/resources/articles/Principles_and_Patterns.pdf>`__

`Design Patterns on
Wikipedia <https://en.wikipedia.org/wiki/Software_design_pattern>`__:
This is a nice summary with examples.

`Refactoring.Guru <https://word-edit.officeapps.live.com/we/Refactoring.Guru>`__

`Source Making: Design
Patterns: <https://sourcemaking.com/design_patterns>`__ This is a great
resource for choosing from competing patterns and refactoring
techniques. However, the Python examples aren’t useful to many novices.

`Uncle Bob: The Clean
Architecture <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>`__

.. _documentation-1:

Documentation
~~~~~~~~~~~~~

`Getting Started with
Sphinx <https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html>`__

`reStructuredText
Primer <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__

`An Introduction to Sphinx and Read the Docs for Technical
Writers <http://www.ericholscher.com/blog/2016/jul/1/sphinx-and-rtd-for-writers/>`__

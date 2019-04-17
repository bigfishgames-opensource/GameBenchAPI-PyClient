Contributing
=============

Who can Make Contributions?
---------------------------

We want everyone to feel free and welcome to add value to this project.
We welcome all people from all roles and skill levels.

If you are a beginner, you might start with improving documentation,
fixing lightweight bugs, little refactoring tasks, and improving tests.
Please reach out to us and we will help you find approachable work.

Regardless of experience, we encourage you to talk through your plans
with us and push branches early to get feedback before you get too deep.

What Code You Can Contribute
----------------------------

All code must be compatible with the license shipped with the project.
This project is a
`BSD-3 <https://opensource.org/licenses/BSD-3-Clause>`__ licensed
product. By contributing, you certify that you have a legal right to
submit your contributions.

Contacting Us
---------------------------

We have a
`Gitter <https://gitter.im/bigfishgames/GameBench-API-PyClient?utm_source=share-link&utm_medium=link&utm_campaign=share-link>`__
community setup for chatting through issues, feature requests, and all
things software development.

The Development Environment
---------------------------

IDEs and text editors are very personal decisions. We want to you work
with tools that you are effective using. We have supplied an
EditorConfig file, configuration files for static analysis, and auto
formatters, as well as our PyCharm .idea folder.

We love PyCharm, we recommend PyCharm, and we hope you use PyCharm and
learn all its tools and shortcuts. If we can make one pitch, it is that
we have PyCharm configured to use the same static analysis and
formatting settings we check on push. Early feedback is always better
than late feedback.

Project Management
---------------------------

We run a simple `ZenHub Kanban board <https://app.zenhub.com/workspaces/gamebenchapi-5cabf535a736c27636b0283d/board?repos=180245554>`_. You are welcome to work anything in the
*backlog* at any time if it does not depend on incomplete stories. We
prioritize the backlog every other Monday morning. Please find the
highest priority item you would like to work on and commit to finishing
within 2 weeks. While we are backlog grooming, we will look for items
that have been in progress for 2 weeks and check on the status.

Version Control Process
---------------------------

Master
~~~~~~~

The master branch should always be releasable. Unreleased working
software isn’t supplying value to anyone. Our development standards and
processes exist to help this be a reality.

Branching
~~~~~~~~~

When you begin work on a bug fix or feature, cut a branch from master.
Be sure your local master is up to date with the remote master branch
before creating yours. Name the branch with a clear concise name
followed by the issue number. Ex: *URLlibSupport-#1123* or
*FixDuplicateHTTPRequests-#213*

Update your branch from master often as you work to avoid complex
conflict resolution at the end.

Commits
~~~~~~~~

We recommend that you commit early and often. This gives you more
freedom to go back and forth between commits as your solution evolves.
However, the frequency of commits is a personal preference.

Commits messages should help you and others quickly understand what has
changed and why. This can often be a way to track down new bugs or
regressions. Finally, include a GitHub issue reference in all commits.

**Summary:** This should be a short title.

*Example:*

*Interface Adapter for urllib.request.Request() #1234*

**Message:** The message should call out what has changed and very
briefly why.

*Example:*

*Issue #1234*

*Added ULRLibRequest adapter class to match output from
api.request.factory to input of urllib.request.Request() to keep
interface segregation and decouple the library from our use cases.*

*Updated RequestTarget ABC to allow generic adaptees and specific
adaptees in the adapter implementations.*

*Removed outdated inline comment from RequestTarget to improve
readability.*

.. _section-1:

Pushes
~~~~~~~

Push your branch to remote early in the process and then as you have
working pieces complete.

The early push is to get your early design decisions out quickly. This
allows you to share your branch with others for feedback even before a
formal pull request and code review. Finding issues early is much easier
to deal with than finding them later. This is an important consideration
if you are new to our development approach or an inexperienced engineer.

Finally, you will create a pull request when you have finished. Pull
requests have several automated checks that need to pass before we can
merge your branch into master.

-  The full test suite must pass.

-  Docs generated.

-  Static analysis must pass.

-  Code coverage must be above 95%

-  Compliance checks must pass.

In addition to the automated checks, an official maintainer must approve
the pull request.

Code Review
--------------

Code review can be awkward for some engineers. It can be difficult to
put your work up for judgment. Rest assured, future you will come to
love it if you embrace it as an opportunity to learn and grow. Even when
we disagree, we all come away with a broader perspective.

We all write imperfect code. If no one ever exposed us to different
approaches, we would never grow. Submitter and reviewer must put aside
their egos and help each other.

For reviewers, you are there to help the project and the submitter be
successful. That means you must be clear and concise with your feedback.
Candid, but respectful. You must also present a path forward. If you
call out some code for improvement, we expect you to call out the
standard it is violating and a little nudge in the right direction.

If either party violates our :any:`Code of Conduct <../CODE_OF_CONDUCT>` , we will act as described
in that policy.

Code review is a critical step in creating quality software. More eyes
and minds are always better than fewer. Everyone who takes part can
learn and grow, not just the submitter.

Code reviewers should focus entirely on whether the submission aligns
with our development standards. Some elements might be subjective and
not all code needs to perfectly align with standards. Everyone should
strive for a consensus on what things the submitter must change, which
should be new stories, and which are trivial.

There is a danger in kicking the can down the road when it comes to code
quality. These things tend to snowball and drive down velocity over
time. If a change adds certain value, it is worth doing now. Not later.

We will quickly reject pull requests that have any of the following
anti-patterns and quality risks:

-  No unit tests.

-  No integration tests.

-  Classes with low cohesion. If there is not a strong working
   relationship between the properties and methods.

-  So-called “god” classes and methods.

-  Many methods that exceed 10 logical statements.

-  Many methods that need more than 5 arguments.

-  Many methods that have many levels of indentation, such as nested if
   statements and nested loops.

-  Copy/paste programming.

Free Open-Source Software (FOSS) is amazing because it brings together
people who want to add value for everyone. We want you to succeed. So
please push your branch early and ask for feedback if you see any of the
items above appearing in your code.

A maintainer will merge the branch to master and release when you and
the reviewers have reached consensus, fixed issues, and all automated
checks have passed.

Next up, Development Standards!

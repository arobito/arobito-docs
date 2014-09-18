.. Copyright 2014 The Arobito Project
   
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
   
       http://www.apache.org/licenses/LICENSE-2.0
   
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   

Coding for Arobito
==================


Development Environments and Systems
------------------------------------

We're not limited to a special operating system. Of course, we're recommending a free and open source OS (like Debian or SuSE Linux).

The same goes for IDEs. There is no rule that says one must use this or that IDE. For Python development, we're recommending `PyCharm by JetBrains <http://www.jetbrains.com/pycharm/>`_, which is available as Community Edition for free.


Programming Languages
---------------------

For the Raspberry Pi backend driven by Arch Linux we prefer Python 3.4. It is the primary project language.

For the web frontend we're using XHTML5, JavaScript and CSS3. The backend is again driven by Python, powered by the famous `CherryPy web framework <http://www.cherrypy.org/>`_.

The Arduino Code is written in C. We're programming the Atmel micro controller directly over the ICSP pinout to save the space for the boot loader.


Coding Conventions
------------------

There is not yet a document that exactly describes how to code. The PyCharm IDE knows a lot about coding conventions and code formatting, so we take the hints there for real.


License Headers
---------------

One thing is a must: Every source code file needs a header, formatted as a comment. It has to be the first thing in every file (except a shebang line). The block tells the viewer about the license of the code.

.. code:: text

   Copyright {year} The Arobito Project
   
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
   
       http://www.apache.org/licenses/LICENSE-2.0
   
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


Additionaly, all Python files need the following license description:

.. code:: python

   __license__ = 'Apache License V2.0'
   __copyright__ = 'Copyright {year} The Arobito Project'


Python Coding
-------------

Python files are encoded as UTF-8. We prefer Unix-style line endings.

After the license header, the imports take place. Below the inputs and before the first line of code, the author of the file/module must be set:

.. code:: python

   __author__ = 'Max Musterman'
   __credits__ = [ 'Max Mustermann' ]
   
With more than one author:

.. code:: python

   __author__ = 'Eva Musterfrau, Max Mustermann'
   __credits__ = [ 'Eva Musterfrau', 'Max Mustermann' ]
   
It could be helpful to add a maintainer:

.. code:: python

   __maintainer__ = 'Max Mustermann'


TODO: Define how docstrings shall look like, how parameters are defined and how return types are marked.


Documentation
-------------

The project documentation is made with Sphinx using reStructuredText-Files. Additional papers are made with a to-be-created LaTeX class.

The documentation root path in the project folder is ``/doc``.

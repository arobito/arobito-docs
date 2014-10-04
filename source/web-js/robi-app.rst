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


robi-app.js
===========

This is an overview over the ``/src/web-static/robi-assets/robi-app.js`` file contents. It contains the main stuff for
the Arobito communication between the backend and the web frontend.


Namespace
---------

The code in the ``robi-app.js`` creates the namespace ``window.robi`` (or just ``robi`` for short) to make it's
functions public. It also has the internal namespace ``local`` which is not available outside the module's code.


Initialization
--------------

The module initialize itself on document load time. There is no additional loading necessary.


API documentation
-----------------


Public Methods
..............

.. js:function:: robi.error(title, message)

   Create a error growl message (the little pop-up in the upper right window corner)
   
   See also :js:func:`robi.warn <robi.warn>`, :js:func:`robi.notice <robi.notice>`, :js:func:`robi.message
   <robi.message>`. 

   :param string title: The title of the pop-up
   :param string message: The message to display

.. js:function:: robi.warn(title, message)

   Create a warn growl message (the little pop-up in the upper right window corner)

   See also :js:func:`robi.error <robi.error>`, :js:func:`robi.notice <robi.notice>`, :js:func:`robi.message
   <robi.message>`.
   
   :param string title: The title of the pop-up
   :param string message: The message to display

.. js:function:: robi.notice(title, message)

   Create a notice growl message (the little pop-up in the upper right window corner)

   See also :js:func:`robi.error <robi.error>`, :js:func:`robi.warn <robi.warn>`, :js:func:`robi.message
   <robi.message>`.

   :param string title: The title of the pop-up
   :param string message: The message to display
   
.. js:function:: robi.message(title, message)

   Create a growl message (the little pop-up in the upper right window corner)

   See also :js:func:`robi.error <robi.error>`, :js:func:`robi.warn <robi.warn>`, :js:func:`robi.notice
   <robi.notice>`.

   :param string title: The title of the pop-up
   :param string message: The message to display

   
   
Private Methods
...............



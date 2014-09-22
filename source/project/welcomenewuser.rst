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


Welcome New User
================

This document should help you getting started with our project. We're glad you're with us. If you need help or if you
have questions, please do not hesitate to :doc:`drop us a line <connect>`.


Prepare yourself
----------------


1. Create a GitHub.com account
``````````````````````````````

You need a GitHub.com account to commit to the project. If you already have one, you can skip this step. Just make sure
that we know about your username.

Open `github.com <https://github.com/>`_ and you will see the registration form right on the front page. Make sure you
read the terms and conditions and sign up. Send us your new username, so we can add you to the list of collaborators for
the repositories you're going to contribute to.


2. Install Git Client Software
``````````````````````````````

Most Linuxes and Unixes have a Git client in their package repositories. So you might have to run one of the following
commands, depending on your operating system:

.. code:: bash

   apt-get install git           # Debian, Ubuntu
   yum install git               # CentOS
   zypper install git            # OpenSUSE

If you live in the Windows world, there is a nice all-in-one installer, that contains everything you need, including GUI
and command line tools, a SSH client and much more. Check out `git-scm.com <http://git-scm.com/download/win>`_ for
details.


3. Create a SSH key pair
````````````````````````

We strongly encourage developers to access our repositories via SSH. This has several pros and cons [#]_, but from a
developer perspective, the pros win, because GitHub allows anonymous access always via HTTPS.

Long story short: You need a key pair (a private and a public key). This is not the place to discuss facets of
authorization, authentication and encryption. If you already have such a key pair, you can skip this step.

Execute this command in a shell:

.. code:: bash

   ssh-keygen -b 8192

Almost every Linux and Unix have ``ssh-keygen`` preinstalled. Under Windows, the Git package above provides the tool.

You will see the following on your screen for a few seconds up to minutes...

.. code:: text

   Generating public/private rsa key pair.

... and a little later, you'll be ask to enter the filename to save the private key to. Default would be something like
``$HOME/.ssh/id_rsa`` or, under Windows, ``%USERPROFILE%\.ssh\id_rsa``.

.. code:: text

   Enter file in which to save the key (~/.ssh/id_rsa):

We recommend calling your file ``id_rsa_github`` and put it in the standard directories mentioned above.

You will be asked for a passphrase next. This passphrase will be needed each time you use your key. We encourage using a
passphrase, but it is not required. If you don't enter one, the key is unprotected and can be used anytime without prior
unlocking.

When you see such a picture...

.. code:: text

   00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff documentation@doc.lan
   The key's randomart image is:
   +--[ RSA 8192]----+
   |*            o.++|
   | +           o*E+|
   |  -.        .+=*.|
   |    =    .   +=+ |
   |        S     o..|
   |       o o     . |
   |          . . .  |
   |           . .   |
   |            .    |
   +-----------------+

... your key is ready to rumble.

.. [#] see `Git on the Server: The Protocols <http://git-scm.com/book/en/Git-on-the-Server-The-Protocols>`_


4. Add your public key to your GitHub account
`````````````````````````````````````````````

Open the `GitHub Settings/SSH Keys page <https://github.com/settings/ssh>`_ for your account. Click "Add SSH key" and
paste the contents of your ``id_rsa_github.pub`` file to the "key" field. The "title" field can be filled with some name
that helps you to identify the key.

.. warning:: Make sure you paste the contents of the ``.pub`` file of your key! The private key (in the file without the
             ``.pub`` ending) is really meant to be kept secret!

After you clicked the "Add key" button, you'll receive an e-mail that confirms the action.


5. Configure your SSH client
````````````````````````````

You can easily configure your SSH client to automatically use your key when you connect with GitHub. Go to your
``$HOME/.ssh`` (``%USERPROFILE%\.ssh`` under Windows) directory and create a file simply named ``config`` (if it does not
already exist). Put the following information in this file:

.. code:: text

   Host github.com
   User git
   IdentityFile ~/.ssh/id_rsa_github

So, each time, you connect to GitHub, SSH automatically uses your key.

.. note:: The username ``git`` is correct and must not be replaced with your GitHub username! You are identified by your
          key.


6. Setup basic Git configuration
````````````````````````````````

There are a few global settings that should be applied to your Git installation. Skip this step when you already did
that, but you can't destroy anything if you do it twice.

.. code:: bash

   git config --global user.name "Your Real Name"
   git config --global user.email your.mail@address.org

.. note:: The e-mail address should be the address you used to register with GitHub. If you want to use another one,
          you need to add this address to your GitHub account. This makes sure that your contributions are correctly
          associated with your account.

.. note:: Your real name and your e-mail address you enter here will be visible to anyone that takes a closer look
          at the contributions.


7. Clone the repositories
`````````````````````````

Now you have everything you need to get started and you can clone our repositories. Basically, you open a command line
at the directory you want to clone to and execute the following command:

.. code:: bash

   git clone git@github.com:arobito/arobito.git

For the documentation, use

.. code:: bash

   git clone git@github.com:arobito/arobito-docs.git

So, that's it!


8. Setup signing key (optional)
```````````````````````````````

If you do not know what we are talking about here, simply skip this step.

If you are familiar with the ideas of commit and tag signing via GPG, you may want to setup your GPG key. This can
be done globally for all repositories (ABCD1234 is your key ID)...

.. code:: bash

   git config --global user.signingkey ABCD1234

... or local to a specific clone:

.. code:: bash

   cd myclone
   git config user.signingkey ABCD1234

Refer to the `Tagging Section of the Pro Git e-book <http://git-scm.com/book/en/Git-Basics-Tagging>`_ for more
information on tag signing.

.. note:: It does not make sense to sign every commit. Basically, it would be enough to sign tags for releases. But
          currently, we have not established any rules on that.


Work with the code
------------------


Submodules
``````````

In the documentation repository, we're using a submodule under ``code/`` that contains a defined version of the code
from the main repository. This kind of decouples the documentation from the commits in the main repository.

When you clone the documentation repository for the first time, the directory ``code/`` is empty.


Checking out a submodule for the first time
...........................................

To get the code, simply execute the following command from the root directory of your documentation repository clone.

.. code:: bash

   git submodule update --init

This brings the ``code`` directory to the defined version.


Updating a submodule
....................

It may happen that you need to update the contents of the submodule to the current version from the main repository.
Simply go to the ``code`` directory and execute

.. code:: bash

   git pull origin master

The contents will be updated to the most current version. Change back to the root directory of the your documentation
repository clone and enter

.. code:: bash

   git commit

Now you can work with the new code base.

.. todo:: Detailed instructions


More stuff to read
------------------

To get familiar with Git, we recommend taking a look at the great `Pro Git e-book <http://git-scm.com/book/>`_, which is
available for free in several formats and as web page.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2014 The Arobito Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains our doc builder script.

This script is our temporary workaround for `issue #2 <https://github.com/arobito/arobito-docs/issues/2>`_ of our
documentation project.

It basically calls the same command we normally use ``sphinx-build -n -b html -d build/doctrees source build/html``, and
evaluates the output of the sphinx builder to ignore those warnings we can easily ignore.
"""

__license__ = 'Apache License V2.0'
__copyright__ = 'Copyright 2014 The Arobito Project'
__author__ = 'Jürgen Edelbluth'
__credits__ = ['Jürgen Edelbluth']
__maintainer__ = 'Jürgen Edelbluth'

import subprocess
import sys
import re


def main() -> int:
    """
    This method calls the Sphinx Builder on our documentation.

    After the run, it filters the warnings and removes those that can be ignored because of a known Sphinx bug. This
    allows us to let a build "fail" when there are other warnings.

    :return: The exit code of the documentation creation process.
    """
    with subprocess.Popen(['sphinx-build', '-n', '-b', 'html', '-d', '../build/doctrees', '../source', '../build/html'],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE) as build_proc:
        out_stdout, out_stderr = build_proc.communicate()
        return_code = build_proc.returncode

    if return_code != 0:
        print('==========================', file=sys.stderr)
        print('Documentation Build failed', file=sys.stderr)
        print('==========================', file=sys.stderr)
        print(file=sys.stderr)
        print('STDOUT', file=sys.stderr)
        print('------', file=sys.stderr)
        print('{:s}'.format(out_stdout.decode()), file=sys.stderr)
        print(file=sys.stderr)
        print('STDERR', file=sys.stderr)
        print('------', file=sys.stderr)
        print('{:s}'.format(out_stderr.decode()), file=sys.stderr)
        return return_code

    split = out_stderr.decode().split('\n')

    rule = re.compile('^.*WARNING:\spy:class\sreference\starget\snot\sfound:\s(builtins\.'
                      '(type|object)|unittest\.case\.TestCase)$', re.DOTALL | re.UNICODE)

    warnings = filter(lambda s: len(s.strip()) > 0 and not rule.match(s.strip()), split)
    warning_list = list()
    for w in warnings:
        warning_list.append(w.strip())

    if len(warning_list) > 0:
        print('==========================', file=sys.stderr)
        print('Documentation Build failed', file=sys.stderr)
        print('==========================', file=sys.stderr)
        print(file=sys.stderr)
        print('STDOUT', file=sys.stderr)
        print('------', file=sys.stderr)
        print('{:s}'.format(out_stdout.decode()), file=sys.stderr)
        print(file=sys.stderr)
        print('STDERR', file=sys.stderr)
        print('------', file=sys.stderr)
        print('{:s}'.format(out_stderr.decode()), file=sys.stderr)
        print(file=sys.stderr)
        print('NON IGNORABLE WARNINGS', file=sys.stderr)
        print('----------------------', file=sys.stderr)
        for w in warning_list:
            print(w, file=sys.stderr)
        return 1

    print('==============================', file=sys.stdout)
    print('Documentation Build Successful', file=sys.stdout)
    print('==============================', file=sys.stdout)
    print(file=sys.stdout)
    print('STDOUT', file=sys.stdout)
    print('------', file=sys.stdout)
    print('{:s}'.format(out_stdout.decode()), file=sys.stdout)
    print(file=sys.stdout)
    print('STDERR', file=sys.stdout)
    print('------', file=sys.stdout)
    print('{:s}'.format(out_stderr.decode()), file=sys.stdout)
    print(file=sys.stdout)
    return return_code


if __name__ == '__main__':
    sys.exit(main())


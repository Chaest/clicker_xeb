# -*- coding: utf-8 -*-

from ansiblelint import AnsibleLintRule

import re

class IndentationShouldBeTwoSpacesWide(AnsibleLintRule):
    '''
    STRA rule number 002

    Tests whether indentations used in the code are always two spaces wide or not.
    This module is simplified by only checking indentation length is a factor of two.
    Hence it does not handles cases such as four spaces wide indentation or any other factors of two.
    It is mostly intended to prevent cases such as follow:

    dict:
       threespaceswide:
    array:
     - onespacewide
     - elements
     - are evil

    '''
    id = 'STRA_002'
    shortdesc = 'Indentation should be two spaces wide.'
    description = shortdesc
    tags = ['tasks']

    def match(self, file, line):
        m = re.match('( *?)[^ ]+', line)
        if(m):
            return len(m.group(1)) % 2 != 0
        return False
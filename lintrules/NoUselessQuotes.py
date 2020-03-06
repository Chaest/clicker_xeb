# -*- coding: utf-8 -*-

from ansiblelint import AnsibleLintRule

import re

def is_number(v):
    '''
        Checks if the given value (v) will be interpreted as a number
        i.e. a valid number representation that does not start with a '0'
    '''
    try:
        float(v)
        if(len(v) > 0 and v[0] != '0'):
            return True
    except:
        return False
    return False

conditions_where_quotes_are_needed = [
    lambda s: ': ' in s,
    lambda s: ' #' in s,
    lambda s: len(s) > 0 and s[0] in u'[]{}>|*&!%#`@,?:-\'"',
    lambda s: s.lower() in ['yes', 'no', 'true', 'false'],
    is_number
]

class NoUselessQuotes(AnsibleLintRule):
    '''
    STRA rule number 001

    Tests whether useless quotes are used or not.
    '''
    id = 'STRA_001'
    shortdesc = 'A string should only be wrapped in quotes when needed to.'
    description = shortdesc
    tags = ['tasks']

    def needsQuotes(self):
        return any([condition(self.stringValue) for condition in conditions_where_quotes_are_needed])

    def init(self, line):
        '''
            Initialization function the determines the following information:
            * The current line is an entry (i.e. a key: value pair)
            * The current value is wrapped in quotes (i.e. "<value>" or '<value')           => hasQuotes
            * The actual unwrapped value (to determine whether it should be wrapped or not) => stringValue
        '''
        # Gets the left hand part of a yaml entry
        m = re.match('.+?: (.*)', line) 
        if(m):
            value = m.group(1)
            # Checks whether the value is wrapped in quotes
            tmp = re.match('[\'"](.*)[\'"]', value)
            self.hasQuotes = bool(tmp)
            if(self.hasQuotes):
                self.stringValue = tmp.group(1)
        else:
            self.hasQuotes = False

    def match(self, file, line):
        self.init(line)
        return self.hasQuotes and not self.needsQuotes()
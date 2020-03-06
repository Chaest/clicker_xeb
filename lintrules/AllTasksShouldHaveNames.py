# -*- coding: utf-8 -*-

from ansiblelint import AnsibleLintRule

class AllTasksShouldHaveNames(AnsibleLintRule):
    '''
    STRA rule number 003

    Tests whether all tasks are named or not. The default lint will omit debug tasks.
    This one will not.
    '''
    id = 'STRA_003'
    shortdesc = 'All tasks should have names'
    description = shortdesc
    tags = ['tasks']

    def matchtask(self, file, task):
        return task.get('name', '') == ''
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.utils.unsafe_proxy import AnsibleUnsafeText

PORT_MIN_VALUE = 0
PORT_MAX_VALUE = 65535

def is_port(value):
    '''
        Checks if the given value is a valid port
    '''
    try:
        if(str(value)[0] == '0'): return False
    except:
        pass
    try:
        int_value = int(value)
        return PORT_MIN_VALUE <= int_value <= PORT_MAX_VALUE
    except:
        return False

def is_path(value):
    '''
        Checks if the given value is a valid path
    '''
    try:
        if(str(value)[0] == '/'): return True
    except:
        return False
    return False


def is_param_list(value):
    '''
        Checks if the given value is a valid list of parameters
    '''
    def is_valid_param(param):
        return all([key in param for key in ['desc', 'name', 'type']])
    return type(value) == list and all([is_valid_param(param) for param in value])

class TestModule(object):
    '''
        Add jinja2 tests for specific types
    '''

    def tests(self):
        return {
            'secret': lambda v: type(v) in [AnsibleVaultEncryptedUnicode, AnsibleUnsafeText],
            'list':   lambda v: type(v) in [list],
            'bool':   lambda v: type(v) in [bool],
            'port':   is_port,
            'path':   is_path,
            'list_of_param': is_param_list
        }
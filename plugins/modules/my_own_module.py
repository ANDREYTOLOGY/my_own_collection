#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create file with content

version_added: "1.0.0"

description: Create a file on remote host with given content.

options:
    path:
        description: Path to the file
        required: true
        type: str
    content:
        description: Content of the file
        required: true
        type: str

author:
    - Andrey
'''

EXAMPLES = r'''
- name: Create file
  my_own_module:
    path: /tmp/test.txt
    content: "hello world"
'''

RETURN = r'''
path:
    description: File path
    type: str
    returned: always
content:
    description: File content
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import os


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path
    result['content'] = content

    if module.check_mode:
        module.exit_json(**result)

    if os.path.exists(path):
        with open(path, 'r') as f:
            if f.read() == content:
                module.exit_json(**result)

    try:
        with open(path, 'w') as f:
            f.write(content)
        result['changed'] = True
    except Exception as e:
        module.fail_json(msg=str(e), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()

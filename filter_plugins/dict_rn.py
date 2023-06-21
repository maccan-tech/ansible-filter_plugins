DOCUMENTATION = '''
	name: dict_rn
	short_description: Rename dictionary elements.
	version_added: 0.0.1
	author: Marcus Beckman
	description:
		- Rename dictionary elements.
'''
EXAMPLES = '''
- name: Rename dict element
  ansible.builtin.debug:
    msg: ->
    	{{ list | dict_rn('key', 'name') }}

  vars:
  	list:
  	  - key: a
  	  	value: 123
  	  - key: b
  	  	value: 456

  # Produces the following list of dictionaries:
  # {
  #   "name": "a"
  #	  "value": 123
  # },
  # {
  #   "name": "b"
  #	  "value": 456
  # }
'''
RETURN = '''
  _value:
    description: The renamed dict list
    type: list
    elements: dictionary
'''

from ansible.errors import AnsibleFilterError

def dict_rn(things, *terms):
	result = []

	if len(terms) < 2:
		raise AnsibleFilterError("Filter dict_rn needs index and new index as arguments.")

	index = terms[0]
	index_new = terms[1]

	for thing in things:
		thing[index_new]=thing.pop(index)
		result.append(thing)

	return result
		
class FilterModule(object):
	def filters(self):
		return { 'dict_rn': dict_rn }

# ansible-filter_plugins

## Filter dict_rn
Filter for renaming indexes in dictionary list.<br>
Example:
```yml
- name: Rename dict element
  ansible.builtin.debug:
    msg: "{{ list | dict_rn('key', 'name') }}"

  vars:
    list:
      - key: a
        value: 123
      - key: b
        value: 456

  # Produces the following list of dictionaries:
  # {
  #   "name": "a",
  #   "value": 123
  # },
  # {
  #   "name": "b",
  #   "value": 456
  # }
```

# Json Parser

Json Parser is a simple Python Library that allows parse Compilcated Nested Json tree to a Simple Json data.
This Library allows to convert Complicated Nested Json Data to a Intermediate Simple Json Data, which make it easier to process the orginal data.

### Example Data Conversion

```sh
########################## FROM #########################################
{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}

########################## TO #########################################
{
  'menu': {
   'path': 'menu',
   'isRoot': True,
   'children': ['menu/id', 'menu/value', 'menu/popup']
  },
  'menu/id': {
   'path': 'menu/id',
   'isRoot': False,
   'children': []
  },
            .
            .
            .
  'menu/popup/menuitem/2/value': {
   'path': 'menu/popup/menuitem/2/value',
   'isRoot': False,
   'children': []
  },
  'menu/popup/menuitem/2/onclick': {
   'path': 'menu/popup/menuitem/2/onclick',
   'isRoot': False,
   'children': []
  }
}
```

### Installation


```sh
$ pip3 install JsonJ
```

### Usage


```sh
from JsonJ import JsonJ
json = JsonJ(<sample_data>)
```

### Development

Want to contribute? Great!
All you have to do is a Pull Rrequest and start Working

### Todos

 - Search by node
 - Search by value
 - And a lot has to be done

License
----

MIT


**Free Software, Hell Yeah!**

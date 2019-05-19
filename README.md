# JSONJ

Json Parser is a simple Python Library that allows parsing Complicated Nested Json tree to a Simple Json data.
This Library allows converting Complicated Nested Json Data to an Intermediate Simple Json Data, which make it easier to process the original data.

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

###########################  TO #########################################
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

As you can see, this converted format is Elegant and can be Applied to a Various Task.

### Converted Data Format Description
```sh
            .
            .
            .
'menu/popup/menuitem/2/value': {
   'path': 'menu/popup/menuitem/2/value',
   'isRoot': False,
   'children': []
  },
            .
            .
            .
```

- The key of the data is set to be the path of that particular node from the root Node
- Each Key has a value which in turn is a simple Json with 3 parameters.
  - path: The path of the particular node from the root node (same as that of the key)
  - isRoot: Either it's a Root node or not
  - children: Wheather the particular node has any children or not 

### Installation


```sh
$ pip3 install JsonJ
```

### Usage


```sh
from JsonJ import JsonJ
json = JsonJ(<sample_json_data>)
```
NOTE: PLEASE MAKE SURE THE JSON DATA IS VALID, AS OF NOW THE LIBRARY DOES NOT CHECK WHETHER THE DATA IS VALID OR NOT, BUT THIS VALIDATION WILL BE DONE SOON
### Detailed Usage

```sh
- get_parsed_data() - This function call returns the Intermediate Parsed data
- clean() - This function call clears all the data saved in local variables
```


### Development

Want to contribute? Great!
All you have to do is a Pull Request and start Working

### Todo's

 - Search by node
 - Search by value
 - Json data validator
 - And a lot has to be done

License
----

MIT


**PEACE**

# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:48:29 2019

@author: Joish
"""

class JsonParser():
    
    # Constructor 
    def __init__(self,data):
        self.data = {}
        self.identity = 0
        self.identity2 = 0
        self.localIdentity = 0
        self.mpath = ''
        self.identityArray = []
        self.path = ""
        self.typeof = ""
        self.children = []
        self.isRoot = ''          
        self.temp = ""
        self.objects = [dict,list]
        self.objects2 = [str,int,bool]
        
        self.traverse(data)
        
    # function used to clear the saved variable data
    def clean(self):
      self.data = {}
      self.identity = 0
      self.identity2 = 0
      self.localIdentity = 0
      self.mpath = ''
      self.identityArray = []
      self.path = ""
      self.typeof = ""
      self.children = []
      self.isRoot = ''            
      self.temp = ""
      
    # function responsible for getting the childrens with respect to that that node
    def get_childrens(self, data, path):
        self.children = []

        for key in data:
            self.children.append(self.path + '/' + str(key))
        
        return self.children   
     
    # part of a recursive function to create the required data
    def process(self, key, value):
        if (value == None or type(value) in self.objects2) :
            self.path = self.identityArray[self.identity2 - 1] + '/' + str(key)
#            self.typeof = 'file'
            self.isRoot = True if self.identity == 0 else False
            self.children = []
            self.data[self.path] = {
                'path': self.path,
#                'type': self.typeof,
                'isRoot': self.isRoot,
                'children': self.children,
            }
        
        else:
            self.path = str(key) if self.identity == 0 else self.mpath + '/' + str(key)
#            self.typeof = 'folder'
            self.isRoot = True if self.identity == 0 else False
            self.children = self.get_childrens(value, self.path)
            self.data[self.path] = {
                'path': self.path,
#                'type': self.typeof,
                'isRoot': self.isRoot,
                'children': self.children,
    
            }
    
            self.mpath = str(key) if self.identity == 0 else self.mpath + '/' + str(key)
            self.identityArray.append(self.mpath) 
    
            self.identity += 1
            self.identity2 += 1
       
    # recursive function to go through all the nodes of a JSON tree
    def traverse(self, o):
        if (type(o) == list):
            for key, val in enumerate(o):
                if type(val) in self.objects:
                    self.process(key, val)
                else:
                    self.process(val, val)
                
                if (val != None and type(val) in self.objects):
                    self.traverse(val)
        else:
            for key in o:
                self.process(key, o[key])
                
                if (o[key] != None and type(o[key]) in self.objects):
                    self.traverse(o[key])
                    
        self.localIdentity = self.identity
        self.identity -= 1
        self.identity2 += 1

        self.temp = self.identityArray[len(self.identityArray) - 1].split('/')
        
        if (len(self.temp) > 1):
            self.temp.pop()
            self.temp = "/".join(self.temp)
            self.identityArray.append(self.temp)
            self.mpath = self.temp;
            
    # function to return parsed data - RESULT
    def get_parsed_data(self):
        return self.data
        


# sample = {
#     "glossary": {
#         "title": "example glossary",
# 		"GlossDiv": {
#             "title": "S",
# 			"GlossList": {
#                 "GlossEntry": {
#                     "ID": "SGML",
# 					"SortAs": "SGML",
# 					"GlossTerm": "Standard Generalized Markup Language",
# 					"Acronym": "SGML",
# 					"Abbrev": "ISO 8879:1986",
# 					"GlossDef": {
#                         "para": "A meta-markup language, used to create markup languages such as DocBook.",
# 						"GlossSeeAlso": [{'a':1234}, "XML"]
#                     },
# 					"GlossSee": "markup"
#                 }
#             }
#         }
#     }
# }

# js = JsonParser(sample)
# js.get_parsed_data()
# js.clear()
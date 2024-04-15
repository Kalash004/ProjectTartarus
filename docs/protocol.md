# Protocol Project Tartarus

Protocol for communication with core database app

# How it works

* Step 1: [Send request](#send-request) as [structure](#request-structure) below
* Step 2: Obtain response (Error message/ Done/ Data objects requested)

## Send request

This section is about your request for the application

### Request structure

* API KEY; - `must have` <br>
* REQUEST TYPE; - `must have`<br>
* TABLE - `must have`; <br>
* DATA <br>
* PARAMETERS <br>

### API KEY

Given from administrator. Its needed for verification.

### REQUEST TYPE

* GET - returns back data depending on parameters
* POST - inserts data into the database depending on the data **Must have DATA in request**
* DELETE - deletes data from the database depending on the data **Must have DATA in the request**
* UPDATE - updates data in the database depending on the data **Must have DATA in request**

### Parameters for each request type

#### _GET_

* attribute_name=value <br>
  **Example**:
  NAME=ANTON <br>

<u>**If you dont add any parameters** returns all the data from the database</u>

#### _POST_

--

#### _DELETE_

--

#### _UPDATE_

--

### DATA

* Data in JSON format

```JSON
[
  {
    "id": 1,
    "name": "Anton"
  },
  {
    "id": 2,
    "name": "Notna"
  }
]
```

## Example

### Get an object from the table

APIKEY=apitestkey1;EVENT=GET;TABLE=USERS;PARAMETERS=(NAME=ANTON)
APIKEY=apitestkey1;EVENT=GET;TABLE=USERS;PARAMETERS=(ID=1)

### Insert and object to the table

APIKEY=apitestkey1;EVENT=POST;TABLE=USERS;DATA=[{user_id:1,name:Anton},{user_id:2,name:Notna}]

## Supported Parameter Opperators

'='

# Response

STATUS=`value`;DATA=`[{'table':'users','user_id':1,'name':'Anton'},{'user_id':2,'name':'Anton'}]`;

## Possible status

```
Success - 1
Exception starts - 2
Client exceptions - 23
Service exceptions - 24
Unknown exception - 22
```


# testing
post <br>
APIKEY=apitestkey1;EVENT=POST;TABLE=admin_users;DATA=[{admin_id:none,name:Denis,surename:Kalashnikov,password:test}] `works`

get <br>
no params <br>
APIKEY=apitestkey1;EVENT=GET;TABLE=admin_users; `works`

with params <br>
APIKEY=apitestkey1;EVENT=GET;TABLE=admin_users;PARAMETERS=(NAME=Anton) `works`
APIKEY=apitestkey1;EVENT=GET;TABLE=admin_users;PARAMETERS=(NAME=Anton,ID=4)
APIKEY=apitestkey1;EVENT=GET;TABLE=admin_users;PARAMETERS=(NAME=Anton,admin_id=4)


update
APIKEY=apitestkey1;EVENT=UPDATE;TABLE=admin_users;DATA=[{admin_id:5,name:Someone,surename:Kalashnikov,password:newpas}]       `Works`


delete 

APIKEY=apitestkey1;EVENT=DELETE;TABLE=admin_users;PARAMETERS=(ID=8)  `Works`

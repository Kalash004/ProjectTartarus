# Protocol Project Tartarus

Protocol for communication with core database app

# How it works

* Step 1: Send message as [structure](#structure) below
* Step 2: Sends response (Error message/ Done/ Data objects requested)

## Structure

* API KEY; <br>
* REQUEST TYPE; <br>
* TABLE; <br>
* (DATA) <br>

### API KEY

Given from administrator. Its needed for verification.

### REQUEST TYPE

* GET - returns back data depending on parameters
* POST - inserts data into the database depending on the parameters
* DELETE - deletes data from the database depending on the parameters
* UPDATE - updates data in the database depending on parameters

## Parameters

### GET

* table.attribute_name=value <br>
**Example**
USERS.NAME=ANTON <br>

<u>**No parameters** return all the data from the database</u>

### POST

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

APIKEY=apitestkey1;EVENT=GET;TABLE=USERS;PARAMETERS=(NAME=ANTON,TOP=1)

### Insert and object to the table

APIKEY=abcdapikey123;EVENT=POST;TABLE=USERS;DATA=[{id:1,name:Anton},{id:2,name:Notna}]

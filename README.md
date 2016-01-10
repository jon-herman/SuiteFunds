# SuiteFunds

To run the app, cd into flaskapp and activate the virtual environment:

$ . bin/activate



To create the server and run the app:

$ cd app

$ python app.py

Then point the browser to:
http://127.0.0.1:5000/

The input should be a list in the form "[name] [price]".  It is designed to accept a table copied from an Excel spreadsheet

To close the server:

$ CTRL+C


To close the virtual environment:

$ deactivate

Currently the app is hardcoded with my suite's members, to generalize, delete the hardcoded funds dictionary and uncomment the commented-out lines in the getFunds method.  (The purpose of hardcoding was to ensure that people who made no payments are still included.) 

Additionally, for large sums of money, remove the round() call in getFunds for a more precise evaluation.

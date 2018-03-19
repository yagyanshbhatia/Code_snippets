Picard website has to retrieve data from the manifest file and check if its in correct format, and check the validity of PLUGIN_ZIP_URL

for that I am planning to use `urllib` library of python.

this is a very very naive implementation of the same.
Given script retrieves the json response from the manifest (hosted in this repository only), and stores in a.txt given

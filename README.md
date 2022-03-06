# Python Script to Test GitHub API
A simple script to test the public user API on GitHub.
## Getting started

### Overview
The test will use a GET request to check the headers and response body of the `/users/{user_id}` endpoint of the GitHub API for the `user_id` \'6wl\'. 

Note that for the sake of the completeness of the task, the counts of the public repos, gists, followers, and following were tested for, but as they are subject to change, writing tests for these cases might be an antipattern.



#### Installing Libraries
For accessing the GitHub API we\'ll need to make HTTP requests, so will need to install the Python requests library. To do this run the following command:

`$ python3 -m pip install requests`

## Running the test
To run this test we can use the following command in the terminal:

`$ pytest`

This will test **all** your files in the specified directory that start with \"test\". Or, to just test the current file, we can simply run pytest with the path to the file:

`$ pytest tests/test_GitHub.py`

At the moment, both of these will have the same result, as there's only one Python file present in the repo.

## Authors
- Rebecca McJarrow - Main Author - [REMcJarrow](https://github.com/REMcJarrow "REMcJarrow")



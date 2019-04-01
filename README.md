# Checkr QA Automation exercise (take-home)


## Scenario

A developer in your company wrote a program called `search_directory.py`, and asked you 
to write functional tests for it.

The `search_directory` program is supposed to list all files that match a query inside a given directory, eg:

    $ ./search_directory.py /home/candidate/documents report
    /home/candidate/documents/daily.txt
    /home/candidate/documents/work/2017/summary_report.txt

The behavior of the `search_directory` program is described in the `search_directory.html`.


## Task

Write functional tests to verify if the binary `search_directory` meets the behavior described in its help documentation. Use a test framework *of your choice* (eg, JUnit, Pytest, RSpec). 

You should write as many tests as you feel necessary to cover the behavior described in the help documentation.


## Assumptions

The program `search_directory` is a bug free implementation of the specification.

# sortinghat
## Probelm Statement
- Implement SortingHat: A school hostel assignment Program
- New students join a school and need to be assigned to one of 4 boarding houses. As students come in,
  they registertheirroll number, class & food preference. There are 2 classes - A and B, and two food
  preferences - V & NV. There are 4 boarding houses with equal but limited capacity. 
  
  The hat follows a first in first out policy with the following rules -
    - Queue will be processed based on the time a studentregistered, first in first out
    - Boarding houses for students who prefer V cannot board NV students
    - Boarding houses for class A would be separate from boarding houses for class B
    - Once all boarding houses are filled up to capacity, no more students can be allocated.

  Otherrules
    - Roll numberis a 4 digit integer unique to each student
    - Student can only be registered once, duplicate commands for same student may be ignored

The following is an example of input:

init 12

reg 1 B V

reg 2 A V

reg 3 A V

reg 4 B NV

reg 5 B V

reg 6 A NV

reg 7 A V

reg 8 A NV

reg 9 B NV

reg 10 B V

reg 11 A NV

reg 12 B NV

fin

should produce the following output (in any order) -

BV : [1,5,10]

AV : [2,3,7]

BNV : [4,9,12]

ANV : [6,8,11]

NA : []

## Folder Structure
- **SortingHat** is the main class which accepts the data from the user
- **DataProcessing** is the class which takes care of data cleaning and verification of given data
- **TestSortingHat** under tests folder contains the testcases for the testing the given secanrio 
## Basic Commands
- Install pytest by running the following command **"pip install -r requirements.txt "**
- **pytest test_sortinghat.py -v** = the command will execute the tests only from file tests/test_sortinghat.py.
   

<img height="120px" src="img/Thing1Thing2.jpg" />

# String1 and String2
For this assignment, you'll be coding some string manipulation functions within the `string1.py` and `string2.py` files.

There is some light dependency on knowing how [functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) work in python in terms of argument passing and return values, but you should be able to figure it out as you go.

## Instructions
Complete all of the functions in `string1.py` and `string2.py` based on your knowledge of Python strings, indexing, slicing, and methods. Make sure all the included tests are passing before submitting your work.

Run the programs from the command line like this:
```console
$ python string1.py
```

Here is a sample output. You can see that for the `donuts()` function, some tests are passing, others are failing.
```
$ python string1.py
donuts
 OK  got: 'Number of donuts: 4' expected: 'Number of donuts: 4'
 OK  got: 'Number of donuts: 9' expected: 'Number of donuts: 9'
  X  got: 'Number of donuts: 10' expected: 'Number of donuts: many'
 OK  got: 'Number of donuts: many' expected: 'Number of donuts: many'
()
both_ends
  X  got: None expected: 'spng'
  X  got: None expected: 'Helo'
  X  got: None expected: ''
  X  got: None expected: 'xyyz'
()
fix_start
  X  got: None expected: 'ba**le'
  X  got: None expected: 'a*rdv*rk'
  X  got: None expected: 'goo*le'
  X  got: None expected: 'donut'
()
mix_up
  X  got: None expected: 'pox mid'
  X  got: None expected: 'dig donner'
  X  got: None expected: 'spash gnort'
  X  got: None expected: 'fizzy perm'
```

## Testing with Unittest
This assignment also has separate unit tests to help you during development. The unit tests are located in the `tests` folder; you should not modify these.  Make sure all unit tests are passing before you submit your solution. You can invoke the unit tests from the command line at the root of your project folder:
```console
$ python -m unittest discover tests
```
You can also run these same tests using the `Test Explorer` extension built in to the VSCode editor, by enabling automatic test discovery.  This is a really useful tool and we highly recommend to learn it.

https://code.visualstudio.com/docs/python/testing#_test-discovery

- Test framework is `unittest`
- Test folder pattern is `tests`
- Test name pattern is `test*`

## Submitting your work
To submit your solution for grading, you will need to create a github [Pull Request (PR)](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).  Refer to the `PR Workflow` article in your course content for details.

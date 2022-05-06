# 42_push_swap_tester
Tester for 42 push_swap project.


Make, run Norminette and test folowing the correction checklist

To run the tester:
```
python3 tester_push_swap.py
```
or 
```
chmod +x tester_push_swap.py
./tester_push_swap.py
```

Available arguments:

````
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     specify the push_swap directory (not work with -g) (default: ../)
  -e, --extended_test   run tests with a range (min int, max int) (default: False)
  -g GIT_URL, --git_url GIT_URL
                        takes your git_url and clones the repository and then runs the tests (default: )
  -l LEN, --len LEN     run a single test with the given len (default: None)
  -n N_ITER, --n_iter N_ITER
                        specify the number of iterations to test the 100 and 500 sets (default: 10)
  -v, --verbose         print the list of numbers used for the test (default: False)
  --test TEST           allows you to do a specific test (a = all, e = error, i = identity, s = simple, o = 100, f = 500) (default: a)
  --skip                skip the norme and Makefile (default: False)
````

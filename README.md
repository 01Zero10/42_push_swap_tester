# 42_push_swap_tester
Tester for 42 push_swap project.


Make, run Norminette and test folowing the correction checklist

For run:
```
python3 tester_push_swap.py
```
or 
```
chmod +x tester_push_swap.py
./tester_push_swap.py
```

arguments:

````
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     Push_swap directory (not work with -g) (default: ../)
  -e, --extended_test   Run test with range(min max) int (default: False)
  -g GIT_URL, --git_url GIT_URL
                        Take git_url and clone the repository, then run test (default: )
  -l LEN, --len LEN     run a single test with the given len (default: None)
  -n N_ITER, --n_iter N_ITER
                        Number of iteration for 100, 500 test (default: 10)
  -v, --verbose         Print number list (default: False)
  --test TEST           Select test (a = all, e = error, i = identity, s = simple, o = 100, f = 500) (default: a)
  --skip                Skip norminette and make (default: False)

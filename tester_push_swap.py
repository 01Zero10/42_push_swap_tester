#!/usr/local/bin/python3
import math
import random
import os
import argparse
from time import sleep


class Bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def create_parser():
	arg_parser = argparse.ArgumentParser(description='Push Swap Tester',
										 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	arg_parser.add_argument('-b', '--bonus', action='store_true', default=False, help='Test the checker')
	arg_parser.add_argument('-d', '--dir', type=str, default='../', help='Push_swap directory (not work with -g)')
	arg_parser.add_argument('-e', '--extended_test', action='store_true', default=False,
							help='Run test with range(min max) int')
	arg_parser.add_argument('-g', '--git_url', type=str, default='',
							help='Take git_url and clone the repository, then run test')
	arg_parser.add_argument('-l', '--len', type=int,
							help='run a single test with the given len', default=None)
	arg_parser.add_argument('-n', '--n_iter', type=int, default=10, help='Number of iteration for 100, 500 test')
	arg_parser.add_argument('-v', '--verbose', action='store_true', default=False,
							help='Print number list')
	#arg_parser.add_argument('-s', '--save', action='store_true', default=False, help='Save number list for each iteration in number.txt')
	#arg_parser.add_argument('-)
	
	return arg_parser


def rd_nm(n: int, ext_test):
	lst = []
	while len(lst) != n:
		if not ext_test:
			x = str(random.randint(-50000, 50000))
		else:
			x = random.randint(-2147483648, 2147483647)
		if x not in lst:
			lst.append(x)
	# for element in lst:
	#	lst[lst.index(element)] = str(element)
	return lst


def create_str(lst: list):
	random.shuffle(lst)
	b = " ".join(lst)
	return b


def control_checker(ck_res):
	if ck_res == "OK\n":
		print(f"{Bcolors.OKGREEN}{ck_res}{Bcolors.ENDC}")
	else:
		print(f"{Bcolors.FAIL}{ck_res}{Bcolors.ENDC}")


def point_control(n_ele, wc_out):
	if int(n_ele) == 3:
		if int(wc_out) == 2 or int(wc_out) == 3:
			print(f"{Bcolors.OKGREEN}{wc_out}/3{Bcolors.ENDC}")
		else:
			print(f"{Bcolors.FAIL}{wc_out}/3{Bcolors.ENDC}")
	elif int(n_ele) == 5:
		if 12 >= int(wc_out) > 0:
			print(f"{Bcolors.OKGREEN}{wc_out}/12{Bcolors.ENDC}")
		else:
			print(f"{Bcolors.FAIL}{wc_out}/12{Bcolors.ENDC}")
	elif int(n_ele) == 100:
		if 700 > int(wc_out) > 0:
			print(f"{Bcolors.OKGREEN}{wc_out}/1500{Bcolors.ENDC}")
		elif 700 <= int(wc_out) < 900:
			print(f"{Bcolors.WARNING}{wc_out}/1500{Bcolors.ENDC}")
		elif 900 <= int(wc_out) < 1100:
			print(f"{Bcolors.WARNING}{wc_out}/1500{Bcolors.ENDC}")
		elif 1100 <= int(wc_out) < 1300:
			print(f"{Bcolors.WARNING}{wc_out}/1500{Bcolors.ENDC}")
		elif 1300 <= int(wc_out) < 1500:
			print(f"{Bcolors.WARNING}{wc_out}/1500{Bcolors.ENDC}")
		else:
			print(f"{Bcolors.FAIL}{wc_out}/1500{Bcolors.ENDC}")
	elif int(n_ele) == 500:
		if 5500 > int(wc_out) > 0:
			print(f"{Bcolors.OKGREEN}{wc_out}/11500{Bcolors.ENDC}")
		elif 5500 <= int(wc_out) < 7000:
			print(f"{Bcolors.WARNING}{wc_out}/11500{Bcolors.ENDC}")
		elif 7000 <= int(wc_out) < 8500:
			print(f"{Bcolors.WARNING}{wc_out}/11500{Bcolors.ENDC}")
		elif 8500 <= int(wc_out) < 10000:
			print(f"{Bcolors.WARNING}{wc_out}/11500{Bcolors.ENDC}")
		elif 10000 <= int(wc_out) < 11500:
			print(f"{Bcolors.WARNING}{wc_out}/11500{Bcolors.ENDC}")
		else:
			print(f"{Bcolors.FAIL}{wc_out}/11500{Bcolors.ENDC}")
	else:
		print(f"{Bcolors.HEADER}{wc_out}{Bcolors.ENDC}")


def run_test(n: int, arg):
	for i in range(0, arg.n_iter):
		n_str = create_str(rd_nm(n, arg.extended_test))
		print(f"{Bcolors.BOLD}{Bcolors.OKBLUE}test n{i + 1}{Bcolors.ENDC}")
		if arg.verbose == 1:
			print(f"{Bcolors.BOLD} number list:{Bcolors.ENDC}\n{n_str}\n")
		print(Bcolors.BOLD +
			  Bcolors.OKCYAN + "./push_swap {str} | wc -l {str}: "
			  + Bcolors.ENDC, end="")
		a = os.popen(f"./push_swap {n_str} | wc -l").read()
		point_control(n, a)
		print(Bcolors.BOLD +
			  Bcolors.OKCYAN + "./push_swap {str} | ./checker_Mac {str}: "
			  + Bcolors.ENDC, end="")
		b = os.popen(f"./push_swap {n_str} | ./checker_Mac {n_str}").read()
		if b == "OK\n":
			print(f"{Bcolors.OKGREEN}{b}{Bcolors.ENDC}")
		else:
			print(f"{Bcolors.FAIL}{b}{Bcolors.ENDC}")
		sleep(1)


def clone(git_url: str):
	print(f"{Bcolors.FAIL}{Bcolors.BOLD}Cloning repository{Bcolors.ENDC}")
	os.system(f"git clone {git_url} push_cor")
	os.chdir("push_cor")


def prepare():
	print(f"{Bcolors.FAIL}{Bcolors.BOLD}Running Norminette{Bcolors.ENDC}")
	os.system("norminette")
	sleep(2)
	print(f"{Bcolors.FAIL}{Bcolors.BOLD}Running make{Bcolors.ENDC}")
	sleep(1)
	os.system("make")


def check_error_management(res):
	if not res or res == "Error\n":
		print(f"{Bcolors.OKGREEN}OK{Bcolors.ENDC}")
	else:
		print(f"{Bcolors.FAIL}KO{Bcolors.ENDC}")


def error_management(name):
	print(f"{Bcolors.FAIL}{Bcolors.BOLD}Running Error management test{Bcolors.ENDC}\t")
	sleep(2)
	print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}Running ./push_swap 1 5 sei 0{Bcolors.ENDC}\t", end="")
	res = os.popen(f"./{name} 1 5 sei 0").read()
	check_error_management(res)
	sleep(2)
	print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}Running ./push_swap 1 5 1 0{Bcolors.ENDC}\t", end="")
	res = os.popen(f"./{name} 1 5 1 0").read()
	check_error_management(res)
	sleep(2)
	print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}Running ./push_swap 1 5 0 2147483649{Bcolors.ENDC}\t", end="")
	res = os.popen(f"./{name} 1 5 0 2147483649").read()
	check_error_management(res)
	sleep(2)
	print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}Running ./push_swap{Bcolors.ENDC}\t", end="")
	res = os.popen(f"./{name}").read()
	check_error_management(res)
	sleep(2)


def check_identity_test(res):
	if not res:
		print(f"{Bcolors.OKGREEN}OK{Bcolors.ENDC}")
	else:
		print(f"{Bcolors.FAIL}KO{Bcolors.ENDC}")


def identity_test(name):
	print(f"{Bcolors.FAIL}{Bcolors.BOLD}Running Identity test{Bcolors.ENDC}")
	sleep(2)
	print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}Running ./push_swap 42{Bcolors.ENDC}\t", end="")
	res = os.popen(f"./{name} 42").read()
	check_identity_test(res)
	sleep(2)
	print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}Running ./push_swap 0 1 2 3{Bcolors.ENDC}\t", end="")
	res = os.popen(f"./{name} 0 1 2 3").read()
	check_identity_test(res)
	sleep(2)
	print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}Running ./push_swap 0 1 2 3 4 5 6 7 8 9{Bcolors.ENDC}\t", end="")
	res = os.popen(f"./{name} 0 1 2 3 4 5 6 7 8 9").read()
	check_identity_test(res)
	sleep(2)


def simple_version(name, checker, arg):
	while not checker:
		input(f"{Bcolors.HEADER}{Bcolors.BOLD}Download the checker_Mac and press enter:{Bcolors.ENDC}")
		if "checker_Mac" in os.listdir():
			checker = 1
	print(f"{Bcolors.HEADER}{Bcolors.BOLD}Running Simple version test{Bcolors.ENDC}")
	sleep(2)
	print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}Running ./push_swap 2 1 0 | ./checker_Mac 2 1 0{Bcolors.ENDC}", end="")
	os.popen(f"./{name} 2 1 0 | ./checker_Mac 2 1 0").read()
	sleep(2)
	print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}Running ./push_swap 1 5 2 4 3 | wc -l: {Bcolors.ENDC}", end="")
	res = os.popen(f"./{name} 1 2 5 4 3 | wc -l").read()
	point_control(5, res)
	print(f"{Bcolors.OKBLUE}{Bcolors.BOLD}Running ./push_swap 1 5 2 4 3 | ./checker_Mac 1 5 2 4 3:{Bcolors.ENDC}",
		  end="")
	res = os.popen(f"./{name} 1 5 2 4 3 | ./checker_Mac 1 5 2 4 3").read()
	control_checker(res)
	sleep(2)
	run_test(5, arg)


def test_push(arg):
	name = "push_swap"
	checker = 0
	prepare()
	if name not in os.listdir():
		print(f"{Bcolors.FAIL}{Bcolors.BOLD}ERROR{Bcolors.ENDC}")
		exit()
	print(f"{Bcolors.HEADER}{Bcolors.BOLD}Download checker{Bcolors.ENDC}")
	if "checker_Mac" not in os.listdir():
		os.popen(
			"curl https://projects.intra.42.fr/uploads/document/document/8245/checker_Mac -o checker_Mac && chmod +x "
			"checker_Mac")
		if "checker_Mac" not in os.listdir():
			print(f"{Bcolors.FAIL}{Bcolors.BOLD}Unable to download checker_Mac{Bcolors.ENDC}")
		else:
			checker = 1
	else:
		checker = 1
	error_management(name)
	identity_test(name)
	simple_version(name, checker, arg)
	print(f"{Bcolors.HEADER}{Bcolors.BOLD}Running Middle version test{Bcolors.ENDC}")
	run_test(100, arg)
	sleep(2)
	print(f"{Bcolors.HEADER}{Bcolors.BOLD}Running Advanced version test{Bcolors.ENDC}")
	run_test(500, arg)
	sleep(2)


'''	arg_parser = argparse.ArgumentParser(description='Push Swap Tester',
										 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	arg_parser.add_argument('-v', '--verbose', action='count', default=0)
	arg_parser.add_argument('-g', '--git_url', type=str, default='',
							help='Take git_url and clone the repository, then run test')
	arg_parser.add_argument('-e', '--extended_test', action='store_true', default=False,
							help='Run test with range(min max) int')
	arg_parser.add_argument('-s', '--stack_len', type=int,
							help='run a single test with the given len', default=None)
	arg_parser.add_argument('-b', '--bonus', action='store_true', default=False, help='Test the checker')
	return arg_parser'''


def main():
	arg = create_parser().parse_args()
	if arg.git_url:
		arg.dir = ''
		clone(arg.git_url)
		if not arg.len:
			test_push(arg)
		else:
			print('NOT IMPLEMENTED')
	else:
		if arg.dir:
			os.chdir(arg.dir)
		if not arg.len:
			test_push(arg)
		else:
			print('NOT IMPLEMENTED')


if __name__ == "__main__":
	main()

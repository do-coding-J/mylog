master_clean : clean_blah clean_blah2 clean_some_files clean_targets clean_thing clean_all clean_static

# example 1 : echo
echo_hello :
	echo "Hello, World"

# example 2 : echo 2
echo_hello2:
	echo "Hello, World"
	echo "This line will print if the file hello does not exist."

# example 3 : compile .c file

# uptodate does not fix output even blah.c fixed
blah_uptodate:
	cc blah.c -o blah

# make as prerequisite and build from beginning
blah_resolved: blah.c
	cc blah.c -o blah

clean_blah :
	rm -rf blah

# example 4 : make from dependencies 
blah2 : blah2.o 				# run last
	cc blah2.o -o blah2

blah2.o : blah2.c				# run second
	cc -c blah2.c -o blah2.o

blah2.c : 						# run first
	echo "int main() {return 0;}" > blah2.c

clean_blah2:
	rm -rf blah2.o blah2

# example 5 : variables 
files := file1 file2
some_files : ${files}
	echo "Look at this variable: " ${files}
	touch some_file

file1 :
	touch file1

file2 :
	touch file2

clean_some_files :
	rm -rf file1 file2 some_file


# examples 6 : all target
target_all : target_one target_two target_three

target_one :
	touch target_one

target_two :
	touch target_two

target_three :
	touch target_three

clean_targets :
	rm -rf target_one target_two target_three

# multiple targets : target can be multiple
multiple_all : multiple_one multiple_two

multiple_one multiple_two :
	echo $@

# example 7 : wildcards
print : $(wildcard *.c)
	ls -la $?

thing_wrong := *.o # Don't do this! '*' will not get expanded
thing_right := $(wildcard *.o)

thing_all: thing_one thing_two thing_three thing_four

# Fails, because $(thing_wrong) is the string "*.o"
thing_one: $(thing_wrong)

# Stays as *.o if there are no files that match this pattern :(
thing_two: *.o 

# Works as you would expect! In this case, it does nothing.
thing_three: $(thing_right)

# Same as rule three
thing_four: $(wildcard *.o)

clean_thing:
	rm -rf *.o

# example 8 : automatic patterns
hey_all: all_one all_two
	# Outputs "hey", since this is the target name
	echo $@

	# Outputs all prerequisites newer than the target
	echo $?

	# Outputs all prerequisites
	echo $^

	# Outputs the first prerequisite
	echo $<

	touch hey_all

all_one:
	touch all_one

all_two:
	touch all_two

clean_all:
	rm -rf hey_all all_one all_two


# example 9 : Fancy rules
CC = gcc
CLAGS = -g

# example 9-1 static patterns
objects = foo.o bar.o all.o
static_all : $(objects)
	$(CC) $^ -o all

${objects} : %.o: %.c
	$(CC) -c $^ -o $@

all.c : 
	echo "int main() {return 0;}" > all.c

%.c :
	touch $@

clean_static :
	rm -rf *.c *.o all

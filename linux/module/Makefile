SOURCE := $(wildcard *.c)
CC := gcc
CFLAGS :=
CPPFLAGS := 

all : %.o

%.o : ${SOURCE}
	$(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@
	echo $<

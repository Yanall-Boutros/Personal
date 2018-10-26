#------------------------------------------------------------------------------
#  Makefile for CMPS 101 Programming Assignment 5
#
#  make                     makes pe3
#  make GraphClient         makes GraphClient
#  make clean               removes binaries
#  make checkFind           tests pe3 for memory leaks on in3
#  make checkClient         tests GraphClient for memory leaks
#------------------------------------------------------------------------------

BASE_SOURCES   = pe3.c List.c
BASE_OBJECTS   = pe3.o List.o
HEADERS        = List.h
COMPILE        = gcc -c -std=c99 -Wall
LINK           = gcc -o
REMOVE         = rm -f
MEMCHECK       = valgrind --leak-check=full

pe3 : $(BASE_OBJECTS)
	$(LINK) pe3 $(BASE_OBJECTS) -lm

pe3.o : pe3.c $(HEADERS)
	$(COMPILE) pe3.c

$(BASE_OBJECTS) : $(BASE_SOURCES) $(HEADERS)
	$(COMPILE) $(BASE_SOURCES)

clean :
	$(REMOVE) pe3 $(BASE_OBJECTS)

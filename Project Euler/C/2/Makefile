#------------------------------------------------------------------------------
#  Makefile for CMPS 101 Programming Assignment 5
#
#  make                     makes pe2
#  make GraphClient         makes GraphClient
#  make clean               removes binaries
#  make checkFind           tests pe2 for memory leaks on in3
#  make checkClient         tests GraphClient for memory leaks
#------------------------------------------------------------------------------

BASE_SOURCES   = pe2.c List.c
BASE_OBJECTS   = pe2.o List.o
HEADERS        = List.h
COMPILE        = gcc -c -std=c99 -Wall -lm
LINK           = gcc -o
REMOVE         = rm -f
MEMCHECK       = valgrind --leak-check=full

pe2 : $(BASE_OBJECTS)
	$(LINK) pe2 $(BASE_OBJECTS)

pe2.o : pe2.c $(HEADERS)
	$(COMPILE) pe2.c

$(BASE_OBJECTS) : $(BASE_SOURCES) $(HEADERS)
	$(COMPILE) $(BASE_SOURCES)

clean :
	$(REMOVE) pe2 $(BASE_OBJECTS)

checkFind : pe2
	$(MEMCHECK) pe2 in3 junk3

checkClient : GraphClient
	$(MEMCHECK) GraphClient

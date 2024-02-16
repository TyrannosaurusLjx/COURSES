Objfiles = $(wildcard *.cpp)
test : $(Objfiles)
	g++ -o test $(Objfiles)

run :
	./test

.PHONY : clean all

clean :
	rm -f *.o

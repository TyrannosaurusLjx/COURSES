# Makefile for C++ and LaTeX

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++11
LATEX = xelatex

# Executables
EXECUTABLE = test

# Targets
all: $(EXECUTABLE)

$(EXECUTABLE): TestTree.cpp
	$(CXX) $(CXXFLAGS) TestTree.cpp -Wno-dangling-else -o $(EXECUTABLE)

report.pdf: report.tex
	$(LATEX) report.tex

report: report.pdf

clean:
	rm -f $(EXECUTABLE)
	rm -f *.aux *.log *.out *.pdf *.synctex.gz

.PHONY: all clean report

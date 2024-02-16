TEX_FILES := $(filter-out muban.tex,$(wildcard *.tex))

# Generate PDF files from the .tex files
PDF_FILES := $(patsubst %.tex,%.pdf,$(TEX_FILES))

.PHONY: all clean

all: $(PDF_FILES)

%.pdf: %.tex
	xelatex $<

clean:
	rm -f *.aux *.log *.out

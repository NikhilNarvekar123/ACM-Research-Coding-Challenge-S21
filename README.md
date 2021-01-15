# ACM Research Coding Challenge (Spring 2021)

**Solution**
I first researched what circular genome maps looked like. After having a general idea that they show the arrangement
of circular DNA in a diagram, I searched online for the right Python parsing/graphing libraries. I found out about BioPython
which offered methods to parse genbank data and create a circular genome map from it. 

My current solution parses the genbank file and extracts its features. The diagram's title is found in the first feature
and assigned. Afterwards, it creates the genome map through each of the gene sequence features. Finally, it creates a PNG file
of the map and saves it.

I tried to increase the resolution so that the gene names would be more clear, but the BioPython method doesn't have any way to do so.

**Resources**
https://biopython.org/docs/1.75/api/Bio.Graphics.GenomeDiagram.html
https://biopython-tutorial.readthedocs.io/en/latest/notebooks/17%20-%20Graphics%20including%20GenomeDiagram.html#A-top-down-example
also google

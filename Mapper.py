
# import all libraries needed for genome map drawing 
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram

# import library to parse genbank file
from Bio import SeqIO


# parse Genome file 
record = SeqIO.read("Genome.gb", "genbank")
title = record.features[0].qualifiers['organism'][0] 

# create empty diagram
gd_diagram = GenomeDiagram.Diagram(title)
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()


# generate genome map data from features
for feature in record.features:
    
    # only use the gene coding sequence (CDS) to graph each gene
    if feature.type != "gene":
        continue

    # alternate colors
    if len(gd_feature_set) % 2 == 0:
        color = colors.green
    else:
        color = colors.lightgreen


    gd_feature_set.add_feature(feature, color=color, label=True)


# draw diagram and save to PNG
gd_diagram.draw(format="circular", circular=True, pagesize=(20*cm,20*cm), start=0, end=len(record), circle_core=0.7)
gd_diagram.write("circularGenomeMap.png", "PNG")

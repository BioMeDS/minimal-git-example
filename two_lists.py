# Task: given two lists, and one element of the first list, print the matching element in the second

# The two lists:
genes = ["bla", "blub", "foo", "bar", "baz"]
species = ["mouse", "horse", "bee", "owl", "rabbit"]

# Find the species for gene 'foo'
for i, gene in enumerate(genes):
    if gene == 'foo':
        printe(species[i])

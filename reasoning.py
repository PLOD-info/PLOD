#!/usr/bin/python
from owlready2 import *
my_world = World()
onto = my_world.get_ontology("rdf/SARS-CoV-2_Infection_Risk_Ontology_cardinality.owl").load()
data = my_world.get_ontology("rdf/example/PLOD_r3.rdf").load()
sync_reasoner([onto,data])
results = list(my_world.sparql("""
    PREFIX plod: <http://plod.info/rdf/>
    SELECT DISTINCT * WHERE {
        ?s rdf:type plod:HighLevelCloseContact .
    } limit 10"""))
print(results)

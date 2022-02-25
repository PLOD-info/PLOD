# SPARQL例
## Example 1
時間と場所のクロス検索
```sql
PREFIX plod: <http://plod.info/rdf/>
PREFIX schema: <http://schema.org/>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select distinct ?event1 ?place1 ?city1 ?event2 ?place2 ?city2 where { 
    ?event1 a schema:Event ; plod:time ?time1 ; schema:location ?place1 .
    ?place1 plod:city ?city1 .
    ?time1  time:hasBeginning ?begin1 ; time:hasEnd ?end1 .
  ?event2 a schema:Event ; plod:time ?time2 ; schema:location ?place2 .
    ?event2 schema:location ?place1 .
    ?place2 plod:city ?city2 .
  ?time2 time:hasBeginning ?begin2 ; time:hasEnd ?end2 .
    filter(xsd:dateTime(?end1) > xsd:dateTime(?begin2) 
        && xsd:dateTime(?begin1) < xsd:dateTime(?end2))
  filter(?event1 != ?event2)
 }
```

## Example 2
Aさんと中密閉の場所にいた人を回数で降順表示
```sql
PREFIX plod: <http://plod.info/rdf/>
PREFIX schema: <http://schema.org/>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?agent (count(distinct ?event) AS ?cnt)  WHERE { 
    ?event plod:agent <http://plod.info/rdf/id/person_a_A> ;
        plod:agent ?agent ;
        schema:location ?place .
    filter (?agent != <http://plod.info/rdf/id/person_a_A>)
    ?situation plod:isSituationOf ?place .
    ?situation a plod:ClosedSpace .
 } GROUP BY ?agent ORDER BY DESC(?cnt)
```

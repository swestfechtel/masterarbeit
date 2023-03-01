# masterarbeit

## Notes:
- what to do with triads?
- in bucharest dataset: where are nodes with zero degree?

## Questions for next meeting:
- Bucharest dataset: what about non-edges?
- Bucharest dataset: are all contacts patients or do contacts include non-patients? Contrast china datasets where all contacts are patients => both included -> follow up: how to distinguish?
- are non-edges relevant for r(h)em? => no
- REM covariates: do covariates depending on node attributes have to be relation between receiver or sender, e.g. age difference? bei REM alles drei: source, target, relation. Bei rhem: aggregate über receiver set (z.B. avg, std) oder relational (z.B. altersunterschied, sex match etc.)
- how to incorporate anyway? => dummy events: source, target, event type, event value = attribute -> siehe tutorial rhem
- basic analysis: network directed or undirected? => besser ungerichtet

### REM Covariates:
#### Note attributes:
- age difference
- sex difference
- residency difference (where applicable)
- job difference (where applicable)
- more from big china dataset, but need to know if they have to be relational (see question above)

#### Network effects
- repitition
- repiprocity
- triadic closure
- four-cyclic closure
- what else?

## TODO:
- add nodes with zero degree to edge lists 
# coronapolation.sqlite

|ObjectId|Meldedatum              |IdBundesland|          Bundesland| IdLandkreis|        Landkreis| Altersgruppe| Geschlecht|  AnzahlFall|  AnzahlTodesfall|
|--------|------------------------|------------|--------------------|------------|-----------------|-------------|-----------|------------|-----------------|
|  146936|2020-03-20T00:00:00.000Z|          -1|     -nicht erhoben-|         0-1|  -nicht erhoben-|      A15-A34|          W|           1|                0|
|  146937|2020-03-19T00:00:00.000Z|          -1|     -nicht erhoben-|         0-1|  -nicht erhoben-|      A35-A59|          M|           1|                0|
|  146938|2020-03-14T00:00:00.000Z|           1|  Schleswig-Holstein|       01001|     SK Flensburg|      A15-A34|          M|           1|                0|
|  146939|2020-03-19T00:00:00.000Z|           1|  Schleswig-Holstein|       01001|     SK Flensburg|      A15-A34|          M|           2|                0|
|  146940|2020-03-14T00:00:00.000Z|           1|  Schleswig-Holstein|       01001|     SK Flensburg|      A15-A34|          W|           1|                0|

# Execute
````
python3 predict.py <sqlite_dataset>
````

## Basic Operations
What is the count of infections per day, on a district-by-district basis, over the entire history of
the dataset?
````
by_district = dataset.groupby(["Landkreis", "Meldedatum"])["AnzahlFall"].count()
print(by_district.tail(10))
````
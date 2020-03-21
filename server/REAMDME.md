```
curl coronapolation.baremetal.rocks:8080/bundeslaender | json_pp
curl coronapolation.baremetal.rocks:8080/landkreise/<lankreis-id>
curl "coronapolation.baremetal.rocks:8080/infizierte/05111?since=<optional date %Y-%m-%d>&until=<optional date %Y-%m-%d>" | json_pp
curl "coronapolation.baremetal.rocks:8080/neuinfizierte/05111?since=<optional date %Y-%m-%d>&until=<optional date %Y-%m-%d>" | json_pp

```
```
curl https://coronapolation.baremetal.rocks/bundeslaender | json_pp
curl https://coronapolation.baremetal.rocks/landkreise/<lankreis-id>
curl "https://coronapolation.baremetal.rocks/infizierte/05111?since=<optional date %Y-%m-%d>&until=<optional date %Y-%m-%d>" | json_pp
curl "https://coronapolation.baremetal.rocks/neuinfizierte/05111?since=<optional date %Y-%m-%d>&until=<optional date %Y-%m-%d>" | json_pp
curl "https://coronapolation.baremetal.rocks/infizierte_bundesland/1?since=<optional date %Y-%m-%d>&until=<optional date %Y-%m-%d>" | json_pp
curl "https://coronapolation.baremetal.rocks/neuinfizierte_bundesland/1?since=<optional date %Y-%m-%d>&until=<optional date %Y-%m-%d>" | json_pp

```

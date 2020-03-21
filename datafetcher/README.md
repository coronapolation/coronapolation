### Cronjob

```
0 * * * * cd ~/datafetcher && python3 datafetcher.py --config coronapolation-fetcher.conf &> /tmp/datafetcher.log
```

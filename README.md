# crawlersuseragents

<p align="center">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/p0dalirius/crawlersuseragents">
  <a href="https://twitter.com/intent/follow?screen_name=podalirius_" title="Follow"><img src="https://img.shields.io/twitter/follow/podalirius_?label=Podalirius&style=social"></a>
  <a href="https://www.youtube.com/channel/Podalirius_?sub_confirmation=1" title="Subscribe"><img alt="YouTube Channel Subscribers" src="https://img.shields.io/youtube/channel/subscribers/Podalirius_?style=social"></a>
  <br>
</p>

This Python script can be used to check if there is any differences in responses of an application when the request comes from a search engine's crawler.

![](./.github/four_results.png)

## Features

 - [x] 30 crawler's user agent strings.
 - [x] Multithreading.
 - [x] JSON export with `--json outputfile.json`.
 - [x] Auto-detecting responses that stands out.

## Usage

```
$ ./crawlersuseragents.py -h
[~] Access web pages as web crawlers User-Agents, v1.1

usage: crawlersuseragents.py [-h] [-v] [-t THREADS] [-x PROXY] [-k] [-L] [-j JSONFILE] url

This Python script can be used to check if there is any differences in responses of an application
when the request comes from a search engine's crawler.

positional arguments:
  url                   e.g. https://example.com:port/path

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         arg1 help message
  -t THREADS, --threads THREADS
                        Number of threads (default: 5)
  -x PROXY, --proxy PROXY
                        Specify a proxy to use for requests (e.g., http://localhost:8080)
  -k, --insecure        Allow insecure server connections when using SSL (default: False)
  -L, --location        Follow redirects (default: False)
  -j JSONFILE, --jsonfile JSONFILE
                        Save results to specified JSON file.

```

## Auto-detecting responses that stands out

Results are sorted by uniqueness of their response's length. This means that the results with unique response length will be on top, and results with response's length occurring multiple times at the bottom: 

| Two different result lengths | Four different result lengths  |
|------------------------------|--------------------------------|
| ![](./.github/two_results.png) | ![](./.github/four_results.png) |


## Contributing

Pull requests are welcome. Feel free to open an issue if you want to add other features.

## References
 - https://developers.google.com/search/docs/advanced/crawling/overview-google-crawlers
 - https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0

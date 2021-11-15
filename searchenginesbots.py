#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : searchenginesbots.py
# Author             : Podalirius (@podalirius_)
# Date created       : 15 Nov 2021

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
import requests
from rich.console import Console
from rich import box
from rich.table import Table
import json


banner = "[~] Access web pages as web crawlers User-Agents, v1.1\n"

searchengines_bots_ua = {
    # https://developers.google.com/search/docs/advanced/crawling/overview-google-crawlers
    "Google": {
        'APIs-Google': [
            'APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)',
        ],
        'AdSense': [
            'Mediapartners-Google',
        ],
        'AdsBot Mobile Web Android': [
            'Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)',
        ],
        'AdsBot Mobile Web': [
            'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)',
        ],
        'Googlebot Image': [
            'Googlebot-Image/1.0',
        ],
        'Googlebot News': [
            'Googlebot-News',
        ],
        'Googlebot Video': [
            'Googlebot-Video/1.0',
        ],
        'Googlebot Desktop': [
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36',
            'Googlebot/2.1 (+http://www.google.com/bot.html)'
        ],
        "Googlebot Smartphone": [
            "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
        ],
        "Mobile AdSense": [
            "(Various mobile device types) (compatible; Mediapartners-Google/2.1; +http://www.google.com/bot.html)"
        ],
        "Mobile Apps Android": [
            "AdsBot-Google-Mobile-Apps"
        ],
        "Feedfetcher": [
            "FeedFetcher-Google; (+http://www.google.com/feedfetcher.html)"
        ],
        "Google Read Aloud": [
            # Desktop agent:
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36 (compatible; Google-Read-Aloud; +https://developers.google.com/search/docs/advanced/crawling/overview-google-crawlers)",
            # Mobile agent:
            "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36 (compatible; Google-Read-Aloud; +https://developers.google.com/search/docs/advanced/crawling/overview-google-crawlers)",
            # Former agent (deprecated):
            "google-speakr"
        ],
        "Duplex on the web": [
            "Mozilla/5.0 (Linux; Android 11; Pixel 2; DuplexWeb-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36"
        ],
        "Google Favicon": [
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon"
        ],
        "Web Light": [
            "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19"
        ],
        "Google StoreBot": [
            # Desktop agent:
            "Mozilla/5.0 (X11; Linux x86_64; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
            # Mobile agent:
            "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36"
        ]
    },
    # https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0
    "Bing": {
        'Bingbot': [
            "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
            "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/W.X.Y.Z Safari/537.36 Edg/W.X.Y.Z",
            "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 Edg/W.X.Y.Z (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
        ],
        'AdIdxBot': [
            "Mozilla/5.0 (compatible; adidxbot/2.0; +http://www.bing.com/bingbot.htm)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; adidxbot/2.0; +http://www.bing.com/bingbot.htm)",
            "Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 530) like Gecko (compatible; adidxbot/2.0; +http://www.bing.com/bingbot.htm)"
        ],
        'BingPreview': [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534+ (KHTML, like Gecko) BingPreview/1.0b",
            "Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 530) like Gecko BingPreview/1.0b"
        ],
    }
}


def test_searchengine_ua(options, proxies, results, botowner, ua_source, ua_value):
    try:
        r = requests.get(
            url=options.url,
            # this is to set the client to accept insecure servers
            verify=options.verify,
            proxies=proxies,
            allow_redirects=options.redirect,
            # this is to prevent the download of huge files, focus on the request, not on the data
            stream=True,
            headers={"User-Agent": ua_value}
        )
    except requests.exceptions.ProxyError:
        print("[!] Invalid proxy specified")
        raise SystemExit
    if options.verbose == True:
        print("[!] Obtained results: [%d] length : %d bytes" % (r.status_code, len(r.content)))

    results.append(
        {
            "status_code": r.status_code,
            "length": len(r.text),
            "bot-owner": botowner,
            "bot-name": ua_source,
            "user-agent": ua_value
        }
    )


def print_results(console, results):
    if options.verbose == True:
        print("[>] Parsing & printing results")

    table = Table(show_header=True, header_style="bold blue", border_style="blue", box=box.SIMPLE)
    table.add_column("Bot Owner")
    table.add_column("Bot Name")
    table.add_column("Length")
    table.add_column("Status code")
    table.add_column("User Agent")

    # Choose colors for uncommon lengths
    lengths = [result["length"] for result in results]
    lengths = [(len([1 for result in results if result["length"] == l]), l) for l in list(set(lengths))]
    lengths = sorted(lengths, key=lambda l:l[1])

    # Sorting the results by uniqueness of response length
    _results = []
    for target_length in sorted(lengths):
        _results += [lr for lr in results if lr["length"] == target_length[1]]
    results = _results

    if len(lengths) == 2:
        for result in results:
            if result["length"] == min(lengths)[1]:
                style = "green"
            elif result["length"] == max(lengths)[1]:
                style = "red"
            table.add_row(result["bot-owner"], result["bot-name"], str(result["length"]), str(result["status_code"]), result["user-agent"], style=style)

    elif len(lengths) == 3:
        scale = ["red", "orange3", "green"]
        colors = {str(lengths[k][1]): scale[k] for k in range(len(lengths))}
        for result in results:
            style = colors[str(result["length"])]
            table.add_row(result["bot-owner"], result["bot-name"], str(result["length"]), str(result["status_code"]), result["user-agent"], style=style)

    elif len(lengths) == 4:
        scale = ["red", "orange3", "yellow3", "green"]
        colors = {str(lengths[k][1]): scale[k] for k in range(len(lengths))}
        for result in results:
            style = colors[str(result["length"])]
            table.add_row(result["bot-owner"], result["bot-name"], str(result["length"]), str(result["status_code"]), result["user-agent"], style=style)

    else:
        for result in results:
            style = "orange3"
            table.add_row(result["bot-owner"], result["bot-name"], str(result["length"]), str(result["status_code"]), result["user-agent"], style=style)
    console.print(table)


def parseArgs():
    description = "This Python script can be used to check if there is any differences in responses of an application when the request comes from a search engine's crawler."
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "url",
        help="e.g. https://example.com:port/path"
    )
    parser.add_argument("-v", "--verbose", default=None, action="store_true", help='arg1 help message')
    parser.add_argument("-t", "--threads", dest="threads", action="store", type=int, default=5, required=False, help="Number of threads (default: 5)")
    parser.add_argument('-x', '--proxy', action="store", default=None, dest='proxy', help="Specify a proxy to use for requests (e.g., http://localhost:8080)")
    parser.add_argument("-k", "--insecure", dest="verify", action="store_false", default=True, required=False, help="Allow insecure server connections when using SSL (default: False)")
    parser.add_argument("-L", "--location", dest="redirect", action="store_true", default=False, required=False, help="Follow redirects (default: False)")
    parser.add_argument("-j", "--jsonfile", dest="jsonfile", default=None, required=False, help="Save results to specified JSON file.")
    return parser.parse_args()


if __name__ == '__main__':
    print(banner)

    options = parseArgs()
    try:
        console = Console()
        # Verifying the proxy option
        if options.proxy:
            try:
                proxies = {
                    "http": "http://" + options.proxy.split('//')[1],
                    "https": "http://" + options.proxy.split('//')[1]
                }
                if options.verbose == True:
                    print("[debug] Setting proxies to %s" % str(proxies))
            except (IndexError, ValueError):
                print("[!] Invalid proxy specified.")
                sys.exit(1)
        else:
            if options.verbose == True:
                print("[debug] Setting proxies to 'None'")
            proxies = None

        if not options.verify:
            # Disable warings of insecure connection for invalid cerificates
            requests.packages.urllib3.disable_warnings()
            # Allow use of deprecated and weak cipher methods
            requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
            try:
                requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
            except AttributeError:
                pass

        results = []
        # Waits for all the threads to be completed
        with ThreadPoolExecutor(max_workers=min(options.threads, len(searchengines_bots_ua))) as tp:
            for botowner in searchengines_bots_ua.keys():
                for ua_source in searchengines_bots_ua[botowner].keys():
                    for ua_value in searchengines_bots_ua[botowner][ua_source]:
                        tp.submit(test_searchengine_ua, options, proxies, results, botowner, ua_source, ua_value)

        # Parsing and print results
        print_results(console, results)

        # Export to JSON if specified
        if options.jsonfile is not None:
            f = open(options.jsonfile, "w")
            f.write(json.dumps(results, indent=4) + "\n")
            f.close()

    except KeyboardInterrupt:
        print("[+] Terminating script...")
        raise SystemExit

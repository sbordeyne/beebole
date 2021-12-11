# This dirty as fuck script will scrape the documentation from beebole
# to extract sample data to run tests against. It's automated so that as long
# as beebole maintains an up-to-date doc, the tests should reflect the state of
# their API. The script is very fragile though, as beebole apparently doesn't
# know how to write proper HTML, or even JSON for that matters.

import requests
from lxml import etree
import jstyleson as json
from pathlib import Path
import re


def extract(data):
    responses = {}
    payloads = {}
    service = ''
    for i, node in enumerate(data):
        if i < 13:
            continue
        if node.tag == 'p' and node.text is not None:
            d = ''.join(e.text for e in data[i + 1].xpath('./span'))
            d = re.sub(r'\.\.\.', '', d)  # clean out the ellipsis
            d = re.sub(r'//(.+)\n', '', d)  # clean out the comments on top
                                            # of using jstyleson
            if node.text.lower() == 'request:':
                try:
                    nodedata = json.loads(d)
                except:
                    try:
                        nodedata = json.loads(re.subn('\}', '', d, 1)[0])
                    except:
                        print(re.subn('\}', '', d, 1)[0])
                        break
                service = nodedata.pop('service', '')
                payloads[service] = nodedata
            if node.text.lower() == 'response:':
                try:
                    nodedata = json.loads(d)
                except:
                    print(d)
                    continue
                responses[service] = nodedata
    return payloads, responses


def main():
    DOC_URL = 'https://beebole.com/timesheet-api'
    doc_html = requests.get(DOC_URL).text

    parser = etree.HTMLParser(recover=True)
    root = etree.fromstring(doc_html, parser)
    data = root.xpath(
        ".//h3|.//h3/following-sibling::p|.//h3/following-sibling::div//code"
    )
    payloads, responses = extract(data)
    with open(Path(__file__).parent.parent / 'tests/data/payloads.json', 'w') as outfile:
        json.dump(payloads, outfile, indent=2)
    with open(Path(__file__).parent.parent / 'tests/data/responses.json', 'w') as outfile:
        json.dump(responses, outfile, indent=2)


if __name__ == '__main__':
    main()

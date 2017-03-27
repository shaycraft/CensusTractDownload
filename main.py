from sys import stdout
import urllib2
from lxml import html
import os

url = "http://www2.census.gov/geo/tiger/TIGER2015/TRACT"
htmlStr = urllib2.urlopen(url).read()
DOWNLOAD_FOLDER = 'Downloads'
BUFFER_SIZE = 300 * 1024

if not os.path.exists(DOWNLOAD_FOLDER):
    print 'Creating downloads folder...'
    os.makedirs(DOWNLOAD_FOLDER)

zips = html.fromstring(htmlStr).xpath('//table/tr/td/a[last()]/text()')[1:]
for z in zips:
    with open('Downloads/{0}'.format(z), 'wb') as download_file:
        downloadUrl = '{0}/{1}'.format(url, z)
        print 'Downloading {0}'.format(downloadUrl)
        res = urllib2.urlopen(downloadUrl)
        while True:
            chunk = res.read(BUFFER_SIZE)
            if not chunk:
                break
            download_file.write(chunk)
            print '.',
    print



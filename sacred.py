import requests
import re
import sys
ls

if len(sys.argv) < 2:
   print 'Usage: python sacred.py <outfile>'
   sys.exit()

#import mechanize
url_stem = 'http://www.sacred-texts.com/eso/sta/sta'
delimiter = '</p>'
book = ''


for i in range(3, 51):
   file_index = i
   if file_index < 10:
      file_index = '%d%d' % (0, file_index)
   print 'getting file index %s' % file_index
   url = '%s%s%s' % (url_stem, file_index, '.htm')
   page = requests.get(url).text
   page = page[page.index(delimiter):]
   page = re.sub('<[^<]+?>', '', page)
   page = re.sub('Click to enlarge', '', page)
   book = '%s%s' % (book, page)

outfile = open(sys.argv[1], 'w')
outfile.write(book)

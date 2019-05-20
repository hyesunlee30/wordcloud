from collections import Counter
from konlpy.tag import Twitter
import pytagcloud


import codecs

fileObj = codecs.open( "한국폴리텍poly2.txt", "r", "utf-8" )

data = fileObj.read()

nlp = Twitter()
nouns = nlp.nouns(data)
nouns = [n for n in nouns if len(n) > 1]

count = Counter(nouns)
tags2 = count.most_common(40)
taglist = pytagcloud.make_tags(tags2, maxsize=80)
pytagcloud.create_tag_image(taglist, '한국폴리텍.jpg', size=(800, 500), fontname='Noto Sans CJK', rectangular=False)

fileObj.close()


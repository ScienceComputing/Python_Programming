"""
Pass the html content from a variable to the Selector
"""
from scrapy.selector import Selector

html = """
<html>
  <body>
    <div id="div1" class="class-1">
      <p class="class-1 class-2">Hello Protein-Protein Interaction!</p>
      <div id="div2">
        <p id="p2" class="class-2">Choose 
            <a href="https://www.ebi.ac.uk/intact/home">IntAct!</a>!
        </p>
      </div>
    </div>
    <div id="div3" class="class-2">
      <p class="class-2">Enjoy IntAct!</p>
    </div>
  </body>
</html>
"""

sel = Selector(text=html) 
sel.xpath('//p') # Return a SelectorList of Selector objects
# [<Selector query='//p' data='<p class="class-1 class-2">Hello Prot...'>, <Selector query='//p' data='<p id="p2" class="class-2">Choose \n  ...'>, <Selector query='//p' data='<p class="class-2">Enjoy IntAct!</p>'>]
sel.xpath('//p').extract()
# ['<p class="class-1 class-2">Hello Protein-Protein Interaction!</p>', '<p id="p2" class="class-2">Choose \n            <a href="https://www.ebi.ac.uk/intact/home">IntAct!</a>!\n        </p>', '<p class="class-2">Enjoy IntAct!</p>']
sel.xpath('//p').extract_first() # Return the data of the first Selector object
# '<p class="class-1 class-2">Hello Protein-Protein Interaction!</p>'
sel.xpath('//p')[1].extract() # Return the data of the second Selector object
# '<p id="p2" class="class-2">Choose \n            <a href="https://www.ebi.ac.uk/intact/home">IntAct!</a>!\n        </p>'

# XPath chaining: the following 3 lines are equivalent
sel.xpath('/html/body/div[1]')
# [<Selector query='/html/body/div[1]' data='<div id="div1" class="class-1">\n     ...'>]
sel.xpath('/html').xpath('./body/div[1]')
# [<Selector query='./body/div[1]' data='<div id="div1" class="class-1">\n     ...'>]
sel.xpath('/html').xpath('./body').xpath('./div[1]')
# [<Selector query='./div[1]' data='<div id="div1" class="class-1">\n     ...'>]

def print_attribute(xpath, html_content):
    sel = Selector(text=html_content) # Set up the selector, which selects the entire html content
    print("You have selected:")
    for i, el in enumerate(sel.xpath(xpath).extract()):
        print("%d) %s" % (i+1, el))

print_attribute('//p[@id="p2"]/a/@href', html)

"""
Pass the html content from a website to the Selector
"""
from scrapy.selector import Selector
import requests
target_url = 'https://www.ncbi.nlm.nih.gov/clinvar/?term=BRCA1%5Bgene%5D&redir=gene'
html = requests.get(target_url).content
sel = Selector(text=html) 
print(f"We have found: {len(sel.xpath('//*'))} elements in this website!")
# We have found: 7778 elements in this website!


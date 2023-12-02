from scrapy.selector import Selector

def print_attribute(xpath, html_content):
    sel = Selector(text=html_content)
    print("You have selected:")
    for i, el in enumerate(sel.xpath(xpath).extract()):
        print("%d) %s" % (i+1, el))

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

print_attribute('//p[@id="p2"]/a/@href', html)

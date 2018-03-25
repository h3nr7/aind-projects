import markdown2 as md2
from jinja2 import Environment, PackageLoader, select_autosecape


class GenerateHtml():
    def __init__(self):
        print('begin generator:')
        self.env = Environment(
            loader=PackageLoader('aind_projects', 'templates'),
            autoescape=select_autosecape(['html', 'xml'])
        )
        self.createIndex()

    def createIndex(self):
        index_file = open("index.md", "r")
        with open("docs/index.html", "w") as html_file:
            html_file.write(md2.markdown(index_file.read()))


GenerateHtml()

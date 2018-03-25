"""generate html"""

import os
import glob
import shutil
import logging
import markdown2 as md2
from jinja2 import Environment, PackageLoader, select_autoescape


class GenerateHtml():
    def __init__(self):
        print('begin generator:')
        self.env = Environment(
            loader=PackageLoader('core', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.logger = logging.getLogger('AIND Logger')
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        fomatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(fomatter)
        self.logger.addHandler(ch)

        self.createIndex()
        self.cloneHtml()


    def createIndex(self):
        index_template = self.env.get_template('index.html')
        with open("docs/index.html", "w") as html_file:
            html_file.write(index_template.render(
                title='AIND Projects'
            ))

    def cloneHtml(self):
        src_files = os.listdir()
        # for file_name in src_files:
        #     self.logger.info(file_name)

if __name__ == '__main__':
    GenerateHtml()

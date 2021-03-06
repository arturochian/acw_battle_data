# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 22:47:55 2014

@author: jrnold
"""
import glob
import csv

import utils
    
if __name__ == "__main__":      
    srcdir = "battles/dbpedia"
    dst = "battles_wikipedia_links.csv"
    files = glob.glob("%s/*.ntriples" % srcdir)
    wikilinks = [utils.get_wikipedia_page(src) for src in files]
    with open(dst, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["dbpedia", "wikipedia"])
        for row in wikilinks:
            if row:
                writer.writerow(row)
        
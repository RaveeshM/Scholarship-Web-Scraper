from urllib.request import urlopen
import csv

def snip(src, sub1, sub2):
    """ Given a src string, snip the text located between strings sub1 and sub2"""
    idx_start = src.find(sub1) + len(sub1)
    idx_end = src.find(sub2, idx_start)
    
    return src[idx_start:idx_end].strip()

with open('scholarships.csv', 'w', newline = '') as csv_file:
    csvwriter = csv.writer(csv_file)

    header = ['Scholarship Name', 'Deadline', 'Amount', 'Description', 'Location', 'Years', 'Link']
    csvwriter.writerow(header)

    # opens each of the 769 pages
    for page_num in range(1, 770):
        
        # retrieve the page and html source
        url = 'http://www.collegescholarships.org/financial-aid/?page=' + str(page_num)
        page = urlopen(url)
        html = page.read().decode()

        # restrict to scholarship-list html class
        scholarships_class = snip(html,'<div class="scholarship-list">', '<ul class="pagination">')

        # split into list, remove dummy first element
        scholarships_list = scholarships_class.split('<div class="row">')
        scholarships_list.pop(0)

        # collect string fields for each scholarship by snipping the information between HTML tags
        for scholarship in scholarships_list:
            amount = snip(scholarship, '<strong>$', '</strong>')
            link = snip(scholarship, '<h4 class="text-uppercase"><a href="', '"')
            name = snip(scholarship, '<h4 class="text-uppercase"><a href="' +
                        link + '">', '</a>')        
            deadline = snip(scholarship, '</span><br />\n                <strong>', '</strong>')        
            description = snip(scholarship, '</p>\n        <p>', '</p>\n')          
            location = snip(scholarship, '<i class="fa fa-li fa-map-marker"></i>\n                    ' +
                            '<span class="trim" data-length="120">\n', '\n')          
            years = snip(scholarship, '<i class="fa fa-li fa-graduation-cap"></i>\n                    ' +
                         '<span class="trim" data-length="120">\n                                            ',
                         '\n                                        </span>\n                </li>\n' +
                         '                <li>\n                    <i class="fa fa-li fa-book"></i>\n')
            
            # combine the strings into a list to write a row to the csv
            csvwriter.writerow([name, deadline, amount, description, location, years, link])
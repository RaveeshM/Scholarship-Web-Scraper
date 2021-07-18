# python-scholarship-scraper
 A python-based web scraper that scrapes scholarship data into a CSV file

## Purpose
Scholarship information is often hosted on websites with difficult-to-navigate UI's which can make filtering scholarship data by major, location, amount, etc. hard to do. This scraper scrapes the 23,041 scholarships hosted on [http://www.collegescholarships.org/](http://www.collegescholarships.org/) and outputs the data as a CSV.

## How does it work?
The scraper relies on Python's [urllib.request](https://docs.python.org/3/library/urllib.request.html) library and [CSV](https://docs.python.org/3/library/csv.html) module. First, one of the pages of results is opened from site and its entire HTML data is extracted. Next, using Python string functions, the relevant information is extracted as a series of strings for the scholarship amount, name, description, etc. Last, these strings are combined into a list and added as a row of data in the CSV. This process is repeated for each scholarship on a page, and then for each of the pages on the site.

```python
def snip(src, sub1, sub2):
    """ Given a src string, snip the text located between strings sub1 and sub2"""
    idx_start = src.find(sub1) + len(sub1)
    idx_end = src.find(sub2, idx_start)
    
    return src[idx_start:idx_end].strip()
```
The heavy-lifting of this scraper is done using the ```snip``` function. This function extracts the string located after a given ```sub1``` string and before a ```sub2``` string.

## How does it look?
The data from the scraper is outputted as a CSV file which can be opened with Microsoft Excel or Google Sheets to filter and refine. An example of the output is provided [here](example-scholarships.csv).

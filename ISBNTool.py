import isbnlib
import csv

class ISBNTool:
  # Returns a book object with all the data recovered
  def getBookInfo(self, bookCode):
    book = isbnlib.meta(bookCode)

    # Add a description, if available
    try:
      book['Description'] = isbnlib.desc(ISBN)
    except:
        pass

    return book

  # Writes the info of a book to a csv file
  def writeInfo(self, book, output):
    with open(output, "a") as outfile:
    # Init writer
    writer = csv.writer(outfile)

    # Write book info
    writer.writerow(['ISBN', 'Title', 'Author', 'Year', 'Description'])
    if book['Description'] != None:
      writer.writerow([book['ISBN-13'], book['Title'], book['Authors'][0], book['Year'], book['Description']])
    else:
      writer.writerow([book['ISBN-13'], book['Title'], book['Authors'][0], book['Year'], "N/A"])

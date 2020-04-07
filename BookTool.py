import isbnlib
import csv
import os

class BookTool:
  # Returns a book object with all the data recovered
  def getBookInfo(self, bookCode):
    book = isbnlib.meta(bookCode)

    # Add a description, if it's available and if the book was recovered
    if book:
      try:
        book['Description'] = isbnlib.desc(ISBN)
      except:
        book['Description'] = "N/A"

    return book

  # Writes the info of a book to a csv file
  def writeInfo(self, book, output):
    # Write header if it's the first time writing the file
    writeHeader = True if not os.path.exists(output) else False

    with open(output, "a") as outfile:
      # Init writer
      writer = csv.writer(outfile)

      # Write book info
      if writeHeader: writer.writerow(['ISBN', 'Title', 'Author', 'Year', 'Description']) 
      writer.writerow([book['ISBN-13'], book['Title'], book['Authors'][0], book['Year'], book['Description']])

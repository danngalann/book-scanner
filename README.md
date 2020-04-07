# Book Scanner
## A little explanation
So I have a lot of books. A lot. The day came when I had to donate some of them to my local library to free space on my bedroom, and in order to do that I had to submit a document with the titles of all the books I wanted to donate, so my library could tell me which books did they want.

Naturally, being as lazy as I am, I didn't want to spend thirty minutes manually writting all the titles. So instead I spent three days writting a script that could read the barcodes at the back of the books, search the internet for their info, and write it to a file.

## Files
* `getBooks.py`: This is the main file. It iterate over the images in the images folder and use BarcodeScanner and BookTool to write the information of each book to a file.
* `BarcodeScanner.py`: This class can take an image and return any barcodes it could read on it. In the case of books, the barcode is usually the [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number).
* `BookTool.py`: This class can take an ISBN and return a book object with all the info it could find. It also can take a book and write all the info to a csv file.

## How to use
To use this script, download or copy this repo and run
`pip install -r requirements.txt`
Then copy all the pictures of the barcodes of your books to the `images` folder, and run
`python getBooks.py`
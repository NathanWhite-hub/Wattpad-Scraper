# Wattpad-Scraper

This is a Python script that extracts the text from stories on Wattpad as well as all chapters within a story.

A special thanks to the developers at https://playwright.dev for their great library.

## Installation

**1.)** If not already installed, go to https://www.python.org/downloads/ and download the latest version of Python for your OS. Make sure to install pip with the installation (check the box).

**2.)** Run both of the following commands in command prompt or terminal if on MacOS.
```
pip install playwright
playwright install
```

**3.)** I recommend placing both the script and the link.txt in a folder on your desktop for organizational purposes.

## Use

This script reads the text file known as links.txt. A user will paste the links to the stories they wish to scrape (do not post the actual chapters) into the links.txt file, each story separated by a new line. The script will then open a browser window, scan for the chapters, then visit each chapter of the story and scrape the story text content before moving onto the next line (the next link) in the links.txt file and repeating.

All scraped text will be placed in a file called wattPadExport.txt in the directory that the script is in. This script also formats the data to remove the '+' symbol that is exported with it. This symbol is scraped from WattPad, which is the symbol from the quote box and is not a part of the story text content. Run the .py file to begin the process and watch the script go.

This does not clean the data for use in an AI, and I recommend using other scripts/tools out there for doing so.

I wrote this script for use in collecting data to train ML models, and I am not responsible for what you do with the scraped content; use it morally.

## In-Depth Explanation

This is an in-depth explanation of what this script does and is not necessary if you are just using it to scrape data. The script starts off with opening the browser context and then opening the links.txt file. It runs the readlines() method and stores the output list in the variable storylinks.

It then runs a for loop to cycle through the list of stories and for each story it begins with declaring an empty list known as the variable chapterLinks. It then navigates to the storylink URL and queries all of the <a> tags within the .story-parts class of the DOM (the .story-parts class holds an unordered list of all the chapters).
  
After querying all of the selectors, it then runs another for loop that appends the href attribute of each <a> tag onto the chapterLinks list. Now that it has each link to the chapters, it begins the scraping process.

### The Scraping Process
  
The script then begins a for loop that navigates to each chapter link in the chapterLink list. On each page, it will query all `<p>` tag selectors that are contained within the ``<pre>`` tag. It then runs a for loop to grab each `<p>` tag's text content and add/assign it to the text_paragraph variable. While it might look messy, it is necessary to assign the text content to a new variable as the paragraph variable is one of the list elements and has the selector information stored as JNode.

After adding all of the text content to the text_paragraph variable, it then opens (or creates) the wattPadExport.txt file within the script's current directory. It then replaces the + sign, keeping a bit of space at the start (so it can differentiate if someone added a + in their story, and replaces it with an empty character.

It then writes the text_paragraph to the text file and adds new lines to separate the stories. This entire process is then repeated for the rest of the storylinks.

from os import close
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    
    # Opens the links.txt file.
    with open('links.txt', 'r', encoding='utf-8') as cd:
        
        # Run the readlines() method and store the list in storyLinks
        storyLinks = cd.readlines()
        
        # Loop through each story link in the list.
        for storyLink in storyLinks:
            
            # Assign the empty variables
            text_paragraph = ""
            chapterLinks = []
            
            # Open the story's main page
            page.goto(storyLink)
            
            # Query all of the selectors that contain the href for the chapters
            chapters = page.query_selector_all('.story-parts >> ul >> li >> a')
            
            # Loop through the list and concatinate the href for the chapter onto the main website URL
            for chapter in chapters:
                chapterLinks.append('https://www.wattpad.com' + chapter.get_attribute('href'))
                
            # Loop through each chapter in the gathered list
            for chapterLink in chapterLinks:
                
                page.goto(chapterLink)
                
                # Query all paragraph selectors in the pre tag. This holds the story text
                paragraphs = page.query_selector_all('pre >> p')
                
                # Loop through the selectors and add assign the text content onto the text_paragraph variable
                for paragraph in paragraphs:
                    
                    text_paragraph += paragraph.text_content()
                
                # Open the wattPadExport text file, then replace the + symbol that gets scraped, and write the scraped
                # text content from the story. Then write new lines to seperate the next story.
                with open('wattPadExport.txt', 'w', encoding="utf-8", newline='\n') as cd:

                    text_paragraph = text_paragraph.replace('  +', '')
                    cd.write(text_paragraph + '\n\n\n\n')

            # ---------------------
        context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

from os import close
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    text_paragraph = ""

    # Open new page
    page = context.new_page()

    with open('links.txt', 'r', encoding='utf-8') as cd:

        storylinks = cd.readlines()

        for storylink in storylinks:

            chapterLinks = []

            page.goto(storylink)

            chapters = page.query_selector_all('.story-parts >> ul >> li >> a')

            for chapter in chapters:
                chapterLinks.append('https://www.wattpad.com' + chapter.get_attribute('href'))

            for chapterLink in chapterLinks:

                page.goto(chapterLink)
                # Click text=In the simple town of Beaufort, British Columbia lived couple so in love, that i
                paragraphs = page.query_selector_all('pre >> p')

                for paragraph in paragraphs:
                    
                    text_paragraph += paragraph.text_content()
                
                with open('wattPadExport.txt', 'w', encoding="utf-8", newline='\n') as cd:

                    text_paragraph = text_paragraph.replace('  +', '')
                    cd.write(text_paragraph + '\n\n\n\n')

            # ---------------------
        context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

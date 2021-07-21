from services import database_service
import asyncio
from pyppeteer import launch

from settings import database_settings

database_service.connect_to_database()

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(database_settings['SCRAPPER_WEBPAGE_URL'])
    await page.screenshot({'path': 'example.png'})
    await browser.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())


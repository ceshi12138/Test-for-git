import aiohttp
import asyncio
from bs4 import BeautifulSoup
import os

async def fetch_chapter(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            return None
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string
        chapter_content = soup.find('div', {'id': 'chaptercontent'}).get_text(separator="\n")
        return title, chapter_content

async def main(chapter_ids):
    path = r'C:\Users\Administrator\Desktop\新建文件夹(2).txt'
    base_url = 'https://www.bigee.cc/book/3524/'

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_chapter(session, base_url + str(i) + '.html') for i in chapter_ids]
        chapters = await asyncio.gather(*tasks)

    # 确保路径存在
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'a', encoding='utf-8') as file:
        for i, (title, chapter_content) in enumerate(chapters, start=1):
            if title is not None and chapter_content is not None:
                print(f"正在爬取第{i}章")
                file.write(title + "\n")
                file.write(chapter_content + "\n\n")

chapter_ids = list(range(1, 2000))
asyncio.run(main(chapter_ids))

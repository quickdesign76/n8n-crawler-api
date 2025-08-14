import asyncio
from crawl4ai import AsyncWebCrawler

# هذه هي الدالة الرئيسية التي تقوم باستخراج البيانات
async def run_crawler(target_url: str):
    # نقوم بتهيئة الأداة
    async with AsyncWebCrawler() as crawler:
        # نقوم بتشغيلها على الرابط المطلوب
        result = await crawler.arun(url=target_url)
        # نعيد النتيجة بصيغة نص نظيف (Markdown)
        return {
            "url": target_url,
            "content": result.markdown,
            "success": True,
            "error": None
        }

# هذا الجزء للتجربة فقط إذا أردت تشغيل الملف مباشرة
if __name__ == '__main__':
    test_url = "https://www.n8n.io/"
    print(f"Testing crawler on: {test_url}")
    result = asyncio.run(run_crawler(test_url))
    print(result["content"][:500]) # طباعة أول 500 حرف

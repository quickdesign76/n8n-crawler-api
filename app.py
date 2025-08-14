from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from crawl import run_crawler # نستدعي الدالة من الملف السابق

# تهيئة تطبيق الـ API
app = FastAPI()

# نحدد شكل البيانات التي سيستقبلها التطبيق
class URLRequest(BaseModel):
    url: str

# هذا هو التعريف الرئيسي لنقطة النهاية (Endpoint)
@app.post("/crawl")
async def create_crawl_job(request: URLRequest):
    try:
        # نطبع الرابط الذي استلمناه (مفيد لتصحيح الأخطاء)
        print(f"Received request to crawl: {request.url}")
        # نقوم بتشغيل أداة الكرولر وننتظر النتيجة
        result = await run_crawler(request.url)
        # نعيد النتيجة إلى n8n
        return result
    except Exception as e:
        # في حال حدوث أي خطأ، نعيد رسالة خطأ واضحة
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# هذا السطر يسمح للخادم بالعمل (للتجربة المحلية)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

import asyncio
from flask import Flask, jsonify, request
from crawl4ai import AsyncWebCrawler
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # Enable CORS for all domains

async def fetch_data(url):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        return result.markdown

@app.route("/crawl", methods=["GET"])
def home():
    url = request.args.get("url", "https://www.nbcnews.com/business")  # Default URL
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(fetch_data(url))
    return jsonify({"data": result})

if __name__ == "__main__":
    app.run(debug=True)

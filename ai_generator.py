import openai
import os
from dotenv import load_dotenv
from openai import OpenAIError, APIError, AuthenticationError, RateLimitError

load_dotenv()  # Ensure .env is loaded before using the key

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_blog_post(keyword, seo_data):
    prompt = f"""
Write a blog post about "{keyword}".
Include: Introduction, Benefits, Top Products (with affiliate link placeholders), and Conclusion.
Make it SEO-optimized using:
- Search Volume: {seo_data['search_volume']}
- Keyword Difficulty: {seo_data['keyword_difficulty']}
- CPC: ${seo_data['avg_cpc']}

Use {{AFF_LINK_1}}, {{AFF_LINK_2}} as placeholders for links.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content
    except RateLimitError:
        content = "⚠️ Error: OpenAI API rate limit exceeded. Please try again later."
    except AuthenticationError:
        content = "⚠️ Error: Invalid or expired OpenAI API key."
    except APIError as e:
        content = f"⚠️ API Error: {str(e)}"
    except OpenAIError as e:
        content = f"⚠️ Unexpected OpenAI error: {str(e)}"
    except Exception as e:
        content = f"⚠️ Unexpected Error: {str(e)}"

    return content.replace("{{AFF_LINK_1}}", "https://example.com/product1") \
                  .replace("{{AFF_LINK_2}}", "https://example.com/product2")

import google.generativeai as genai
import os
from dotenv import load_dotenv
import typing_extensions as typing
load_dotenv()


class Story(typing.TypedDict):
    story_parts: list[str]
    prompts_for_each_part: list[str]
    kazanim_numarasi: str


key = os.getenv("API_KEY")

genai.configure(api_key=key)

model = genai.GenerativeModel("gemini-1.5-pro", system_instruction="You are an elementary school teacher.")
sample_pdf = genai.upload_file("hb_kitap.pdf")
response = model.generate_content(
    ["HB.x.x.x. olarak belirtilmiş kazanımlardan 1 tanesi ile ilgili eğitici anafikri olan türkçe hikayeler yaz. "
     "Hikayeler en az 500 kelime olsun."
     "Hikayeler sahne sahne bölünmüş olsun. "
     "Her sahne için yapay zekayla görsel üretmemizi sağlayacak ingilizce promtlar yaz. "
     "Promtlar olabildiğince detaylı olsun."
     "Kazanımların numarasını belirt.", sample_pdf],
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json", response_schema=list[Story]
    ),
    stream=True,
)

for chunk in response:
    print(chunk.text)
    print("_" * 80)

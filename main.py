import google.generativeai as genai
import os
from dotenv import load_dotenv
import typing_extensions as typing
from outcomes import list_of_outcomes

load_dotenv()

outcomes = list_of_outcomes()


class Scene(typing.TypedDict):
    image_prompt: str  # The prompt for the image generation of the scene
    scene_text: str  # The text content of the scene


class Story(typing.TypedDict):
    story_scenes_and_image_prompts: list[Scene]
    outcome: str


key = os.getenv("API_KEY")

genai.configure(api_key=key)

model = genai.GenerativeModel("gemini-1.5-pro",
                              system_instruction="You are an author aimed at elementary school students.")

response = model.generate_content(
    f"Write an educational story in Turkish centered around {outcomes[10]}"
    "Story should contain an educational main theme aligned with the specified outcome."
    "Story should be at least 1000 words and divided into scenes."
    "For each scene, create detailed English prompts for generating images using AI."
    "Ensure the prompts are as simple as possible."
    "Specify the outcome in the story.",
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json", response_schema=list[Story]
    ),
    stream=True,
)

for chunk in response:
    print(chunk.text)

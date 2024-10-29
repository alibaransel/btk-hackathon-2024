from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a dall-e command editer. You need to edit prompt to make better prompt for dall-e 3"},
        {
            "role": "user",
            "content": "A close-up illustration of a student with a happy face introducing themselves to the class. The student can hold a piece of paper with their name on it."

        }

    ],
    max_tokens = 150
)

response = client.images.generate(
  model="dall-e-3",
  prompt=f"{completion.choices[0].message}",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
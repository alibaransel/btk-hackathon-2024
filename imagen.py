import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

# TODO(developer): Update and un-comment below lines
project_id = "vertex-ai-440116"

vertexai.init(project=project_id, location="us-central1")

generation_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

prompt = """
A photorealistic image of a cookbook laying on a wooden kitchen table, the cover facing forward featuring a smiling family sitting at a similar table, soft overhead lighting illuminating the scene, the cookbook is the main focus of the image.
"""

image = generation_model.generate_images(
    prompt=prompt,
    number_of_images=1,
    aspect_ratio="1:1",
    safety_filter_level="block_some",
    person_generation="allow_all",
)

# OPTIONAL: View the generated image in a notebook
image[0].show()
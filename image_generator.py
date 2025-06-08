async def generate_thumbnail(prompt: str) -> str:
    response = await openai.Image.acreate(
        prompt=f"Podcast thumbnail illustration: {prompt}",
        n=1,
        size="512x512",
        response_format="url"
    )

    image_url = response['data'][0]['url']
    image_path = os.path.join(IMAGE_OUTPUT_DIR, f"{uuid.uuid4()}.png")

    async with httpx.AsyncClient() as client:
        img_data = await client.get(image_url)
        with open(image_path, "wb") as f:
            f.write(img_data.content)

    return image_path

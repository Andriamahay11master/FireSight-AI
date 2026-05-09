# backend/app/utils/image_processing.py

from PIL import Image
import io


# -----------------------------------------
# LOAD IMAGE FROM BYTES
# -----------------------------------------
def load_image(image_bytes: bytes) -> Image.Image:
    """
    Convert uploaded bytes into a PIL image.
    """

    try:
        image = Image.open(io.BytesIO(image_bytes))

        return image

    except Exception as e:
        raise ValueError(f"Invalid image file: {str(e)}")


# -----------------------------------------
# CONVERT IMAGE TO RGB
# -----------------------------------------
def convert_to_rgb(image: Image.Image) -> Image.Image:
    """
    Ensure image is in RGB format.
    """

    if image.mode != "RGB":
        image = image.convert("RGB")

    return image


# -----------------------------------------
# RESIZE IMAGE
# -----------------------------------------
def resize_image(
    image: Image.Image,
    size=(640, 640)
) -> Image.Image:
    """
    Resize image for model inference.
    """

    return image.resize(size)


# -----------------------------------------
# COMPLETE PREPROCESSING PIPELINE
# -----------------------------------------
def preprocess_image(image_bytes: bytes) -> Image.Image:
    """
    Full image preprocessing pipeline.
    """

    image = load_image(image_bytes)

    image = convert_to_rgb(image)

    image = resize_image(image)

    return image
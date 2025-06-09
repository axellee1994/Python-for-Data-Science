from PIL import Image
import numpy as np

def ft_load(path: str):
    try:
        img = Image.open(path)
        img_array = np.array(img)
        print("The shape of the image is:", img_array.shape)
        return img_array

    except FileNotFoundError:
        print(f"File {path} not found.")
        return None
    except IOError:
        print(f"Error opening file {path}.")
        return None

def main():
    path = input("Enter the path to the image file: ")
    image_array = ft_load(path)
    if image_array is not None:
        print("Image loaded successfully.")
    else:
        print("Failed to load image.")

if __name__ == "__main__" :
    main() 
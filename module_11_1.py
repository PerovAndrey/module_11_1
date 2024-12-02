from PIL import Image, ImageFilter
import numpy as np

image_path = "/Users/andrey_perov/Downloads/ключ.jpg"
image = Image.open(image_path)
new_size = (800, 600)
resized_image = image.resize(new_size)
blurred_image = resized_image.filter(ImageFilter.BLUR)
output_path = "ключ2.png"
blurred_image.save(output_path, format='PNG')
print(f"Изображение обработано и сохранено как {output_path}")

array = np.array([9, 8, 7, 6, 5, 1, 2, 3, 4, 5])
print("Исходный массив:")
print(array)

array_addition = array + 5
print("После сложения на 5:")
print(array_addition)

array_subtraction = array - 3
print("После вычитания 3:")
print(array_subtraction)

array_multiplication = array * 2
print("После умножения на 2:")
print(array_multiplication)

array_division = array / 2
print("После деления на 2:")
print(array_division)

array_power = array ** 2
print("После возведения в квадрат:")
print(array_power)
import tkinter as tk
import shape_area_calculator


def calculate_area():
    # Вычисление площади круга
    radius = float(radius_entry.get())
    circle_area = shape_area_calculator.compute_circle_area(radius)
    circle_result_label.config(text=f"Площадь круга: {circle_area}")

    # Вычисление площади треугольника
    side1 = float(side1_entry.get())
    side2 = float(side2_entry.get())
    side3 = float(side3_entry.get())
    triangle_area, is_right_triangle = shape_area_calculator.compute_triangle_area(side1, side2, side3)
    triangle_result_label.config(text=f"Площадь треугольника: {triangle_area}")
    triangle_type_label.config(text="Треугольник прямоугольный" if is_right_triangle else "Треугольник не прямоугольный")


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Вычисление площади фигур")

    radius_label = tk.Label(window, text="Радиус круга:")
    radius_label.pack()
    radius_entry = tk.Entry(window)
    radius_entry.pack()

    side1_label = tk.Label(window, text="Сторона 1 треугольника:")
    side1_label.pack()
    side1_entry = tk.Entry(window)
    side1_entry.pack()

    side2_label = tk.Label(window, text="Сторона 2 треугольника:")
    side2_label.pack()
    side2_entry = tk.Entry(window)
    side2_entry.pack()

    side3_label = tk.Label(window, text="Сторона 3 треугольника:")
    side3_label.pack()
    side3_entry = tk.Entry(window)
    side3_entry.pack()

    calculate_button = tk.Button(window, text="Вычислить площади", command=calculate_area)
    calculate_button.pack()

    circle_result_label = tk.Label(window, text="")
    circle_result_label.pack()

    triangle_result_label = tk.Label(window, text="")
    triangle_result_label.pack()

    triangle_type_label = tk.Label(window, text="")
    triangle_type_label.pack()

    window.mainloop()
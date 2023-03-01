
def BMI(w, h):
    bmi = w/(h**2)
    if bmi < 18.5:
        return("Underweight", bmi)
    elif 18.5 < bmi < 24.9:
        return("Normal Weight", bmi)
    elif 25 < bmi < 29.9:
        return("OverWeight", bmi)
    else:
        return ("Obese", bmi)

a, b = BMI(70, 1.6)
print("Chỉ số BMI là: ",b, "Tình Trạng cơ thể:",a)
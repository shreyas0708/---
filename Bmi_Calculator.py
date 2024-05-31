def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi <= 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi>=25.0 and bmi< 30:
        return "Overweight"
    else:
        return "Obese"
    

def main():
    try:
        weight = float(input("Enter weight in kilograms(kg): "))
        height = float(input("Enter height in meters(m): "))

        if weight <= 0 or height <= 0:
            print("Incorrect input! Weight and height must be greater than zero.")
        else:
            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)

            print(f"Body Masss Index is: {bmi:.2f}")
            print("8Category:", category)

    except ValueError:
        print("Invalid input! Weight and height must be numeric values.")

if __name__ == "__main__":
    main()

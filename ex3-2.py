try:
    hw = float(input("Enter Hours: "))
    rp = float(input("Enter Rate: "))
except:
    print("Error, please enter a numeric input")
    quit()
    if hw > 40:
        extrahours = float(hw - 40)
        pay = float((hw * rp) + (extrahours * (rp * 0.5)))
        print("Pay: ", pay)
    else:
        print("Pay: ", (hw * rp))

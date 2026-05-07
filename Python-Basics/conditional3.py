maths_score = 89
if maths_score > 90:
    print("A1")
elif maths_score > 80:
    print("A2")
else:
    print("B")
science_score = int(input("Enter your science score: "))
if science_score > 100 or science_score < 0:
    print("invalid input")
elif science_score >= 90:
    print("A1")
elif science_score >= 80:
    print("A2")
else:
    print("B")

science_score = int(input("Enter your science score:"))
math_score = int(input("Enter your math score:"))

if science_score > 100 or science_score < 0:
    print("invalid input")
if math_score > 100 or math_score < 0:
    print("invalid input")
elif science_score >= 90 and maths_score < 0:
    print ("You are a champ")
elif science_score >= 80 or (50 < math_score < 80):
    print("You are average")
elif 60 < science_score < 80 or (math_score < 80):
    print("You can be a math expert")
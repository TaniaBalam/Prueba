def exam_grade(score):
	if score > 95:
		grade = "Buen promedio"
	elif score >= 60:
		grade = "Pasas"
	else:
		grade = "No pasas"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail

print("Hola mundo")
print("Hola Tania")
print("Hello Misael")

print(5-2)

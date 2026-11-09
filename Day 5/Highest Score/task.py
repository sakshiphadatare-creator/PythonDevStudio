student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))
# #1st option
# print(sum(student_scores))
# #2nd option
# total_score = sum(student_scores)
# print("Total score : ",total_score)

sum = 0
for score in student_scores:
    sum += score
print(sum)

print(max(student_scores))
print(min(student_scores))

student_scores = [8, 65, 89, 86, 55, 91, 64, 89]
max_score  = 0
for score in student_scores :
    if score > max_score :
        max_score = score
print("max score : ",max_score)

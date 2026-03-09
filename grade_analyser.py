def process_scores(students):
  print(student_details)
  average_score = []
  for i in student_details.values():
    j = round(sum(i)/len(i),2)
    average_score.append(j)
  print(average_score)
  a,b,c = average_score
  print(a,b,c)
  averages = {"Alice": a, "Bob": b, "Clara": c}
  print(averages)
  return averages

def classify_grades(averages):
  for name, avg in averages.items():
    if avg >= 90:
      grade = 'A'
    elif avg >= 75 and avg < 90:
      grade = 'B'
    elif avg >= 60 and avg < 75 :
      grade = 'C'
    else:
      grade = 'F'
    averages[name]= (avg, grade)
  print(averages)
  return averages
def generate_report(classified):
  print("===== Student Grade Report =====")
  passed = 0
  failed = 0
  for name, (avg,grades) in classified.items():
    if grades == 'A' or 'B' or 'C':
      status = 'Pass'
      passed +=1
    else:
      status = 'Fail'
      failed +=1
    print(f"{name} | Avg: {avg} | Grade : {grades} | Status: {status}")
  print(f"Total Student : {len(classified)} ")
  print(f"Total students passed: {passed}")
  print(f"Total students failed: {failed}")


student_details = {"Alice": [88,86,85],
                   "Bob": [61,64,63],
                   "Clara": [95,98,96]}
average_score = process_scores(student_details)
classified = classify_grades(average_score)
passed_students = generate_report(classified)
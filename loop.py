attempts = 0
while attempts < 3:
   print("trying to connect...")
   attempts += 1

print("Done")


#distionary loops
scores={
   "ram": 85,
   "sham": 92,
   "sita": 78
}  
for student, score in scores.items():
   print(student, "scored", score)

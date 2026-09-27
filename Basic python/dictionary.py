"""
Dictionary-er lookup, insert, delete 
shob average case e 
O(1) — eta interview e onek kaje lage (jemon frequency count korte)
"""
student = {
    "name" : "Subrata",
    "age" : 15,
    "cgpa" : 3.5
}

# student["department"] = "CSE"
# print(f"Name ->  {student.get("name")}")
# print(f"Age -> {student.get("age")} ")

# del student["cgpa"]


# print(student)
for key, value in student.items():
    print(key, "->", value)
# Write a function `students_in_common` that takes two lists, `class1` and
# `class2` and returns a new list that contains only the students that are
# taking both classes
def students_in_common(class1, class2):
    return ### YOUR CODE HERE

############# Tests below (don't change these!) ############# 

history_class = ["Anna", "Beth", "Carol", "David", "Eli", "Fred", "Gina"]
math_class = ["Anna", "Carol", "Eli", "Fred", "Hal", "Ina", "Jeff"]
art_class = ["Anna", "David", "Hal", "Ina"]

print(students_in_common(history_class, math_class)) #Anna, Carol, Eli, Fred
print(students_in_common(history_class, art_class)) #Anna, David
print(students_in_common(art_class, math_class)) #Anna, Hal, Ina


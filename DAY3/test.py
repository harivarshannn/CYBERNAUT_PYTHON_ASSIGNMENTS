test_scores = [85, 90, 78, 92, 88]
average_score = sum(test_scores) / len(test_scores)
print(f"The average of the test scores is: {average_score:.2f}")
new_score = float(input("Please enter a new test score: "))
test_scores.append(new_score)
new_average_score = sum(test_scores) / len(test_scores)
print(f"The updated average of the test scores is: {new_average_score:.2f}")

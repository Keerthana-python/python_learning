# day = input("enter a day")
# match day.upper():
#     case "MONDAY":
#         print("first day of week")
# def replace_and_count(paragraph):
#     # Replacing 'is' with 'was'
#     updated_paragraph = paragraph.replace('is', 'was')
    
#     # Counting occurrences of 'a'
#     count_a = updated_paragraph.count('a')
    
#     return updated_paragraph, count_a

# paragraph = "This is a sample paragraph with a few words and a few letters."
# updated_paragraph, count_a = replace_and_count(paragraph)
# print(f"Updated Paragraph: {updated_paragraph}")
# print(f"Number of 'a': {count_a}")

def task1(paragraph):
    replaced_paragraph = paragraph.replace(" is ", " was ")
    a_count = replaced_paragraph.count('a')
    return replaced_paragraph, a_count
paragraph = "This is a simple task where we replace is with was."
replaced_paragraph, a_count = task1(paragraph)
print("Modified Paragraph:", replaced_paragraph)
print("Number of 'a's:", a_count)


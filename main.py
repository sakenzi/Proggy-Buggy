from collections import Counter

def check_plagiarism(line1: str, line2: str) -> str:
    if Counter(line1) == Counter(line2):
        return "PLAGIARISM"
    else:
        return "AUTHENTIC"

line1 = input().strip()
line2 = input().strip()
print(check_plagiarism(line1, line2))
# Use the file name mbox-short.txt as the file name
fh = open(r"D:\python\Coursera\Module 2 Data Structure\File\mbox-short.txt")

# Print file content
print(fh.read())

# Go back to start of file
fh.seek(0)

count = 0
total = 0.0

for line in fh:
    line = line.strip()
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.find(":")
        number = float(line[pos+1:].strip())
        total = total + number
        count = count + 1

avg = total / count
print("Average spam confidence:", avg)

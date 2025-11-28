#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

a = text.strip()
#print(a)

b = a[22:28]    # store the slice
#print(b)

c = b.strip()   
#print(c)

d = float(c)
print(f"{d:.4f}") 




text = "X-DSPAM-Confidence:    0.8475"

a = text.strip()

# find the position of the colon
pos = a.find(':')

# extract everything after the colon
b = a[pos+1:].strip()    # this gives "0.8475"

d = float(b)
print(f"{d:.4f}")

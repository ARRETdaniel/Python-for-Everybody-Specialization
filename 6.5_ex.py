text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
pe = text[pos+1:]
print(float(pe))

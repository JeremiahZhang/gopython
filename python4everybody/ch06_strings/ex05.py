text = "X-DSPAM-Confidence:    0.8475";

num_pos = text.find('0')
num = text[num_pos:]

num = float(num)

print(num)

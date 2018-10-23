import re
text = "Here is some text that contains something."
pattern = "that"
if re.search(pattern, text):
    print("Yes,%s  was found in the text" %pattern)
else:
            print("No, %s was not found in the text" % pattern)

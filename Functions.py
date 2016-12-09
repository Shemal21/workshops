__author__ = 'jc350024'
"""
"""

text = "Merry Christmas"
print(text[:5]+text[6:12])

y, x = 5, "Yay"
try:
    result = x*y
    print(result)
except ValueError:
    print("value")
except TypeError:
    print("type")
except:
    print("other")


def inch_to_meter(inch):
    return inch*0.0254

print(inch_to_meter(10))

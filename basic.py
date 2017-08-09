
def draw(arr):
    for x in arr:
        print "*" * x

nums = [18, 2, 29, 11, 5, 20]
draw(nums)

def stars(arr):
    for x in arr:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length

x = [10, "Braden", 2, "Ashley", "KeiLani Utu", 8]
stars(x)

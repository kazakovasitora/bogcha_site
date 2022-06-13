from django.core.exceptions import ValidationError

def rasm_olchami(img):
    width = img.width
    height = img.height
    if width > 300:
        raise ValidationError("Maximum Uzunlik 300px")
    if height > 300:
        raise ValidationError("Maximum Balandlik 300px")
    
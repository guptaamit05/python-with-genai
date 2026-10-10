import module_assignment.math_utils as math_utils
from module_assignment.math_utils import square
from module_assignment.string_utils import capitalize_words,reverse_string,word_count
import shop_package.discount as disc
from shop_package.billing import calculate_total

a = 20
b = 10
s = 4
text ="hello i am a good boy"
print(f"addition of {a} and {b}: {math_utils.add(a,b)}")
print(f"subtraction {a} and {b}: {math_utils.subtract(a,b)}")
print(f"square of {s} : {square(s)}")
print("="*20)


# capitalize_words,reverse_string,word_count
print(capitalize_words(text))
print(reverse_string(text))
print(word_count(text))
print("="*20)


# apply_discount, display_total
print(disc.apply_discount(1000, 10))
print(calculate_total([100,200,300]))

from app.groww.client import groww
import inspect

print(inspect.signature(groww.get_option_chain))
print()

print(groww.get_option_chain.__doc__)
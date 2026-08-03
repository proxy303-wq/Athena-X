from app.groww.client import groww

print("=" * 60)
print("ATHENA X - GROWW SDK METHODS")
print("=" * 60)

methods = [m for m in dir(groww) if not m.startswith("_")]

for method in sorted(methods):
    print(method)
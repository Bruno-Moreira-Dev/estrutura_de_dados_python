linguagens = ["python", "java", "js", "c", "c#"]

linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

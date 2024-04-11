import compiler
import preprocessor
a=input()
b=preprocessor.preprocessor()
d=a.split(" ")
a=d[0]
if d[1]=="-obj":
    b.directives(a+" true")
elif d[1]=="-0":
    b.directives(a+" false")
c=compiler.compilerGold()
c.run(a)

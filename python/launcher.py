import compiler
import preprocessor
a=input()
b=preprocessor.preprocessor()
d=a.split(" ")
a=d[0]
if d[1]=="-1":
    b.directives(a+" true")
elif d[1]=="-0":
    b.directives(a+" false")
c=compiler.compilerGold()
if d[2]=="-java":
    c.run(a,"java")
elif d[2]=="-fort":
    c.run(a,"fortran")
elif d[2]=="-cpp":
    c.run(a,"c_plus_plus")
elif d[2]=="-cpp_header":
    c.run(a,"c_plus_plus_header")
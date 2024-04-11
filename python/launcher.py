import compiler
import preprocessor
a=input()
b=preprocessor.preprocessor()
b.directives(a+" no")
c=compiler.compilerGold()
c.run(a)

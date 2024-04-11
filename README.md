This is a compiler and preprocessor for simple programming language

can compile to:
* java

simple hello world program in file test.gold:

     class start function void main String[]\_args start sysout << "Hello\_world" ; end end
equivalent multi-line program:

     class start
     function void main String[]\_args start
     sysout << "Hello\_world" ;
     end
     end
equivalent program with preprocessor directives:

     #start_def main
     function void main String[]\_args start
     #end_def
     class start
     #put main
     sysout << "Hello\_world" ;
     end
     end
resultant java code:

     public class test{
       public static void main(String[] args){
         System.out.print("Hello world");
      }
    }
if you want to use the preprocessor than it has to be muiltiple lines.

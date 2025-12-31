#include "compiler.h"
int main(int argc,char** argv){
    return aurum::compiler::compile_sequence(aurum::shared::utils::get_args(argc,argv));
}
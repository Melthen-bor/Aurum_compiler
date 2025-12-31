#ifndef AURUM_COMPILER_FILE
#define AURUM_COMPILER_FILE
#include "shared.h"
#include <sstream>
namespace aurum{
    namespace compiler{
        namespace internals{
            extern std::string global_path;
            extern std::string code_path;
            extern std::string generated_code_path;
            extern std::string generated_header_path;
            //extern std::vector<std::string> generated_files;
            extern shared::integers::nat max_errors;
            namespace old{
                struct value{
                    std::string type;
                    int is_ptr:1;
                    int auto_ptr:1;
                    int unused:6;
                    int ptr_level;
                    bool operator ==(value&);
                };
                struct variable: public value{
                    std::string name;
                    bool of_type(value&);
                };
                struct function{
                    std::string name;
                    std::vector<variable> args;
                    value return_value;
                    int no_discard:1;
                    int mangling:1;
                    int imported:1;
                    int use_varargs:1;
                    int unused:4;
                    function(std::string);
                    // Used to get the actual name of the function
                    // Ex:
                    //  Aurum Function Declaration:
                    //      function test(u64,u8 &* &*,varargs) u64;
                    //  C Function Declaration:
                    //      With Mangling:
                    //          uint64_t testæu64ƿu8þþævarargs(uint64_t,uint8_t**,...);
                    //      Sans Mangling:
                    //          uint64_t test(uint64_t,uint8_t**,...);
                    std::string get_internal_name();
                    bool is_same_func(std::string,std::vector<value>);
                };
                struct struct_{
                    std::string name;
                    std::vector<variable> fields;
                };
                struct class_: public struct_{
                    std::vector<function> methods;
                };
                struct builtin_type{
                    std::string name;
                    std::string compilation;
                };
                class token_eater{
                    std::vector<lexer::token> tkns;
                    shared::integers::nat location;
                public:
                    token_eater();
                    token_eater(std::vector<lexer::token>);
                    shared::optional<lexer::token> peek();
                    lexer::token consume();
                };
                enum class scope_type: shared::integers::byte{
                    NORMAL,
                    FUNCTION,
                    CLASS,
                    STRUCT
                };
                struct scope{
                    std::vector<variable> vars;
                    scope_type type;
                };
                class macro{
                    std::string name;
                    std::vector<std::string> args;
                    std::vector<lexer::token> tkns;
                    bool is_arg(lexer::token&);
                    shared::integers::nat which_arg(lexer::token&);
                public:
                    macro(std::string);
                    void push_arg(std::string);
                    void push_tkn(lexer::token);
                    shared::integers::nat argc();
                    shared::integers::nat size();
                    token_eater get_tkns(std::vector<lexer::token>);
                };
                class compiler{
                    std::vector<std::string> data_types;
                    std::vector<function> funcs;
                    std::vector<variable> global_vars;
                    std::vector<struct_> structs;
                    std::vector<class_> classes;
                    std::vector<builtin_type> builtins;
                    std::vector<variable> type_defs;
                    std::vector<std::string> imports;
                    std::vector<macro> macros;
                    shared::integers::nat error_count;
                    shared::integers::byte use_varargs;
                    void report_error(std::string);
                    std::vector<variable> compile_arguments(token_eater&);
                    std::string get_type_name(std::string&);
                    std::string get_compiled_arguments(const std::vector<variable>&, bool);
                    bool is_type(std::string&);
                    bool is_global_var(std::string&);
                    std::vector<variable> compile_used_arguments(token_eater&,std::vector<scope>*);
                    //Takes ptrs to environment variables
                    void compile_tkn_stream(token_eater,shared::integers::nat,...);
                public:
                    compiler();
                    void use_flag(std::string);
                    // First argument is the file name
                    // Second argument should be false in most cases
                    void compile(std::string, bool);
                };
            };
        };
        shared::integers::byte compile_sequence(std::vector<std::string>);
    };
};
#endif
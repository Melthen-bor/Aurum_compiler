#include "compiler.h"
#include <stdargs.h>
/*
    READ THIS BEFORE MODIFYING THIS CODE
    There are Functions in this code that can throw std::string
    This is to idiot-proof these functions
*/
std::string aurum::compiler::internals::global_path;
std::string aurum::compiler::internals::code_path;
std::string aurum::compiler::internals::generated_code_path;
std::string aurum::compiler::internals::generated_header_path;
aurum::shared::integers::nat aurum::compiler::internals::max_errors;
bool aurum::compiler::internals::old::value::operator==(value& other){
    if(!(other.type==this->type)) return false;
    if(!(other.is_ptr==this->is_ptr)) return false;
    if(!(other.ptr_level==this->ptr_level)) return false;
}
aurum::compiler::internals::old::function::function(std::string name){
    this->name=name;
    this->args=std::vector<variable>();
    this->return_value=value();
    this->no_discard=0;
    this->mangling=0;
    this->use_varargs=0;
    this->imported=0;
}
std::string aurum::compiler::internals::old::function::get_internal_name(){
    if(!this->mangling) return this->name;
    std::string out=name;
    out.append("æ");
    for(int i=0;i<this->args.size();i++){
        out.append(this->args.at(i).type);
        if(this->args.at(i).is_ptr) for(int j=0;j<this->args.at(i).ptr_level;j++) out.append("þ");
        if(!(i==this->args.size()-1)) out.append("ƿ");
    }
    if(this->use_varargs) out.append("ævarargs");
    return out;
}
bool aurum::compiler::internals::old::function::is_same_func(std::string name,std::vector<value>& arg_types){
    if(!this->mangling) return this->name==name;
    if(!(this->name==name)) return false;
    if(arg_types.size()<this->args.size()) return false;
    for(int i=0;i<this->args.size();i++) if(!(arg_types.at(i)==this->args.at(i))) return false;
    if(!((arg_types.size()>this->args.size())&&this->use_varargs)) return false;
    return true;
}
aurum::compiler::internals::old::token_eater::token_eater(){
    this->tkns=std::vector<lexer::token>();
    this->location=0;
}
aurum::compiler::internals::old::token_eater::token_eater(std::vector<lexer::token> tokns){
    this->tkns=tokns;
    this->location=0;
}
aurum::shared::optional<lexer::token> aurum::compiler::internals::old::token_eater::peek(){
    return (this->location<this->tkns.size())?this->tkns.at(this->location):shared::optional<lexer::token>();
}
aurum::lexer::token aurum::compiler::internals::old::token_eater::consume(){
    if(this->location==this->tkns.size()) throw std::string("Internal Compiler Function[aurum::compiler::internals::old::token_eater::consume] is misused");
    return this->tkns.at(this->location++);
}
bool aurum::compiler::internals::old::macro::is_arg(lexer::token& tkn){
    if(tkn.type==shared::lexer::token_type::ID) for(int i=0;i<this->argc();i++) if(this->args.at(i)==tkn.val) return true;
    return false;
}
aurum::shared::integers::nat aurum::compiler::internals::old::macro::which_arg(lexer::token& tkn){
    for(int i=0;i<this->argc();i++) if(this->args.at(i)==tkn.val) return i;
    throw std::string("Internal Compiler Function[aurum::compiler::internals::old::macro::which_arg] is misused");
}
aurum::compile::internals::old::macro::macro(std::string name){
    this->name=name;
    this->args=std::vector<std::string>();
    this->tkns=std::vector<lexer::token>();
}
void aurum::compiler::internals::old::macro::push_arg(std::string arg){
    this->args.push_back(arg);
}
void aurum::compiler::internals::old::macro::push_tkn(lexer::token tkn){
    this->tkns.push_back(tkn);
}
aurum::shared::integers::nat aurum::compiler::internals::old::macro::argc(){
    return this->args.size();
}
aurum::shared::integers::nat aurum::compiler::internals::old::macro::size(){
    return this->tkns.size();
}
aurum::compiler::internals::old::token_eater aurum::compiler::internals::old::macro::get_tkns(std::vector<lexer::token> args){
    if(!(args.size()==this->argc())) throw std::string("Internal Compiler Function[aurum::compiler::internals::old::macro::get_tkns] is misused");
    return (!this->size())?token_eater():token_eater([&args,this](){std::vector<lexer::token> buf;for(int i=0;i<this->size();i++) buf.push_back(this->is_arg(this->tkns.at(i))?args.at(this->which_arg(this->tkns.at(i))):this->tkns.at(i));return buf;}());
}
void aurum::compiler::internals::old::compiler::report_error(std::string msg){
    if(this->error_count==max_errors) std::exit(1);
    std::cerr<<"\033[31mError: "<<msg<<"\033[0m"<<std::endl;
    this->error_count++;
}
std::string aurum::compiler::internals::old::compiler::get_type_name(std::string& type_name){
    for(int i=0;i<this->builtins.size();i++) if(this->builtins.at(i).name==type_name) return this->builtins.at(i).compilation;
    return type_name
}
std::string aurum::compiler::internals::old::compiler::get_compiled_arguments(const std::vector<variable>& args,bool include_name){
    std::string out;
    for(int i=0;i<args.size();i++){
        if(i) out.push_back(',');
        out+=args.at(i).type;
        if(include_name){
            out.push_back((char)32);
            out+=args.at(i).name;
        }
    }
    return out;
}
bool aurum::compiler::internals::old::compiler::is_type(std::string& type_name){
    for(int i=0;i<this->data_types.size()) if(this->data_types.at(i).name==type_name) return true;
    return false;
}
bool aurum::compiler::internals::old::compiler::is_global_var(std::string& name){
    for(int i=0;i<this->globals_vars.size();i++) if(this->global_vars.at(i).name==name) return true;
    return false;
}
std::vector<aurum::compiler::internals::old::variable> aurum::compiler::internals::old::compiler::compile_arguments(token_eater& tkns){
    std::vector<variable> out;
    lexer::token temp;
    while(tkns.peek()){
        temp=tkns.consume();
        switch(temp.type){
        case lexer::token_type::END_ARGS:
            return out;
        case lexer::token_type::ID:
            if(!(this->is_type(temp.val))) this->report_error("Expected Type");
            out.push_back(variable());
            out.back().type=temp.val;
            if(tkns.peek()&&tkns.peek().type==lexer::token_type::ID) if(this->is_type(tkns.peek().val)) out.back().name=tkns.consume().val;
            else this->report_error("Expected Type");
            if(!(tkns.peek().type==lexer::token_type::ARG_SEPERATOR)) this->report_error("Expected Argument Separator");
            tkns.consume();
            break;
        case lexer::token_type::VARARGS:
            this->use_varargs=true;
        case lexer::token_type::ARG_SEPERATOR:
            break;
        default:
            this->report_error("Invalid Token in Argument List");
        }
    }
}
std::vector<aurum::compiler::internals::old::variable> aurum::compiler::internals::old::compiler::compile_used_arguments(token_eater& tkns,std::vector<scope>* scopes){
    std::vector<variable> out;
    lexer::token temp;
    while(tkns.peek()){
        temp=tkns.consume();
        switch(temp.type){
        case lexer::token_type::END_ARGS:
            return out;
        case lexer::token_type::ID:
            if(!(this->))
        }
    }
}
#define FIRST_COMPILE_TKN_STREAM_VERSION 0
#define MINIMUM_FOR_FUNCTIONS 1
#define MINIMUM_FOR_STRUCTS 2
#define MINIMUM_FOR_NO_DISCARD 3
#define LATEST_COMPILE_TKN_STREAM_VERSION 3
void aurum::compiler::internals::old::compiler::compile_tkn_stream(token_eater tkns,shared::integers::nat version,...){
    if(this->use_varargs) this->report_error("Unexpected Internal Value");
    va_list var_args;
    va_start(var_args,version);
    std::string_stream* file=nullptr;
    std::string_stream* header=nullptr;
    bool* create_header=nullptr;
    bool* create_bin=nullptr;
    bool* auto_mode=nullptr;
    bool* global_library=nullptr;
    bool* mangle=nullptr;
    bool* in_class=nullptr;
    bool* account_for_function=nullptr;
    bool* in_function=nullptr;
    std::vector<scope>* scopes=nullptr;
    bool imported=false;
    bool* in_struct=nullptr;
    bool* no_discard_mode=nullptr;
    if(version>LATEST_COMPILE_TKN_STREAM_VERSION) throw std::string("Internal Compiler Function[aurum::compiler::internals::old::compiler::compile_tkn_stream] is misused");
    // Version 0
    file=va_arg(var_args,std::string_stream*);
    header=va_arg(var_args,std::string_stream*);
    create_header=va_arg(var_args,bool*);
    create_bin=va_arg(var_args,bool*);
    auto_mode=va_arg(var_args,bool*);
    global_library=va_arg(var_args,bool*);
    mangle=va_arg(var_args,bool*);
    in_class=va_arg(var_args,bool*);
    account_for_function=va_arg(var_args,bool*);
    in_function=va_arg(var_args,bool*);
    scopes=va_arg(var_args,std::vector<scope>*);
    if(!version) goto end;
    // Version 1
    imported=va_arg(var_args,bool);
    if(version==1) goto end;
    // Version 2
    in_struct=va_arg(var_args,bool*);
    if(version==2) goto end;
    // Version 3
    no_discard_mode=va_arg(var_args,bool*);
    //if(version==3) goto end;
    end:
    va_end(var_args);
    lexer::token temp;
    while(!tkns.peek()){
        temp=tkns.consume();
        switch(temp.type){
        case lexer::token_type::IMPORT:
            if(!(scopes->size())) this->report_error("Imports are not allowed in scopes");
            if(!(tkns.peek().type==lexer::token_type::ID)) this->report_error("Expected Token of Type:ID");
            temp=tkns.consume();
            for(int i=0;i<this->imports.size();i++) if(this->imports.at(i)==temp.val) break;
            (*header)<<"#include "<<((*global_library)?'<':'"')<<temp.val<<".h"<<((*global_library)?'>':'"')<<'\n';
            this->imports.push_back(temp.val);
            if(!(tkns.peek().type==lexer::token_type::END_STATEMENT)) this->report_error("Expected Token of Type:END_STATEMENT");
            tkns.consume();
            this->compile(temp.val, *global_library);
            break;
        case lexer::token_type::COMPILER_TAG:
            if(temp.val=="NO_HEADER") (*create_header)=false;
            else if(temp.val=="AUTO") (*auto_mode)=true;
            else if(temp.val=="MANUAL") (*auto_mode)=false;
            else if(temp.val=="GLOBAL") (*global_library)=true;
            else if(temp.val=="LOCAL") (*global_library)=false;
            else if(temp.val=="MANGLE") (*mangle)=true;
            else if(temp.val=="NO_MANGLE") (*mangle)=false;
            else if(temp.val=="NO_BIN") (*create_bin)=false;
            else if(temp.val=="PLACE_MACRO"){
                if(!((!tkns.peek())&&(tkns.peek().type==lexer::token_type::ID))) this->report_error("Expected Token of Type:ID");
                temp=tkns.consume();
                std::vector<lexer::token> temp_tkns;
                if((!tkns.peek())&&(tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="START_MACRO_ARGS")){
                    tkns.consume();
                    while((!tkns.peek())&&(!(tkns.peek().type==lexer::token_type::COMPILER_TAG))&&(!(tkns.peek().val=="STOP_MACRO_ARGS")) temp_tkns.push_back(tkns.consume());
                    if(!(!tkns.peek())) this->report_error("Expected Token");
                    tkns.consume();
                }
                bool macro_found=false;
                for(int i=0;i<this->macros.size();i++) if(this->macros.at(i).name==temp.val) i=(this->compile_tkn_stream((macro_found=true,this->macros.at(i).get_tkns(temp_tkns)),
                    version,file,header,create_header,
                    create_bin,auto_mode,global_library,
                    mangle,in_class,account_for_function,
                    in_function,scope,imported,in_struct,
                    no_discard_mode
                ),this->macros.size());
                if(!macro_found) this->report_error("Macro["+temp.val+"] does not exist");
            } else if(temp.val=="DEFINE"){
                if(!((!tkns.peek())&&(tkns.peek().type==lexer::token_type::ID))) this->report_error("Expected Token of Type:ID");
                temp=tkns.consume();
                for(int i=0;i<this->macros.size();i++) if(this->macros.at(i).name==temp.val) this->report_error("Redefinition of Macro["+temp.val+"]");
                this->macros.push_back(macro(temp.val));
                if(!(!tkns.peek())) this->report_error("Expected Token");
                if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="START_MACRO_ARGS")) while((!tkns.peek())&&(!((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="STOP_MACRO_ARGS")))){
                    temp=tkns.consume();
                    if(!(temp.type==lexer::token_type::ID)) this->report_error("Expected Token of Type:ID");
                    this->macros.back().push_arg(temp.val);
                }
                if(!(!tkns.peek())) this->report_error("Expected Token");
                tkns.consume();
                while((!tkns.peek())&&(!((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="ENDDEF")))){
                    temp=tkns.consume();
                    this->macros.back().push_tkn(temp);
                }
                if(!(!tkns.peek())) this->report_error("Expected Token");
                tkns.consume();
            } else if(temp.val=="IFNDEF"){
                if(!((!tkns.peek())&&(tkns.peek().type==lexer::token_type::ID))) this->report_error("Expected Token of Type:ID");
                temp=tkns.consume();
                bool macro_found=false;
                for(int i=0;i<this->macros.size();i++) if(this->macros.at(i).name==temp.val) macro_found=true;
                int macro_scope=1;
                if(macro_found) {while((!tkns.peek())&&macro_scope){
                    if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="IFDEF")) macro_scope++;
                    else if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="IFNDEF")) macro_scope++;
                    else if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="ENDIF")) macro_scope--;
                    tkns.consume();
                }} else{
                    std::vector<lexer::token> temp_tkns=std::vector<lexer::token>();
                    while((!tkns.peek())&&macro_scope){
                        if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="IFDEF")) macro_scope++;
                        else if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="IFNDEF")) macro_scope++;
                        else if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="ENDIF")) macro_scope--;
                        if(macro_scope) temp_tkns.push_back(tkns.consume());
                        else tkns.consume();
                    }
                    this->compile_tkn_stream(token_eater(temp_tkns),version,file,header,create_header,
                        create_bin,auto_mode,global_library,
                        mangle,in_class,account_for_function,
                        in_function,scope,imported,in_struct,
                        no_discard_mode
                    );
                }
            } else if(temp.val=="IFDEF"){
                if(!((!tkns.peek())&&(tkns.peek().type==lexer::token_type::ID))) this->report_error("Expected Token of Type:ID");
                temp=tkns.consume();
                bool macro_found=false;
                for(int i=0;i<this->macros.size();i++) if(this->macros.at(i).name==temp.val) macro_found=true;
                int macro_scope=1;
                if(!macro_found) {while((!tkns.peek())&&macro_scope){
                    if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="IFDEF")) macro_scope++;
                    else if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="IFNDEF")) macro_scope++;
                    else if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="ENDIF")) macro_scope--;
                    tkns.consume();
                }} else{
                    std::vector<lexer::token> temp_tkns=std::vector<lexer::token>();
                    while((!tkns.peek())&&macro_scope){
                        if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="IFDEF")) macro_scope++;
                        else if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="IFNDEF")) macro_scope++;
                        else if((tkns.peek().type==lexer::token_type::COMPILER_TAG)&&(tkns.peek().val=="ENDIF")) macro_scope--;
                        if(macro_scope) temp_tkns.push_back(tkns.consume());
                        else tkns.consume();
                    }
                    this->compile_tkn_stream(token_eater(temp_tkns),version,file,header,create_header,
                        create_bin,auto_mode,global_library,
                        mangle,in_class,account_for_function,
                        in_function,scope,imported,in_struct,
                        no_discard_mode
                    );
                }
            } else if(temp.val=="NO_DISCARD") if(version<MINIMUM_FOR_NO_DISCARD) this->report_error("No Discard may not be used") else (*no_discard_mode)=true;
            else if(temp.val=="MAY_DISCARD") if(version<MINIMUM_FOR_NO_DISCARD) this->report_error("May Discard may not be used") else (*no_discard_mode)=false;
            break;
        case lexer::token_type::FUNCTION:
            if(*in_function) this->report_error("Functions can not be defined inside functions");
            if(!(*in_class)){
                if(!(tkns.peek().type==lexer::token_type::ID)) this->report_error("Expected Token of Type:ID");
                temp=tkns.consume();
                if(!(tkns.peek().type==lexer::token_type::START_ARGS)) this->report_error("Expected Token of Type:START_ARGS");
                tkns.consume();
                this->funcs.push_back(function(temp.val));
                this->funcs.back().args=compile_arguments(tkns);
                this->funcs.back().imported=imported;
                this->funcs.back().mangling=(*mangle);
                this->funcs.back().use_varargs=this->use_varargs;
                if(version<3) this->funcs.back().no_discard=false;
                else this->funcs.back().no_discard=(*no_discard_mode);
                if(!(tkns.peek().type==lexer::token_type::ID)) this->report_error("Expected Token of Type:ID");
                temp=tkns.consume();
                this->funcs.back().return_value.type=temp.val;
                if(tkns.peek().type==lexer::token_type::POINT_OP){
                    this->funcs.back().return_value.is_ptr=true;
                    this->funcs.back().return_value.auto_ptr=(*auto_mode);
                }
                while(tkns.peek().type==lexer::token_type::POINT_OP){
                    this->funcs.back().return_value.ptr_level++;
                    tkns,.consume();
                }
                (*header)<<this->get_type_name(this->funcs.back().return_value.type);
                for(int i=0;i<this->funcs.back().return_value.ptr_level;i++) (*header)<<"*";
                (*header)<<' '<<this->funcs.back().get_internal_name()<<'(';
                (*header)<<this->get_compiled_arguments(this->funcs.back().args,false);
                if(this->funcs.back().use_varargs) (*header)<<", ...";
                (*header)<<");\n";
                if(tkns.peek().type==lexer::token_type::END_STATEMENT){
                    tkns.consume();
                    break;
                }
                (*file)<<this->get_type_name(this->funcs.back().return_value.type);
                for(int i=0;i<this->funcs.back().return_value.ptr_level;i++) (*file)<<"*";
                (*file)<<' '<<this->funcs.back().name<<'(';
                (*file)<<this->get_compiled_arguments(this->funcs.back().args,true);
                if(this->funcs.back().use_varargs) (*file)<<", ...";
                (*file)<<')';
                if(!(tkns.peek().type==lexer::token_type::START)) this->report_error("Expected Token of Type:START");
                if(this->funcs.back().use_varargs) (*account_for_function)=true;
            } else this->report_error("classes are not supported yet");
            break;
        case lexer::token_type::PROCEDURE:
            if(*in_function) this->report_error("Functions can not be defined inside functions");
            if(!(*in_class)){
                if(!(tkns.peek().type==lexer::token_type::ID)) this->report_error("Expected Token of Type:ID");
                temp=tkns.consume();
                if(this->is_type(temp.val)) this-.report_error("ID is a Type");
                if(!(tkns.peek().type==lexer::token_type::START_ARGS)) this->report_error("Expected Token of Type:START_ARGS");
                tkns.consume();
                this->funcs.push_back(function(temp.val));
                this->funcs.back().args=compile_arguments(tkns);
                this->funcs.back().imported=imported;
                this->funcs.back().mangling=(*mangle);
                this->funcs.back().use_varargs=this->use_varargs;
                this->funcs.back().no_discard=false;
                this->funcs.back().return_value.type="u0";
                (*header)<<"u0 "<<this->funcs.back().get_internal_name()<<'(';
                (*header)<<this->get_compiled_arguments(this->funcs.back().args,false);
                if(this->funcs.back().use_varargs) (*header)<<", ...";
                (*header)<<");\n";
                if(tkns.peek().type==lexer::token_type::END_STATEMENT){
                    tkns.consume();
                    break;
                }
                (*file)<<"u0 "<<this->funcs.back().name<<'(';
                (*file)<<this->get_compiled_arguments(this->funcs.back().args,true);
                if(this->funcs.back().use_varargs) (*file)<<", ...";
                (*file)<<')';
                if(!(tkns.peek().type==lexer::token_type::START)) this->report_error("Expected Token of Type:START");
                if(this->funcs.back().use_varargs) (*account_for_function)=true;
            } else this->report_error("classes are not supported yet");
            break;
        case lexer::token_type::VARARGS:
            if(!(*in_function)) this->report_error("Must be in function to use Variable Arguments");
            if(!(this->funcs.back().use_varargs)) this->report_error("Function["+this->funcs.back().name+"] must use Variable Arguments");
            (*file)<<"va_arg(aurum_internal_local_variable_arguments,";
            if(!(tkns.peek().type==lexer::token_type::AS)) this->report_error("Expected Token of Type:AS");
            tkns.consume();
            if(!(tkns.peek().type==lexer::token_type::ID)) this->report_error("Expected Token of Type:ID");
            temp=tkns.consume();
            if(!(this->is_type(temp.val))) this->report_error("Expected type name");
            (*file)<<this->get_type_name(temp.val)<<')';
            break;
        case lexer::token_type::START:
            scopes->push_back(scope());
            (*file)<<"{\n";
            if(*account_for_function){
                scopes->back().type=scope_type::FUNCTION;
                (*in_function)=true;
                if(this->funcs.back().use_varargs){
                    if(!this->funcs.back().args.size()) this->report_error("Variable Arguments can not be the only arguments");
                    (*file)<<"va_list aurum_internal_local_variable_arguments;\n";
                    (*file)<<"va_start(aurum_internal_local_variable_arguments,"<<this->funcs.back().args.back().name<<");\n";
                }
                (*account_for_function)=false;
            }
            break;
        case lexer::token_type::END:
            if(!scopes->size()) report_error("There is no scope to end");
            if(*in_function) if(scopes->back().type==scope_type::FUNCTION){
                if(this->funcs.back().use_varargs) (*file)<<"va_end(aurum_internal_local_variable_arguments);\n";
                (*in_function)=false;
            }
            scopes->pop_back();
            (*file)<<"}\n";
            break;
        case lexer::token_type::TYPEDEF:
            if(scopes->size()) this->report_error("No Typedefs in Scopes");
            if(!(!tkns.peek())) this->report_error("Expected Token");
            if(!(tkns.peek().type==lexer::token_type::ID)) this->report_error("Expected Token of Type:ID");
            temp=tkns.consume();
            if(this->is_type(temp.val)) this->report_error("ID is a Type");
            this->data_types.push_back(temp.val);
            this->type_defs.push_back(variable());
            this->type_defs.back().name=temp.val;
            if(!(!tkns.peek())) this->report_error("Expected Token");
            if(!(tkns.peek().type==lexer::token_type::AS)) this->report_error("Expected Token of Type:AS");
            tkns.consume();
            if(!(!tkns.peek())) this->report_error("Expected Token");
            if(!(tkns.peek().type==lexer::token_type::ID)) this->report_error("Expected Token of Type:ID");
            temp=tkns.consume();
            this->type_defs.back().type=temp.val;
            if(!(!tkns.peek())) this->report_error("Expected Token");
            this->type_defs.back().is_ptr=(tkns.peek().type==lexer::token_type::POINT_OP);
            while((!tkns.peek())&&(tkns.peek().type==lexer::token_type::POINT_OP)) (tkns.consume(),this->type_defs.back().ptr_level++);
            if(!(!tkns.peek())) this->report_error("Expected Token");
            if(!(tkns.peek().type==lexer::token_type::END_STATEMENT)) this->report_error("Expected Token of Type:END_STATEMENT");
            tkns.consume();
            header<<"typedef ";
            header<<this->type_defs.back().type;
            if(this->type_defs.back().is_ptr) for(int i=0;i<this->type_defs.back().ptr_level;i++) header<<'*';
            header<<' ';
            header<<this->type_defs.back().name;
            header<<";\n";
            break;
        case lexer::token_type::END_STATEMENT:
            file<<";\n";
            break;
        case lexer::token_type::ID:
            if(scopes->size){
                if(this->is_type(temp.val)){
                    if(!in_function) this->report_error("Local Variables must be in Functions");
                    this->scopes.back().vars.push_back(variable());
                    this->scopes.back().vars.back().type=temp.val;
                    if(!(!tkns.peek())) this->report_error("Expected Token");
                    this->scopes.back().vars.back().is_ptr=(tkns.peek().type==lexer::token_type::POINT_OP);
                    while((!tkns.peek())&&(tkns.peek().type==lexer::token_type::POINT_OP)) (tkns.consume(),this->scopes.back().vars.back().ptr_level++);
                    if(!((!tkns.peek()))&&(tkns.peek().type==lexer::token_type::ID)) this->report_error("Expected Token of Type:ID");
                    this->scopes.back().vars.back().name=tkns.consume().val;
                    file<<this->scopes.back().vars.back().type;
                    if(this->scopes.back().vars.back().is_ptr) for(int i=0;i<this->scopes.back().vars.back().ptr_level;i++) file<<'*';
                    file<<' ';
                    file<<this->scopes.back().vars.back().name;
                } else if(this->is_global_var(temp.val)){
                    if(!in_function) this->report_error("Variables can only be referenced in Functions");
                    int i;
                    for(i=0;i<this->global_vars.size();i++) if(this->global_vars.at(i).name==temp.val) break;
                    if(!(i<this->global_vars.size())) this->report_error("Could not find global variable");
                    file<<this->global_vars.at(i).name;
                } else{
                    for(int i=((*in_class)?1:0);i<this->scopes.size();i++) for(int j=0;j<this->scopes.at(i).vars.size();j++) if(this->scopes.at(i).vars.at(j).name==temp.val) goto local_variable;

                    for(int i=0;i<this->scopes.size();i++)
                    break;
                    local_variable:
                        file<<temp.val;
                }
            } else{
                if(!(this->is_type(temp.val))) this->report_error("Function calls must be inside scopes");
                this->global_vars.push_back(variable());
                this->global_vars.back().type=temp.val;
                if(!(!tkns.peek())) this->report_error("Expected Token");
                this->global_vars.is_ptr=(tkns.peek().type==lexer::token_type::POINT_OP);
                while((!tkns.peek())&&(tkns.peek().type==lexer::token_type::POINT_OP)) (tkns.consume(),this->global_vars.back().ptr_level++);
                if(!((!tkns.peek())&&(tkns.peek().type==lexer::token_type::ID))) this->report_error("Expected Token of Type:ID");
                this->global_vars.back().name=tkns.consume().val;
                header<<"extern ";
                header<<this->global_vars.back().type;
                if(this->global_vars.back().is_ptr) for(int i=0;i<this->global_vars.back().ptr_level;i++) header<<'*';
                header<<' ';
                header<<this->global_vars.back().name;
                header<<";\n";
                file<<this->global_vars.back().type;
                if(this->global_vars.back().is_ptr) for(int i=0;i<this->global_vars.back().ptr_lexel;i++) file<<'*';
                file<<' ';
                file<<this->global_vars.back().name;
            }
            break;
        default:
            this->report_error("Unexpected Token");
        }
    }
}
aurum::compiler::internals::old::compiler::compiler(){
    this->data_types=std::vector<std::string>();
    this->imports=std::vector<std::string>();
    this->builtins=std::vector<builtin_type>();
    this->error_count=0;
    this->data_types.push_back("u0");
    this->data_types.push_back("u8");
    this->data_types.push_back("u16");
    this->data_types.push_back("u32");
    this->data_types.push_back("u64");
    this->data_types.push_back("i0");
    this->data_types.push_back("i8");
    this->data_types.push_back("i16");
    this->data_types.push_back("i32");
    this->data_types.push_back("i64");
    for(int i=0;i<this->data_types.size();i++){
        if((i==0)||(i==5)){
            this->builtins.push_back(builtin_type{this->data_types.at(i),"void"});
            continue;
        }
        std::string name=std::string();
        if(this->data_types.at(i).at(0)=='u') name.push_back('u');
        name+="int";
        name+=this->data_types.at(i).substr(1,this->data_types.at(i).size()-1);
        name+="_t";
        this->builtins.push_back(builtin_type{this->data_types.at(i),name});
    }
    this->funcs=std::vector<function>();
    this->global_vals=std::vector<variable>();
    this->structs=std::vector<struct_>();
    this->classes=std::vector<class_>();
    this->use_varargs=false;
}
void aurum::compiler::internals::old::compiler::use_flag(std::string flag){
    this->macros.push_back(macro(flag));
}
void aurum::compiler::internals::old::compiler::compile(std::string file_name,bool imported){
    if(this->use_varargs) this->report_error("Unexpected Internal Value");
    lexer::lexer lex();
    std::string_stream file();
    std::string_stream header();
    file<<"#include \""<<file_name<<".h\"\n";
    header<<"#include <stdint.h>\n#include <stdarg.h>\n";
    lexer::token temp;
    bool create_header=true;
    bool create_bin=true;
    bool auto_mode=true;
    bool global_library=false;
    bool mangle=true;
    bool in_class=false;
    bool account_for_function=false;
    bool in_function=false;
    std::vector<scope> scopes;
    bool in_struct=false;
    bool no_discard_mode=false;
    this->compile_tkn_stream(token_eater(lex.use(read_file(code_path+'\\'+file_name+".aur")).tokenize()),LATEST_COMPILE_TKN_STREAM_VERSION,
        &file,&header,
        &create_header,&create_bin,
        &auto_mode,&global_library,
        &mangle,&in_class,
        &account_for_function,&in_function,
        &scopes,imported,
        &in_struct,&no_discard_mode
    );
    if(create_header){
        std::ofstream file_buf((imported?(global_path+"\\include"):generated_header_path)+'\\'+file_name+".h");
        file_buf<<header.str();
        file_buf.close();
    }
    if(create_bin){
        std::ofstream file_buf(generated_code_path+'\\'+file_name+".c");
        file_buf<<out.str();
        file_buf.close();
    }
}
aurum::shared::integers::byte aurum::compiler::compile_sequence(std::vector<std::string> args){
    std::string result_name=std::string();
    std::string file=std::string();
    std::string backend=std::string();
    internals::global_path=std::string();
    internals::code_path=std::string();
    internals::generated_code_path=std::string("backend\\src");
    internals::generated_header_path=std::string("backend\\include");
    bool os_is_microsoft=false;
    for(int i=0;i<args.size();i++){
        if(args.at(i)=="-o"){
            if((++i)==args.size()) shared::utils::crash(shared::internals::errors,4);
            result_name=args.at(i);
        } else if(args.at(i)=="-h"){
            if((++i)==args.size()) shared::utils::crash(shared::internals::errors,4);
            internals::generated_header_path=args.at(i);
        } else if(args.at(i)=="-s"){
            if((++i)==args.size()) shared::utils::crash(shared::internals::errors,4);
            internals::code_path=args.at(i);
        } else if(args.at(i)=="-g"){
            if((++i)==args.size()) shared::utils::crash(shared::internals::errors,4);
            internals::generated_code_path=args.at(i);
        } else if(args.at(i)=="-H"){
            if((++i)==args.size()) shared::utils::crash(shared::internals::errors,4);
            internals::global_path=args.at(i);
        } else if(args.at(i)=="-b"){
            if((++i)==args.size()) shared::utils::crash(shared::internals::errors,4);
            backend=args.at(i);
        } else if(args.at(i)=="-m") os_is_microsoft=true;
        else file=args.at(i);
    }
    if(file==std::string()) shared::utils::crash(shared::internals::errors,5);
    if(backend==std::string()) shared::utils::crash(shared::internals::errors,6);
    // The following line is the only one that needeth be changed upon migration of compiler
    internals::old::compiler compiler();
    compiler.compile(file,false);
    backend.append(" -o");
    backend.append(result_name);
    backend.append(" -iquote ");
    backend.append(internals::generated_header_path);
    backend.append(" -I");
    backend.append(internals::global_path);
    backend.append(' ');
    backend.append(internals::generated_code_path);
    backend.append("\\*.c");
    std::system(backend.c_str());
    backend.clear();
    if(os_is_microsoft){
        backend.append("del ");
        backend.append(internals::generated_code_path);
        backend.append("\\*.c");
        std::system(backend);
        backend.clear();
        backend.append("del ");
        backend.append(internals::generated_header_path);
        backend.append("\\*.h");
        std::system(backend);
        backend.clear();
        backend.append("rmdir ");
        backend.append(internals::generated_header_path);
        std::system(backend);
        backend.clear();
        backend.append("rmdir ");
        backend.append(internals::generated_code_path);
        std::system(backend);
    } else{
        backend.append("rm -rf ");
        backend.append(internals::generated_header_path);
        std::system(backend);
        backend.clear();
        backend.append("rm -rf ");
        backend.append(internals::generated_code_path);
        std::system(backend);
    }
}
#include "shared.h"
void aurum::shared::utils::crash(char** msgs,integers::byte code){
	std::fprintf(std::stderr,msgs[code]);
	std::exit(1);
}
std::string aurum::sharted::utils::join(std::vector<std::string>& list, char connector){
    std::string out;
    for(int i=0;i<list.size();i++){
        if(i) out.push_back(connector);
        out+=list.at(i);
    }
    return out;
}
std::string aurum::shared::utils::read_file(std::string name){
    std::ifstream file(name);
    if(!file.is_open()) return "";
    std::vector<std::string> lines;
    std::string temp;
    while(std::getline(file,temp)) lines.push_back(temp);
    file.close();
    return join(lines,'\n');
}
char** aurum::shared::internals::errors=[
	"No characters to tokenize.\n",
	"Not a valid token.\n",
	"Data corrupted.\n",
	"Invalid Argument.\n",
	"Not enough Arguments.\n",
	"No file provided.\n",
	"No backend provided.\n"
];
aurum::shared::temp_scope0::temp_scope0(){
	this->tkns=std::vector<token>();
	this->scopes=std::vector<handle>();
	this->tkn_location=0;
	this->scp_location=0;
}
aurum::shared::temp_statement::temp_statment(){
	this->tkns=std::vector<token>();
}
aurum::shared::temp_scope1::temp_scope1(){
	this->insts=std::vector<temp_statement>();
	this->scopes=std::vector<handle>();
}
aurum::shared::temp_scope0::~temp_scope0(){
	for(int index=0;index<this->scopes.size();index++) delete ((temp_scope0*)this->scopes.at(index));
}
aurum::shared::temp_scope1::~temp_scope1(){
	for(int index=0;index<this->scopes.size();index++) delete ((temp_scope1*)this->scopes.at(index));
}
inline aurum::shared::optional<aurum::shared::token> aurum::shared::temp_scope0::tkn_peek(){
	return (this->tkn_location<this->tkns)?optional<token>(this->tkns.at(this->tkn_location)):optional<token>();
}
inline aurum::shared::token aurum::shared::temp_scope0::tkn_consume(){
	return this->tkns.at(this->tkn_location++);
}
inline aurum::shared::optional<aurum::shared::handle> aurum::shared::temp_scope0::scp_peek(){
	return (this->scp_location<this->scopes)?optional<handle>(this->scopes.at(this->scp_location)):optional<handle>();
}
inline aurum::shared::handle aurum::shared::temp_scope0::scp_consume(){
	return this->scopes.at(this->scp_location++);
}
inline aurum::shared::optional<aurum::shared::token> aurum::shared::parser::tkn_peek(){
	return (this->tkn_location<this->tkns)?optional<token>(this->tkns.at(this->tkn_location)):optional<token>();
}
inline aurum::shared::token aurum::shared::parser::tkn_consume(){
	return this->tkns.at(this->tkn_location++);
}
aurum::shared::handle aurum::shared::parser::create_scope(){
	temp_scope0* out = new temp_scope0();
	while(!(this->tkn_peek())){
		out->tkns.push_back(this->tkn_consume());
		switch(out->tkns.at(out.tkns.size()-1).type){
		case token_type::END:
			return (handle)out;
		case token_type::START:
			out->scopes.push_back(this->create_scope());
		default:
			break;
		}
	}
	return (handle)out;
}
aurum::shared::handle aurum::shared::parser::create_instructions(temp_scope0* scp){
	temp_scope1* out=new temp_scope1();
	out->insts.push_back(temp_statement());
	while(!(scp->tkn_peek())){
		out->insts.at(out->insts.size()-1).tkns.push_back(scp->tkn_consume());
		switch(out->insts.at(out->insts.size()-1).tkns.at(out->insts.at(out.insts.size()-1).size()-1).type){
		case token_type::END:
			delete scp;
			return (handle)out;
		case token_type::END_STATMENT:
			out->inst.at(out->insts.size()-1).tkns.pop_back();
			out->inst.push_back(temp_statement());
			break;
		case token_type::START:
			if(!!scp->scp_peek()) crash(internals::errors,2);
			out->scopes.push_back(this->create_instructions((temp_scope0*)(scp->scp_consume())));
			out->inst.push_back(temp_statement());
		default:
			break;
		}
	}
	delete scp;
	return (handle)out;
}
std::vector<std::string> aurum::shared::get_args(int argc,char** argv){
	std::vector<std::string> out=std::vector<std::string>();
	for(int i=0;i<argc;i++) out.push_back(std::string(argv[i]));
	return out;
}
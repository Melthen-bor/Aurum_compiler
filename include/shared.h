#ifndef AURUM_SHARED_FILE
#define AURUM_SHARED_FILE
#include <iostream>
#include <vector>
#include <string>
#include <ctype>
#include <cstdlib>
#include <cstdio>
#include <fstream>
namespace aurum {
	namespace shared {
		typedef void* handle;
		namespace integers {
			typedef unsigned char byte;
			typedef unsigned long long nat;
			typedef long long _int;
			inline void set_flags(byte& flags,byte location,byte value){
				flags=value?flags&(255^(1<<location)):flags|(1<<location);
			}
			inline byte get_flag(byte& flags,byte location){
				return flags&(1<<location);
			}
		};
		namespace internals{
			extern char** errors;
		};
		namespace utils{
			void crash(char**,integers::byte);
			std::vector<std::string> get_args(int,char**);
			std::string join(std::vector<std::string>&,char);
			//std::vector<std::string> split(std::string&,char);
			std::string read_file(std::string);
		};
		template<typename type> class optional {
			type val;
			bool exists;
		public:
			optional() {
				this->exists = false;
			}
			optional(type value) {
				this->val = value;
				this->exists = true;
			}
			bool operator!() {
				return this->exists;
			}
			bool operator==(type other) {
				if (!this->exists) return false;
				return other == this->val;
			}
		};
		enum class scope_type{
			if,
			class,
			struct,
			open_class,
			func,
			proc,
			prog
		}
		enum class expr_inst{
			value,
			variable,
			add,
			ass,
			scope,
			mul,
			div,
			sub,
			less,
			more,
			lsh,
			rsh,

		};
		struct expression{
			expr_inst operation;
			std::vector<handle> operands;
		};
		enum class statement_inst{
			start_scope,
			declare,
			return,
			end_scope
		};
		struct statement{
			statement_inst operation;
			expression op0;
			expression op1;
		};
		enum class scope_type{
			global,
		}
		struct scope{
			scope_type type;
			std::vector<statement> insts;
			std::vector<handle> scopes;
		};
		struct temp_scope0{
			std::vector<token> tkns;
			std::vector<handle> scopes;
			temp_scope0();
			~temp_scope0();
		private:
			integers::nat tkn_location;
			inline optional<token> tkn_peek();
			inline token tkn_consume();
			integers::nat scp_location;
			inline optional<handle> scp_peek();
			inline handle scp_consume();
		};
		struct temp_statement{
			std::vector<token> tkns;
			temp_statement();
		};
		struct temp_scope1{
			std::vector<temp_statement> insts;
			std::vector<handle> scopes;
			temp_scope1();
			~temp_scope1();
		};
		class parser{
			std::vector<token> tkns;
			temp_scope0 phase_0;
			temp_scope1 phase_1;
			integers::nat tkn_location;
			inline optional<token> tkn_peek();
			inline token tkn_consume();
			handle create_scope();
			handle create_instructions(temp_scope0*);
		public:
			scope parse();
		};
	};
};
#endif
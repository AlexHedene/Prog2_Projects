#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		int getDecades();
		int fib();
	private:
		int age;
		int rec_fib(int);
	};

Person::Person(int a){
	age = a;
	}
 
int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

int Person::getDecades(){
	return age/10;
	}

int Person::rec_fib(int n){
	if (n <= 1) return 1;
	return rec_fib(n-1) + rec_fib(n-2);
	}

int Person::fib(){
	return rec_fib(age);
	}


extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	int Person_getDecades(Person* person) {return person->getDecades();}
	int Person_fib(Person* person) {return person->fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
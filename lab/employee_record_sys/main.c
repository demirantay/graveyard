/*
  Employe Record System
  ---------------------
  Desc: This is a very basic employee record system built in order to play with
  the C language. The content or the problem that this program tries to solve
  is insignificant.


  I STOPPED BUILDING IT AND LEFT THE PROJECT SINCE IT IS NOT IMPORTANT


*/

#include <stdio.h>
#include <string.h>

// Boolean Definitions
typedef int bool;
#define true 1
#define false 0

// Employee Blueprint
struct Employee {
    int employee_id;
    char first_name[50];
    char last_name[50];
    int salary;
    int performance; // 1 to 5
};

// Methods
struct Employee create_employee(
  int employee_id, char first_name[50], int salary, int performance
);
struct Employee get_employee(struct Employee employee);
int get_salary(struct Employee employee);
int get_performance(struct Employee employee);
void update_first_name(struct Employee employee, char new_name[50]);
void update_salary(struct Employee employee, int new_salary);
void update_performance(struct Employee employee, int new_performance);

/* #### MAIN CODE #### */
int main() {

    // initial employee objects i could ve automated this too but i am lazy atm
    //create_employee(1, "demir", 100, 5);



    // Enterance screen frame
    printf("Employee Management System\n");
    printf("--------------------------\n");
    printf("options: 1 - get salary \n");
    printf("         2 - get performance \n");
    printf("         3 - update first name \n");
    printf("         4 - update salary \n");
    printf("         5 - update performance \n");
    printf("         0 - exit \n\n");

    // Main Loop of the Program that expects a constant user input
    while (true) {

      int user_input;
      printf("$ ");
      scanf("%d", &user_input);

      if (user_input == 1) {
          int salary = get_salary()
          printf("Salary: %d")
      } else if (user_input == 2) {

      } else if (user_input == 3) {

      } else if (user_input == 4) {

      } else if (user_input == 5) {

      } else if (user_input == 0) {
          break;
      } else {
          printf("You entered a invalid number (0 - 5)\n");
          continue;
      }
    }

    // Exit Frame
    printf("\n\nexiting, beep boop!\n");

    return 0;
}


// (crud - create) creating a new employee
struct Employee create_employee(int employee_id, char first_name[50],
                                int salary, int performance) {

    struct Employee employee;

    employee.employee_id = employee_id;
    strcpy(employee.first_name, first_name);
    employee.salary = salary;
    employee.performance = performance;

    // Save it to the storage.txt
    // I am too lazy to implement this level at this time
    return employee;
}

// (crud - read) get the employee stuct
struct Employee get_employee(struct Employee employee) {
    return employee;
}

// (crud - read) get the employee salary
int get_salary(struct Employee employee) {
    int salary = employee.salary;
    return salary;
}

// (crud - read) get the employee performance
int get_performance(struct Employee employee) {
    int performance = employee.performance;
    return performance;
}

// (crud - update) update the name of the employee
void update_first_name(struct Employee employee, char new_name[50]) {
    strcpy(employee.first_name, new_name);
}

// (crud - update) update the salary of the employee
void update_salary(struct Employee employee, int new_salary) {
    employee.salary = new_salary;
}

// (crud - update) update the performance
void update_performance(struct Employee employee, int new_performance) {
    employee.performance = new_performance;
}

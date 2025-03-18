import kotlin.text.toIntOrNull

data class Person(val name: String, val baseSalary: Int);

class SalaryCalculator(private val hourlyRate: Int) {
    fun calculateSalary(hoursWorked: Int): Int {
        return hoursWorked * hourlyRate;
    };
};

fun main() {
    val people = listOf(
        Person("John", 10),
        Person("Pjotr", 11),
        Person("Ivan", 12),
        Person("Alex", 13),
        Person("Hans", 14)
    );

    val sortedPeople = people.sortedBy { it.name };

    val calculator = SalaryCalculator(10); // Example: hourly rate of 10

    for (person in sortedPeople) {
        java.io.IO.print("Enter hours worked for ${person.name}: ")
        val hoursWorkedString = kotlin.io.readlnOrNull();
        if(hoursWorkedString != null){
            val hoursWorked = hoursWorkedString.toIntOrNull() ?: 0; // If they enter a non number, we use 0
            val salary = calculator.calculateSalary(hoursWorked);
            java.io.IO.println("Salary for ${person.name} is $salary");
        } else{
            java.io.IO.println("No hours entered for ${person.name}")
        };
    };
};
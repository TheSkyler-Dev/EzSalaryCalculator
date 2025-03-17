//EzSalaryCalculator: An app for calculating salaries without tax

data class Workers{
    //Worker Class logic here
    val workers = listOf(
        Person("John", 2130),
        Person("Pjotr", 2132),
        Person("Ivan", 2131),
        Person("Alex", 2133),
        Person("Hans", 2134)
    );
    val sortedWorkers = workers.sort(workers, compareBy{it.id});
}

class SalaryCalculator(var: Int){
    //salary calculator logic here
}

fun main(){
    //main logic here
    for (worker in workers){
        println("Salary for ${worker.name} is ${worker.salary}");
    };
}
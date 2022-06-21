package com.example.helloworld

open class Person(name: String, age: Int) {
    var name = ""
    var age = 0

    fun eat() {
        println(name + "is eating. He is " + age + "years old.")
    }

}
fun main() {
    val p = Person("Jack", 19)
    CellPhone.test = 2
}
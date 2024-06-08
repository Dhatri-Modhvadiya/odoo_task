odoo.define('my_module.classes', function (require) {
    'use strict';

    var Class = require('web.Class');

    // Define Class A
    var A = Class.extend({
        init: function (name) {
            this.name = name;
        },

        // Method in Class A
        greet: function () {
            console.log(`Hello, ${this.name}!`);
        },

        // Another method in Class A
        sayGoodbye: function () {
            console.log(`Goodbye, ${this.name}!`);
        }
    });

    // Inherit Class A into Class B
    var B = A.extend({
        init: function (name, age) {
            this._super(name);  // Call the constructor of Class A
            this.age = age;
        },

        // Method in Class B
        displayAge: function () {
            console.log(`${this.name} is ${this.age} years old.`);
        }
    });

    // Add a method to the prototype of Class A
    A.prototype.introduce = function () {
        console.log(`I am ${this.name}.`);
    };

    // Create an instance of Class B and test the methods
    var person = new B('John', 30);
    person.greet();         // Output: Hello, John!
    person.sayGoodbye();    // Output: Goodbye, John!
    person.displayAge();    // Output: John is 30 years old.
    person.introduce();     // Output: I am John.

    // Export the classes if needed
    return {
        A: A,
        B: B
    };
});















//// Define Class A
//class A {
//    constructor(name) {
//        this.name = name;
//    }
//
//    // Method in Class A
//    greet() {
//        console.log(`Hello, ${this.name}!`);
//    }
//
//    // Another method in Class A
//    sayGoodbye() {
//        console.log(`Goodbye, ${this.name}!`);
//    }
//}
//
//// Inherit Class A into Class B
//class B extends A {
//    constructor(name, age) {
//        super(name);  // Call the constructor of Class A
//        this.age = age;
//    }
//
//    // Method in Class B
//    displayAge() {
//        console.log(`${this.name} is ${this.age} years old.`);
//    }
//}
//
//// Create an instance of Class B
//const person = new B('John', 30);
//
//// Use methods from Class A
//person.greet();         // Output: Hello, John!
//person.sayGoodbye();    // Output: Goodbye, John!
//
//// Use method from Class B
//person.displayAge();    // Output: John is 30 years old.

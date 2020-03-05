//JS
function getBook(title, auther) {
    return {
        title: title,
        auther: auther
    };

}
var book = getBook('Harry Potter', 'JK');
console.log(book);
var counter = 5;
console.log(counter);

function sayName() {
    var name = "Coki";
    console.log(name);
}
sayName();

var sayAge = function() {
    console.log(24);
}
sayAge();

var user = {
    names: "Collins",
    age: '24',
    sayNames: function() {
        console.log("My name is " + this.names);
        var that = this;
        var fullname = function() {
            console.log("My name is " + that.names + " and my Age is " + that.age);
        };
        fullname();
    }
}

user.sayNames();

//ES6
const list = [1, 2, 3, 4, 5];
for (let index = 0; index < list.length; index++) {
    console.log(list[index]);

}
const name = "Kiplagat";
console.log(`Hello my name is ${name}`);

const todolist = {
    names: "Shopping list",
    items: ['Milk', 'Bread']
}
const { names, items } = todolist;

console.log(`The ${names} contains the following items ${items}`);
console.log(items);
// if you have one paramenter you can get rid of the parenthesis 
//The arrow function in es6
const sayLocation = (location) => {
    console.log(`My location is ${location}`);
}
sayLocation('Eldoret');
/*
In JavaScript, a higher-order function is a function that operates on other functions by taking them as arguments,
 returning them as results, or both. It treats functions as first-class citizens, allowing you to manipulate and 
 utilize them in various ways.
*/


// map, filter, and reduce are  a javascript builtin higher order function
var numbers = [7, 3, 8, 21, 9]

results = numbers.map(function (number){
    return  number * 2;
});

console.log(results);

// filter :

players = [
    {
        name: "Sakib",
        avg: 45
    },
    {
        name: "Tamim",
        avg : 41,
    },
    {
        name: "M. Rahim",
        avg: 39
    },
    {
        name: "L. Das",
        avg: 32
    }
]

filteredResults = players.filter(function (player){
    return player.avg >=40;
});

console.log(filteredResults);

// reduce:

var numbers = [1, 2, 3, 4, 5]

const sum = numbers.reduce(function(accumulator, num){
    return accumulator + num
});

console.log(sum);



let instance = null;

class Singleton{
    constructor() {
        if (instance) {
            throw new Error("You can only create one instance!");
        }
        instance = this;
    }

    getInstance(){
        return this;
    }
}

let obj1 = new Singleton()
let obj2 = new Singleton()

obj1.getInstance()
obj2.getInstance()
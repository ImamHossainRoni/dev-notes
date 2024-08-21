fn main() {
    variables_mutability();
    variables_shadowing();
    tuples();
    array();
}

fn variables_mutability(){
    let num: i8 = 127;
    //num = 10; // This would cause a compile-time error because num is immutable
    println!("{}", num);

    let mut num2: i8 = 127;
    num2 = 10; // This is allowed because num2 is mutable
    println!("{}", num);
}
fn variables_shadowing(){
    let x = 5;
    let x = x +1;
    let x = "Shadowed";
    println!("{}", x)
}
fn tuples(){
    let tuple: (i32, f64, char) = (500, 5.7, 'A');
    let (x,y,z) = tuple; // Destructuring the tuple
    println!("Original tuple: {:?}", tuple);
    println!("Destructuring the tuple values : {}, {}, {}", x, y, z);
}
fn array(){
    let my_array : [i32; 3] = [1, 2, 4];
    println!("Arrays : {:?}", my_array);
    let slice: &[i32] = &my_array[1..3];
    println!("Array slicing : {:?}", slice);
}
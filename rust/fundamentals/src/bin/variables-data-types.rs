fn main() {
    variables_mutability();
    variables_shadowing();

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
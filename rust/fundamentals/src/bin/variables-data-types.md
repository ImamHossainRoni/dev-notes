<p>In Rust, variables and data types are the fundamental concepts that help  us to store and manipulate data in a safe and efficient way.</p>

### Variables in Rust :
###### 1. Immutable by Default:
1. In Rust, variables are immutable by default, meaning that once a value is assigned, it cannot be changed.
2. To declare an immutable variable, use the let keyword.

```rust
let x = 5;
// x = 6; // This would cause a compile-time error because x is immutable

```
###### 2. Mutable Variables:
If we need to change the value of a variable, we must declare it as mutable using the `mut` keyword.
```rust
let mut y = 10;
y = 15;
```

###### 3. Variable Shadowing:
Rust allows us to "shadow" a variable, that means we can declare a new variable with the same name as a previous variable. The new variable will shadow the old one, and we can even change its type.
```rust
let x = 5;
let x = x + 1; // x is now 6
let x = "shadowed"; // x is now of type &str
```

###### 3. Constants:
Constants are always immutable and must be annotated with a type. They are declared using the const keyword and must be assigned a value at compile time.

```rust
const MAX_POINTS: u32 = 100_000;
```

### Data Types in Rust :
Rust is a statically types language which means that the type of every variable must be known at compile time.
Rust has a rich set of data types that divided into two main categories: `Scalar types` & `Compound types`.

#### Scalar Types :
Scalar types represent a single value. Rust has four primary scalar types: `integers`, `floating-point numbers`, `Booleans`, & `characters`.

##### Integers:
1. Signed (i8, i16, i32, i64, i128, isize) and unsigned (u8, u16, u32, u64, u128, usize) integers.

2. The isize and usize types depend on the architecture of the computer (32-bit or 64-bit).
3. Signed and Unsigned Integers in Rust

<table>
  <tr>
    <th>Type</th>
    <th>Signed/Unsigned</th>
    <th>Bits</th>
    <th>Range</th>
    <th>Formula</th>
    <th>2^n</th>
  </tr>
  <tr>
    <td>i8</td>
    <td>Signed</td>
    <td>8</td>
    <td>-128 to 127</td>
    <td>2^(n-1) - 1</td>
    <td>2^8</td>
  </tr>
  <tr>
    <td>i16</td>
    <td>Signed</td>
    <td>16</td>
    <td>-32,768 to 32,767</td>
    <td>2^(n-1) - 1</td>
    <td>2^16</td>
  </tr>
  <tr>
    <td>i32</td>
    <td>Signed</td>
    <td>32</td>
    <td>-2,147,483,648 to 2,147,483,647</td>
    <td>2^(n-1) - 1</td>
    <td>2^32</td>
  </tr>
  <tr>
    <td>i64</td>
    <td>Signed</td>
    <td>64</td>
    <td>-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807</td>
    <td>2^(n-1) - 1</td>
    <td>2^64</td>
  </tr>
  <tr>
    <td>u8</td>
    <td>Unsigned</td>
    <td>8</td>
    <td>0 to 255</td>
    <td>2^n - 1</td>
    <td>2^8</td>
  </tr>
  <tr>
    <td>u16</td>
    <td>Unsigned</td>
    <td>16</td>
    <td>0 to 65,535</td>
    <td>2^n - 1</td>
    <td>2^16</td>
  </tr>
  <tr>
    <td>u32</td>
    <td>Unsigned</td>
    <td>32</td>
    <td>0 to 4,294,967,295</td>
    <td>2^n - 1</td>
    <td>2^32</td>
  </tr>
  <tr>
    <td>u64</td>
    <td>Unsigned</td>
    <td>64</td>
    <td>0 to 18,446,744,073,709,551,615</td>
    <td>2^n - 1</td>
    <td>2^64</td>
  </tr>
</table>

* **Note**: **Signed integers** can represent both positive and negative numbers. They use one bit to indicate the sign (positive or negative) and the remaining bits to store the magnitude of the value.
  **Unsigned integers** can only represent non-negative numbers. All bits are used to store the magnitude of the value.

```rust
let a: i32 = 10;
let b: u8 = 255;
```
##### Floating-Point Numbers:
1. f32 (32-bit) and f64 (64-bit) floating-point numbers.

```rust
let c: f64 = 2.5;
```
##### Booleans:
1. Represented by the bool type with values true or false.
```rust
let is_active: bool = true;

```
##### Characters:
1. The char type represents a single Unicode scalar value, and it is 4 bytes in size.
```rust
let letter: char = 'A';
let emoji: char = '😊';
```

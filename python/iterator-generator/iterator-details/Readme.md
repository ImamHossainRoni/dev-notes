>I use iterators because they let me process large datasets efficiently by fetching one item at a time instead of 
loading everything into memory. For example, in a project I worked on, I had to process very large CSV files. Instead 
of reading the whole file at once, I used the file object as an iterator to read line by line, which made the program 
memory-efficient and scalable.
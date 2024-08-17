using _1ToMAssociation;

class Program
{
    static void Main()
    {
        // Creating courses data
        Course course1 = new Course();
        course1.Code = "CSC-101";
        course1.Title = "Programing in C";
        course1.Credit = 3;

        Course course2 = new Course();
        course2.Code = "CSC-102";
        course2.Title = "Data Structure & Algorithm";
        course2.Credit = 4;
        
        Course course3 = new Course();
        course3.Code = "CSC-103";
        course3.Title = "Database Management System";
        course3.Credit = 3;
        
        // Creating department data
        Department department = new Department();
        department.Code = "CSE";
        department.Name = "Computer Science & Engineering";
        department.Courses = new List<Course>();
        
        // Adding courses to that particular department
        department.Courses.Add(course1);
        department.Courses.Add(course2);
        department.Courses.Add(course3);
        
        // Printing department information
        Console.WriteLine(department.GetInfo());
       
    }
}
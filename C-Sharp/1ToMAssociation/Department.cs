namespace _1ToMAssociation;

public class Department
{
    public string Code { get; set; }
    public string Name { get; set; }
    
    public List<Course> Courses { get; set; }

    public string GetInfo()
    {
        string info = $"Code: {Code} & Name: {Name}" + Environment.NewLine;
        foreach (var course in Courses)
        {
            info += course.GetCourseDetails() + "\n";
        }

        return info;
    }
}
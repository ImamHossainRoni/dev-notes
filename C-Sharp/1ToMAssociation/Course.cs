namespace _1ToMAssociation;

public class Course
{
    public string Code { get; set; }
    public string Title { get; set; }
    public double Credit { get; set; }

    public string GetCourseDetails()
    {
        return ($"Course Code: {Code} , Course Title: {Title}  and Credit {Credit}");
    }
}
namespace _1To1Association;

public class Address
{
    public string HouseNo { get; set; }
    public string RoadNo { get; set; }
    public string Area { get; set; }
    public string PostCode { get; set; }
    public string District { get; set; }


    public string GetFullAddress()
    {
        return $"House No: {HouseNo}, Road No: {RoadNo}, Area: {Area}, Post Code: {PostCode}, District: {District}";
    }
    
}
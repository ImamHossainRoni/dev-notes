"""
    Open-Closed Principle (OCP) can be achieved through the example of polymorphism.

The Open-Closed Principle states that software entities (classes, modules, functions, etc.) should be open for
extension but closed for modification. In other words, once a module is implemented and working correctly,
it should not be modified to add new features or behaviors. Instead, the module should be open to extension by
allowing new functionality to be added without modifying the existing code.

In the example, the Shape superclass represents a closed entity because it provides a common interface (
calculate_area()) that is not modified when new shapes are added. The Circle and Rectangle classes represent open
entities because they extend the Shape class and provide their own implementations of the calculate_area() method.

By using polymorphism, we can introduce new shape classes (e.g., Triangle, Square) without modifying the existing
code. These new classes can inherit from the Shape class and implement the calculate_area() method according to their
specific shape logic. This way, we can extend the behavior of the program without modifying the existing Shape or
Shape-related code.

The OCP is achieved because the Shape class is closed for modification, as it remains unchanged. It is open for
extension, as new shape classes can be added by inheriting from it and providing their own implementation of the
calculate_area() method.

In summary, polymorphism facilitates the implementation of the Open-Closed Principle by allowing the addition of new
functionality through subclassing and method overriding without modifying the existing code. It promotes code
maintainability, reusability, and flexibility in handling new requirements or variations in behavior.

"""
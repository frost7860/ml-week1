all_students = {"Alice", "Bob", "Charlie", "David", "Eva", "Fay"}
football = {"Alice", "Bob", "Charlie"}
cricket = {"Charlie", "David", "Eva"}
both = football & cricket
print("Students who play both:", both)
only_one = (football ^ cricket)  
print("Students who play only one:", only_one)
none = all_students - (football | cricket)
print("Students who play none:", none)

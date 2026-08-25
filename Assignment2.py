from functools import wraps

# Decorator
def border(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


class Report:

    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class Method
    @classmethod
    def create_report(cls, title, content):
        return cls(title, content)

    # Magic Method (__str__)
    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}"

    # Magic Method (__len__)
    def __len__(self):
        return len(self.content)

    # Magic Method (__add__)
    def __add__(self, other):
        return Report(
            self.title + " & " + other.title,
            self.content + "\n" + other.content
        )





    # Decorated Method
    @border
    def display(self):
        return str(self)


# Creating Reports
r1 = Report.create_report("Student Report", "Name: Rahul\nMarks: 90")
r2 = Report.create_report("Sports Report", "Cricket Winner")

# Display Reports
print(r1.display())

print()

print(r2.display())

print()

# Combine Reports
r3 = r1 + r2
print(r3.display())

print()

# Length of Content
print("Length of Report:", len(r3))
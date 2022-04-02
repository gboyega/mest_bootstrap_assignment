# firstName = "JOHN"
# LastName = "MENSAH"
# employeeId = "EMP18373748"
# basicSalary = 10000
# allowance = 5000
# taxPercentage = 10
# pensionSchemePercentage = 20

# def calculateTax(basicSalary, taxPercentage):
#     return (basicSalary / 100) * taxPercentage

# def calculatePension(basicSalary, allowance, pensionPercentage):
#     return ((basicSalary + allowance) / 100) * pensionPercentage

# def calculateNetSalary(basicSalary, allowance, tax, pension):
#     return basicSalary + allowance - tax - pension

# tax = calculateTax(basicSalary, taxPercentage)
# pensionScheme = calculatePension(basicSalary, allowance, pensionSchemePercentage);
# netSalary = calculateNetSalary(basicSalary, allowance, tax, pensionScheme);

# narration = f"{firstName} {LastName} with employee Id: {employeeId}, earns a basic salary of {basicSalary}GHS and an allowance of {allowance}GHS. His/Her deductibles include tax of {tax}GHS, calculated at {taxPercentage} percent of basic salary and pension contribution of {pensionScheme} GHS calculated at {pensionSchemePercentage} percent of basic salary and allowance. His/Her net salary is therefore {netSalary} GHS."

# # print(narration.format(firstName, LastName, employeeId, basicSalary, allowance,tax, taxPercentage, pensionScheme, pensionSchemePercentage, netSalary))

# print(narration)


# # NET SALARY = (Basic Salary - Tax - Pension Scheme + Allowance)

users = [
    {
        "id": 1,
        "name": "John Bull",
        "email": "me@mey.com",
        "phone_number": "+2331234567890",
        "number_of_visits": "10",
        "posts": [
            {"id": "1.1", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.2", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.3", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.4", "title": "my name", "summary": "My name is jaiye"},
        ],
    },
    {
        "id": 2,
        "name": "John Cow",
        "email": "me@mey.com",
        "phone_number": "+2331234567890",
        "number_of_visits": "9",
        "posts": [
            {"id": "1.1", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.2", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.3", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.4", "title": "my name", "summary": "My name is jaiye"},
        ],
    },
    {
        "id": 3,
        "name": "John Sheep",
        "email": "me@mey.com",
        "phone_number": "+2331234567890",
        "number_of_visits": "8",
        "posts": [
            {"id": "1.1", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.2", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.3", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.4", "title": "my name", "summary": "My name is jaiye"},
        ],
    },
    {
        "id": 4,
        "name": "John Goat",
        "email": "me@mey.com",
        "phone_number": "+2331234567890",
        "number_of_visits": "7",
        "posts": [
            {"id": "1.1", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.2", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.3", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.4", "title": "my name", "summary": "My name is jaiye"},
        ],
    },
    {
        "id": 5,
        "name": "John Deer",
        "email": "me@mey.com",
        "phone_number": "+2331234567890",
        "number_of_visits": "6",
        "posts": [
            {"id": "1.1", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.2", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.3", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.4", "title": "my name", "summary": "My name is jaiye"},
        ],
    },
    {
        "id": 6,
        "name": "John Giraffe",
        "email": "me@mey.com",
        "phone_number": "+2331234567890",
        "number_of_visits": "5",
        "posts": [
            {"id": "1.1", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.2", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.3", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.4", "title": "my name", "summary": "My name is jaiye"},
        ],
    },
    {
        "id": 7,
        "name": "John Horse",
        "email": "me@mey.com",
        "phone_number": "+2331234567890",
        "number_of_visits": "4",
        "posts": [
            {"id": "1.1", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.2", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.3", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.4", "title": "my name", "summary": "My name is jaiye"},
        ],
    },
    {
        "id": 8,
        "name": "John Donkey",
        "email": "me@mey.com",
        "phone_number": "+2331234567890",
        "number_of_visits": "3",
        "posts": [
            {"id": "1.1", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.2", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.3", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.4", "title": "my name", "summary": "My name is jaiye"},
        ],
    },
    {
        "id": 9,
        "name": "John Hippo",
        "email": "me@mey.com",
        "phone_number": "+2331234567890",
        "number_of_visits": "2",
        "posts": [
            {"id": "1.1", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.2", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.3", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.4", "title": "my name", "summary": "My name is jaiye"},
        ],
    },
    {
        "id": 10,
        "name": "John Ox",
        "email": "me@mey.com",
        "phone_number": "+2331234567890",
        "number_of_visits": "1",
        "posts": [
            {"id": "1.1", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.2", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.3", "title": "my name", "summary": "My name is jaiye"},
            {"id": "1.4", "title": "my name", "summary": "My name is jaiye"},
        ],
    },
]


for user in users:
    print(
        """
        User: {},
        Number of visits: {},
        Number of posts: {}
        """.format(
            user["name"], user["number_of_visits"], len(user["posts"])
        )
    )

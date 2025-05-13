## Exercise 4

### Maintaining and Expanding Software for Component Validation

This exercise focuses on strategies for working with existing code bases and ensuring the software remains maintainable as new features and requirements are introduced.

### 1. **Working with Existing Code**    
- How would you approach understanding and contributing to an existing code base with minimal disruption?  

   Start by reading the existing documentation (README files or HTML docs such as Doxygen or Javadoc). Try to understand how the code is used. Breakpoints can be used to understand some parts of the code. The test files can also give some information about the code.

- What practices would you follow to ensure your changes integrate well with the current structure?  

   Create a new file to not disturb the existing one. Make sure every change is easily reversible, so if something breaks, it's simple to get back to a previous version. Respect the code conventions (folder structure, variable names...). Update the documentation for the added code.

### 2. **Ensuring Maintainability**    
- What techniques would you use to keep the code base clean, modular, and easy to maintain as new features are added?  

   Each module/class should only have one precise role. Use encapsulation to avoid uncontrolled dependencies between modules. Design patterns can also be used to avoid errors. Follow coding conventions, and use clear, descriptive names for variables, functions, and methods to improve code readability and maintainability.

- How would you handle code documentation and testing to support long-term maintainability?  

   Keep the README file updated along with the newly added lines of code. Write simple but useful comments when necessary. HTML documentation can also be used.

### 3. **Balancing Flexibility and Stability**    
- How would you design or refactor the software to make it flexible for future changes while ensuring the existing functionality remains stable?  

   Separate the code into different modules to only modify some parts of the code without editing all the code. We can use well-defined APIs/interfaces to limit the dependencies between the different modules.

- Which design patterns or principles would you apply to achieve this balance

   Test files can be written along with the new code to ensure it works well. Use modeling before writing code for object-oriented projects.
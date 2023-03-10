# General Knowledge

## Parameter vs args

- a parameter is what appears in the definition of a function (its signature, or prototype)
- an argument is a value that appears in the call to this function.

## Bit manipulation

![](./bit-manipulations.png)

## Floating point variables

- [What Every Programmer Should Know About Floating-Point Arithmetic](https://floating-point-gui.de/)

## Strong/Weak, Static/Dynamic Typing

- Static/Dynamic Typing is about when type information is acquired (Either at compile time or at runtime)
- Strong/Weak Typing is about how strictly types are distinguished (e.g. whether the language tries to do an implicit conversion from strings to numbers).
- Examples
  - Dynamic: python, javascript
  - Static: c++, java
  - Strong: java, python
  - Weak: javascript, c/c++

![](./strongweakstaticdynamic_type.png)

## Thread vs process

- Threads (of the same process) run in a shared memory space, while processes run in separate memory spaces.
- The thread context includes the thread's set of machine registers, the kernel stack, a thread environment block, and a user stack in the address space of the thread's process.
- Threads handling done by the scheduler

![](./processes-threads.jpg)

## OOP

4 principles:

- Encapsulation: Private & public methods
- Abstraction: Don’t need to know inner details to use class
- Inheritance: To reuse code
- Polymorphism:  Ability of one function to perform in different ways.

## Classes

### Abstract classes

- classes that contain one or more abstract methods.
- An abstract method is a method that is declared, but contains no implementation.
- Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods.

## Good coding

- should fail nicely, and give a reason why it failed
- no code duplication
- readable
- optimized, but optimization shoudln't impact readability
- commented if needed
- structured, maintenable

## CI CD

- Continuous integration: Frequent merging of several small changes into a main branch
- Continuous delivery: When teams produce software in short cycles with high speed and frequency so that reliable software can be released at any time, and with a simple and repeatable deployment process when deciding to deploy
- Continuous deployment: When new software functionality is rolled out completely automatically

## Folder structure

- <https://github.com/kriasoft/Folder-Structure-Conventions>

## Publish code

### Write README

- <https://skerritt.blog/make-popular-open-source-projects/>

### Documentation

- [What nobody tells you about documentation](https://www.divio.com/blog/documentation/)

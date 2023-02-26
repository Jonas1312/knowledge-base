#include <iostream>

template <typename T>
class UniquePtr {
   private:
    T *p_pointer = nullptr;

   public:
    // normal constructors, destructors
    UniquePtr() = delete;
    UniquePtr(T *ptr) : p_pointer(ptr) {}
    ~UniquePtr() {
        std::cout << "destructor called" << std::endl;
        if (p_pointer != nullptr) {
            delete p_pointer;  // what happens if we have a pointer to an array?
        }
    }

    // operators
    T &operator*() { return *p_pointer; }  // * operator has to return the "real" variable we're pointing at
    T *operator->() { return p_pointer; }  // -> operator expects a pointer on its left side

    // copy policy
    UniquePtr(const UniquePtr &obj) = delete;             // copy constructor
    UniquePtr &operator=(const UniquePtr &obj) = delete;  // copy assignement operator

    // move policy
    // UniquePtr(UniquePtr && dying_obj){ // move constructor, can't be const since we're modifying the dying_obj
    //     // transfer ownership
    //     this->p_pointer = dying_obj.p_pointer; // "this" is a pointer !!! that's why we need ->
    //     dying_obj.p_pointer = nullptr;
    // }

    // better move constructor with std::move!
    UniquePtr(UniquePtr &&dying_obj) : UniquePtr(std::move(dying_obj)) {}

    UniquePtr &operator=(UniquePtr &&dying_obj) {  // void since the current obj already exists
        // we need to delete current memory
        if (p_pointer != nullptr) {
            delete p_pointer;
        }

        this->p_pointer = dying_obj.p_pointer;
        dying_obj.p_pointer = nullptr;

        return *this;
    }
};

// for arrays:
// template <typename T>
// class UniquePtr<T[]> {
// ...
// T& operator[](int index)
// };

int main(int argc, char const *argv[]) {
    UniquePtr<int> my_ptr(new int(42));
    std::cout << *my_ptr << std::endl;
    return 0;
}

class Uninheritable{

    friend class NotABase;
    private: 
        Uninheritable(void) {}
};

class NotABase: public virtual Uninheritable {
// WHATEVER
};

class NotADerived: public NotABase{
// WHATEVER ELSE 
};

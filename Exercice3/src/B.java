public class B extends A {

    public B(String name) {
        super(name);
    }

    private void printName(String name){}

    @Override
    public void printName() {
        System.out.println("nom pour B :" + Name);
    }
}

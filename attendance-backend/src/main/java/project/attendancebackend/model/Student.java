package project.attendancebackend.model;
import java.util.Objects;

public class Student {
    
    String name;
    String rollnumber ;

    public Student() {
    }

    public Student(String name, String rollnumber) {
        this.name = name;
        this.rollnumber = rollnumber;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getRollnumber() {
        return this.rollnumber;
    }

    public void setRollnumber(String rollnumber) {
        this.rollnumber = rollnumber;
    }

    @Override
    public String toString() {
        return "{" +
            " name='" + getName() + "'" +
            ", rollnumber='" + getRollnumber() + "'" +
            "}";
    }
    
}

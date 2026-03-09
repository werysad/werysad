using UnityEngine;

public class p2 : MonoBehaviour
{
    void Start()
    {
        CalculateGrade(85); // Example: 85 is B
        CalculateGrade(92); // Example: 92 is A
    }

    void Update()
    {
        
    }

    void CalculateGrade(int marks)
    {
        string grade;

        switch (marks / 10)
        {
            case 10:
            case 9:
                grade = "A";
                break;

            case 8:
                grade = "B";
                break;

            case 7:
                grade = "C";
                break;

            case 6:
                grade = "D";
                break;

            default:
                grade = "F";
                break;
        }

        Debug.Log("Marks: " + marks + " Grade: " + grade);
    }
}
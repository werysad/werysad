using UnityEngine;

public class p1 : MonoBehaviour
{
    void Start()
    {
        CheckOddEven(5);
        CheckOddEven(10);
    }

    void Update()
    {
        
    }

    void CheckOddEven(int num)
    {
        if (num % 2 == 0)
        {
            Debug.Log(num + " is even");
        }
        else
        {
            Debug.Log(num + " is odd");
        }
    }
}
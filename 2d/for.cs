using UnityEngine;

public class p3 : MonoBehaviour
{
    void Start()
    {
        SumOfN(10); // Sum of first 10 numbers
    }

    void Update()
    {   
    }

    void SumOfN(int n)
    {
        int sum = 0;

        for (int i = 1; i <= n; i++)
        {
            sum += i;
        }

        Debug.Log("Sum of first " + n + " numbers: " + sum);
    }
}
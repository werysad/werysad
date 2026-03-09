using UnityEngine;

public class p4 : MonoBehaviour
{
    void Start()
    {
        SumEvenInRange(1, 10); // Sum of even numbers from 1 to 10
    }

    void Update()
    {   
    }

    void SumEvenInRange(int start, int end)
    {
        int sum = 0;
        int current = start;

        while (current <= end)
        {
            if (current % 2 == 0)
            {
                sum += current;
            }
            current++;
        }

        Debug.Log("Sum of even numbers from " + start + " to " + end + ": " + sum);
    }
}
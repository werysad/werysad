using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class InputFieldExample : MonoBehaviour
{
    public InputField inputField;


    public void InputFieldValueChanged(string value)
    {
        Debug.Log("Input field value changed " + value);
    }
}

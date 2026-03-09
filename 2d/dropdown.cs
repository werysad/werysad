using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;


public class DropdownExample : MonoBehaviour
{
    [SerializeField] private TMP_Dropdown m_Dropdown;


    void Start()
    {
        // Optional: you can initialize or add listeners here
    }


    // Update is called once per frame
    public void GetDropDownValue()
    {
        int picked = m_Dropdown.value;
        string selectedOption = m_Dropdown.options[picked].text;
        Debug.Log(selectedOption);
    }
}

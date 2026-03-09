using UnityEngine;


public class Animation_script : MonoBehaviour
{
    private Animator myanim;


    bool iskicking = false;
    bool isbreathing = false;


    // Start is called before the first frame update
    void Start()
    {
        myanim = GetComponent<Animator>();
    }


    // Update is called once per frame
    void Update()
    {
        iskicking = Input.GetKey(KeyCode.W);
        myanim.SetBool("kick", iskicking);
        //make sure the name of the bool in the
        // animator is the same as the one in the code


        isbreathing = Input.GetKey(KeyCode.D);
        myanim.SetBool("breathing", isbreathing);
    }
}

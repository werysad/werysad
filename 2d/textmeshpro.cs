using UnityEngine;
using TMPro;
public class Textmeshpro : MonoBehaviour
{
    public TextMeshProUGUI output;
    public void HandleInput(int val)
    {
        if (val == 0)
        {
            output.text = "One Piece";
        }
        else if (val == 1)
        {
            output.text = "Demon Slayer";
        }
        else if (val == 2)
        {
            output.text = "Bleach";
        }
    }
}
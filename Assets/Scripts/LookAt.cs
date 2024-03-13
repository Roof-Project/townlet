using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LookAt : MonoBehaviour
{
    public Transform LookTransform;

    private void FixedUpdate()
    {
        transform.LookAt(LookTransform);
    }
}

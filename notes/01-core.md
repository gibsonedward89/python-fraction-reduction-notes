# Reduce rational numbers: implementation

## What the example does

Fraction reduces numerator and denominator by their greatest common divisor. A zero denominator raises ZeroDivisionError; signs are normalized.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
[
  6,
  8
]
```

Expected result:

```json
{
  "numerator": 3,
  "denominator": 4
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.

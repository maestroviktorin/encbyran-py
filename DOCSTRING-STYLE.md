# Docstring style

## Motivation

This document is created to describe the unified `__doc__` style used in repository `encryption-by-random`.

## Style

Every docstring (aka `function.__doc__`) in the repository must be written in Markdown and stick to the following standard:

```markdown
### Parameters

Description of each parameter accepted by the function in the form:

`parameter` - Description.

### Actions

Actions performed by the function, such as interactions with other functions, modification of external variables etc.

### Returns

Description of each value returned by the function.
```

* If the function does not accept any parameters, the `Parameters` section can be omitted.

* If the function does not return any values, the `Returns` section can be omitted.

* If the function does not perform any actions, the `Actions` section can be omitted.

## Examples

```py
def add_one(n: int) -> int:
    """
    ### Parameters

    `n` - Number to add 1 to.

    ### Returns

    Sum of `n` and 1.
    """
    return n + 1
```

```py
class Cat:
    def meow() -> None:
        """
        ### Actions

        Prints "Meow!" to the console.
        """
        print("Meow!")
```

```py
used_parameters: set[tuple] = set()


def sum_of(a: int | float, b: int | float) -> int | float:
    """
    ### Parameters

    `a` - First summand.
    `b` - Second summand.

    ### Actions

    Saves `(a, b)` pair to `used_parameters` external variable.

    ### Returns

    Sum of `a` and `b`
    """
    used_parameters.add((a, b))
    return a + b
```

### Mouse and Keyboard Manipulation

[Pynput](https://github.com/moses-palmer/pynput) is an awesome module that can be used to monipulate mouse and keyboard.
* `get mouse pointer coordinates (x, y)`,
* `moving pointer`,
* `pressing some keys alone or combinated`
are some of the functions of it.

The problem is that when writing some workload, makes the same syntaxes like: `.press, .release` 
```python
.press
.press
.press
.release
.release
.release
```

**Pynput Easy** provides some easy usage for `pynput`.

#### mClick

**mClick** is a function that make cursor position where want to click to.

in traditional method, first `.position = (x, y)` then `.press`, `.release`.

in this function:
`mClick(x, y)` makes the same goal.

**mDoubleClick** does also similarly.


#### tabKey

`Tab key` is a special key from others. Because press more than one time. So, `tabKey(n)` function press `Tab key` one after another `0.1 sec` intervals.


#### keyCombine

`Key Combination` is the best method to move for a developer. in `pynput` some keys are different the letters such as `Ctrl`, `Shift` etc. When the key `ctrl` want to pressed, syntax sould be different the letter keys. For instance of `Ctrl + C`:
```python
.press(Key.ctrl)
.press('c')
.release('c')
.release(Key.ctrl)
```

But in this function:
`keyCombine("ctrl+c")`

**Noted that:** in some cases, cursor keeps location on the screen even moved to the location disered.

##### Usage

```python
from pynputEasy import mClick, mDoubleClick, tabKey, keyCombine
```
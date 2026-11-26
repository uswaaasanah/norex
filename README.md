# NOREX — Nonlinear Root Explorer

NOREX is a desktop application for exploring numerical methods that approximate real roots of a user-supplied function, that is, values of `x` for which `f(x) = 0`. Its CustomTkinter interface lets you choose a method, enter parameters, and inspect the estimated root, iteration table, and a graph of the function with the iteration points.

The interface labels are in Indonesian. The method names shown in the application are **Biseksi** (bisection), **Regula Falsi** (false position), **Newton-Raphson**, and **Secant**.

## Features

- Enter a symbolic function of `x`.
- Choose one of four root-finding methods.
- Set an initial point or interval and a tolerance.
- View the estimated root and per-iteration values.
- View the function curve and the method's iteration points in an embedded Matplotlib plot.

## Requirements

- Python 3
- A working desktop display and Tk support (Tkinter is included with many Python distributions; on some Linux distributions it must be installed separately).
- The Python packages `customtkinter`, `matplotlib`, `numpy`, and `sympy`.

Install the dependencies with pip:

```bash
python -m pip install customtkinter matplotlib numpy sympy
```

The checked-in `requirements.txt` currently lists `customtkinter`, `matplotlib`, and `sympyp`. The latter appears to be a misspelling of the package name `sympy`, and `numpy` is also used by the application but is not listed there. The install command above names the packages the code imports directly.

## Run the application

Run the GUI from the repository root so Python can find the solver modules:

```bash
python Norex.py
```

There is no command-line interface. The solver modules can also be imported and called from another Python program; see [Solver modules](#solver-modules).

## Using the GUI

1. Type a function of `x` into **Masukkan Fungsi f(x)**. For example, `x**2 - 2`.
2. Choose a method from **PILIH METODE**.
3. Enter the required starting value(s) and tolerance in the fields that appear.
4. Select **HITUNG**.
5. Read the approximate root under **Penyelesaian**, inspect **DATA ITERASI**, and review the plotted function and iteration points under **GRAFIK**.

Use Python/SymPy expression syntax: write powers with `**` (for example, `x**3 - 2*x - 5`) and use explicit multiplication (for example, `2*x`). The expression must be parseable by SymPy and evaluable as a real number at the points visited by the selected method. The graph is sampled with NumPy over a range based on the iteration points.

### Parameters by method

| GUI method | Required values | How the values are used |
| --- | --- | --- |
| Biseksi | Lower bound `a`, upper bound `b`, tolerance `e` | Repeatedly halves the bracket. The starting endpoints must bracket a root (their function values have opposite signs, or an endpoint is itself a root). |
| Regula Falsi | Lower bound `a`, upper bound `b`, tolerance `e` | Uses a line through the endpoint function values to estimate the next point. The implementation requires a sign-changing interval, or a root at an endpoint. |
| Newton-Raphson | Initial value `a`, tolerance `e` | Uses the derivative of the function and starts from `a`. The `b` field is not used. The derivative must be nonzero at each point where an update is needed. |
| Secant | Two initial values `a` and `b`, tolerance `e` | Uses the last two points to estimate the next point. The implementation checks that the initial function values bracket a root, even though this condition is not generally required by the secant method. |

The tolerance must be positive. In the current implementations, bisection stops when the bracket width is at most `e`. Regula Falsi, Newton-Raphson, and Secant stop when the absolute function value at the latest point is at most `e` (a residual criterion). These are different error measures; the tolerance is not a guaranteed bound on the distance from the reported estimate to the exact root.

The solvers do not impose a maximum iteration count. Choose valid starting values and a suitable tolerance; methods may fail to converge or may encounter a zero denominator/derivative or an expression that cannot be evaluated. A function can have multiple roots, and the result depends on its initial value(s) or interval.

## Solver modules

Each module defines a function that accepts the function as a string and returns `(root, iterations)`, where `root` is the computed estimate and `iterations` is a list of dictionaries. Values in each dictionary are numeric and keyed as shown below. The modules use SymPy to parse and evaluate the expression.

| File | Public function | Parameters | Method |
| --- | --- | --- | --- |
| [`biseksi2.py`](biseksi2.py) | `biseksi(fungsi, a, b, e)` | Expression string, interval endpoints, tolerance | Bisection; iteration records include the updated `a`, `b`, midpoint `x_baru`, `f(x_baru)`, and `eror`. Its `eror` is interval width. |
| [`regulaf1.py`](regulaf1.py) | `regulafalsi(fungsi, a, b, e)` | Expression string, interval endpoints, tolerance | Regula Falsi / false position; records include updated endpoints, estimated point, function value, and residual `eror`. |
| [`newraph1.py`](newraph1.py) | `newraph(fungsi, a, e)` | Expression string, initial point, tolerance | Newton-Raphson; derives `f'(x)` symbolically. Records include `x_baru`, `f(x_baru)`, `f'(x_baru)`, and residual `eror`. |
| [`secant1.py`](secant1.py) | `secant(fungsi, a, b, e)` | Expression string, two initial points, tolerance | Secant; records include `x_baru`, `f(x_baru)`, and residual `eror`. |

For example, a solver can be called directly:

```python
import biseksi2

root, iterations = biseksi2.biseksi("x**2 - 2", 1, 2, 1e-6)
print(root)
print(iterations[-1] if iterations else "The initial endpoint was already a root")
```

The returned history can be empty when an interval endpoint is already an exact root. Newton-Raphson does not perform the same endpoint-root shortcut.

## Project files

- [`Norex.py`](Norex.py) — launches the CustomTkinter window, dispatches input to the selected solver, displays the iteration table, and embeds the Matplotlib graph.
- [`biseksi2.py`](biseksi2.py) — bisection implementation.
- [`regulaf1.py`](regulaf1.py) — Regula Falsi implementation.
- [`newraph1.py`](newraph1.py) — Newton-Raphson implementation.
- [`secant1.py`](secant1.py) — secant implementation.
- [`requirements.txt`](requirements.txt) — dependency list (see the note above about its current contents).

## Notes and limitations

- The GUI catches common input and expression errors and shows an error dialog. Mathematical convergence is not guaranteed for arbitrary functions or starting values.
- The implementation uses exact floating-point comparisons for some checks, such as whether a function value is exactly zero.
- Newton-Raphson can fail when its derivative is zero at an iterate. Regula Falsi and Secant can also encounter a zero denominator for degenerate inputs.
- Iterations have no hard upper limit, so a non-converging case may continue running.
- The graph uses the iteration values to choose a plotting interval and evaluates the function over that interval. Functions with poles, discontinuities, complex values, or numerical overflow may not produce a useful plot.
- The application source contains Indonesian labels and error messages.

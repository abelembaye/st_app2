import streamlit as st
import math
def quadratic_equation_solver(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return None

st.title("Quadratic Equation Solver")

a = st.number_input("Enter the value of coefficient a", value=1.0)
b = st.number_input("Enter the value of coefficient b", value=0.0)
c = st.number_input("Enter the value of coefficient c", value=0.0)

if st.button("Solve"):
    result = quadratic_equation_solver(a, b, c)
    if result is None:
        st.error("The equation has no real roots.")
    elif isinstance(result, tuple):
        st.success(f"The roots are {result[0]} and {result[1]}.")
    else:
        st.success(f"The root is {result}.")

import streamlit as st

def largest_number(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")

    num1 = st.number_input("Enter the first number:", value=0)
    num2 = st.number_input("Enter the second number:", value=0)
    num3 = st.number_input("Enter the third number:", value=0)

    if st.button("Find Largest Number"):
        result = largest_number(num1, num2, num3)
        st.success(f"The largest number is: {result}")

if __name__ == "__main__":
    main()

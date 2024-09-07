import streamlit as st

# Title
st.title("Streamlit Interactive Widget Examples")

# Button
if st.button("Click Me"):
    st.success("Button has been clicked!")
else:
	st.info("Button has not been clicked!")

# Checkbox
checkbox_state = st.checkbox("Check me to enable something")
if checkbox_state:
    st.success("Checkbox is checked!")
else:
	st.info("Checkbox is not checked!")

# Radio button
radio_selection = st.radio("Choose an option:", ["Mango", "Apple", "Banana", "Coconut"])
st.success("You selected: " + radio_selection)

# Selectbox
selectbox_selection = st.selectbox("Choose an item:", ["Mango", "Apple", "Banana", "Coconut"])
st.success("You selected: " + selectbox_selection)

# Multiselect
multiselect_selection = st.multiselect("Choose multiple items:", ["Mango", "Apple", "Banana", "Coconut"])
st.write("You selected: ", multiselect_selection)

# Slider
slider_value = st.slider("Select a value:", min_value=0, max_value=10, value=5, step=1)
st.write("Slider value:", slider_value)

# Select slider
select_slider_value = st.select_slider("Select a value:", options=range(10))
st.write("Selected slider value:", select_slider_value)

select_slider_value = st.select_slider("Select a value:", options=[1, 'ML', 4, 'AI', 5, 6, 3, 2, 'NLP'])
st.write("Selected slider value:", select_slider_value)

import streamlit as st
st.sidebar.image("logo.jpeg", use_column_width=True)
st.sidebar.text("联系我们：")
st.sidebar.text("https://XXXX/")



st.markdown(

    """
<style>
.css-17eq0hr{
    background-color: #182b45!important;
    color: blue!important;
    background-image: blue;

}
.css-j8zjtb{
    font-size:1.0rem;
}
</style>
""",
    unsafe_allow_html=True,
)


x = st.slider('x')

st.write(x, 'squared is', x * x)

import time
import numpy as np
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)
for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)
progress_bar.empty()
st.button("Re-run")
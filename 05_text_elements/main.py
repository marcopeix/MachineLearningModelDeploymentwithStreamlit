import streamlit as st

# Give your app a title
st.title("Your title")

# Header
st.header("Main header")

# Subheader
st.subheader("This is a subheader")

# Markdown
st.markdown("This is markdown **text**")
st.markdown("# Header1")
st.markdown("## Header 2")
st.markdown("### Header 3")

# Caption
st.caption("This is a caption")

# Code block
st.code("""import pandas as pd
pd.read_csv(my_csv_file)
""")

# Preformatted text
st.text("Some text")

# LaTeX
st.latex("x = 2^2")

# Divider
st.text('Text above divider')
st.divider()
st.text('Text below divider')

#st.write
st.write('Some text')
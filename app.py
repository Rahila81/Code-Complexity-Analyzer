import streamlit as st

from analyzer import analyze_code


# --------------------------------
# Page configuration
# --------------------------------

st.set_page_config(
    page_title="Code Complexity Analyzer",
    page_icon="🐛",
    layout="wide"
)


# --------------------------------
# Header
# --------------------------------

st.title("🐛 Code Complexity Analyzer")

st.write(
    "Analyze your source code and get insights about "
    "complexity, loops, conditions and code quality."
)


# --------------------------------
# Language selection
# --------------------------------

language = st.selectbox(
    "Select Programming Language",
    ["Java", "Python", "C"]
)


# --------------------------------
# Code input
# --------------------------------

code = st.text_area(
    "Paste your code here:",
    height=300,
    placeholder="Paste your source code..."
)


# --------------------------------
# Analyze button
# --------------------------------

if st.button("🔍 Analyze Code", use_container_width=True):

    if code.strip() == "":
        st.warning("Please enter some code.")

    else:

        result = analyze_code(code)

        st.success("Code analysis completed!")


        # --------------------------------
        # Main metrics
        # --------------------------------

        st.subheader("📊 Code Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Code Lines",
                result["code_lines"]
            )

        with col2:
            st.metric(
                "Loops",
                result["loops"]
            )

        with col3:
            st.metric(
                "Conditions",
                result["conditions"]
            )

        with col4:
            st.metric(
                "Functions",
                result["functions"]
            )


        # --------------------------------
        # Complexity
        # --------------------------------

        st.subheader("⚡ Complexity Analysis")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### ⏱️ Time Complexity")

            st.info(
                result["time"]
            )

        with col2:

            st.markdown("### 💾 Space Complexity")

            st.info(
                result["space"]
            )


        # --------------------------------
        # Nested loops
        # --------------------------------

        st.subheader("🔄 Loop Analysis")

        st.write(
            f"Maximum nested loop depth: **{result['nested_depth']}**"
        )


        # --------------------------------
        # Explanation
        # --------------------------------

        st.subheader("💡 Explanation")

        st.write(
            result["explanation"]
        )


        # --------------------------------
        # Code quality
        # --------------------------------

        st.subheader("⭐ Code Quality")

        st.progress(
            result["score"] / 100
        )

        st.write(
            f"Estimated Code Quality Score: **{result['score']}/100**"
        )


        # --------------------------------
        # Additional information
        # --------------------------------

        st.subheader("📋 Additional Statistics")

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"Total lines: **{result['total_lines']}**"
            )

        with col2:

            st.write(
                f"Comment lines: **{result['comments']}**"
            )
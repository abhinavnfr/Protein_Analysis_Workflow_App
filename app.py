import streamlit as st
import fetch_fasta_sequence as fs

def main():
    st.title("Protein Sequence Analysis Workflow Application")
    st.write("")
    st.subheader("Step 1: Fetch FASTA sequences from accession numbers")
    import streamlit as st

    st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f5;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    
    # File uploader for accession numbers
    uploaded_file = st.file_uploader("Choose a text file containing accession numbers", type=["txt"])
    
    # Initialize session state to track if the process is in progress
    if "fetching" not in st.session_state:
        st.session_state.fetching = False
    
    if st.button("Fetch FASTA Sequences", disabled=st.session_state.fetching):
        # Set the fetching state to True to disable button and file uploader
        st.session_state.fetching = True
    
        # Fetch the sequences
        output_file = fs.fetch_fasta_main(uploaded_file)
        if output_file:
            # Provide a download link for the user
            with open(output_file, 'rb') as f:
                st.download_button(
                    label="Download Sequences",
                    data=f,
                    file_name='sequences.fasta',
                    mime='text/plain'
                )
    
    # Disable the file uploader if the fetching is in progress
    if st.session_state.fetching:
        st.warning("Fetching in progress. Please wait...")

if __name__ == "__main__":
    main()

import streamlit as st
import fetch_fasta_sequence as fs

def main():
    st.markdown("<h1 style='color: pink;'>Protein Sequence Analysis Workflow Application</h1>", unsafe_allow_html=True)
    st.write("")
    st.subheader("Step 1: Fetch FASTA sequences from accession numbers")
    
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
                if st.download_button(
                    label="Download Sequences",
                    data=f,
                    file_name='sequences.fasta',
                    mime='text/plain'
                ):
            st.session_state.clear()  # Reset session state
            st.session_state.fetching = False  # Ensure fetching state is reset
            st.session_state.uploader = None # Clear the Uploader State
            st.rerun()  # Restart the app to initial state

if __name__ == "__main__":
    main()

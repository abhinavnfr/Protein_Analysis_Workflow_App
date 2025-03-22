import streamlit as st
import fetch_fasta_sequence as fs

def main():
    st.markdown("<h1 style='color: pink;'>Protein Sequence Analysis Workflow Application</h1>", unsafe_allow_html=True)
    st.write("")
    st.subheader("Step 1: Fetch FASTA sequences from accession numbers")
    
    # Initialize session state
    if "fetching" not in st.session_state:
        st.session_state.fetching = False
    if "reset_uploader" not in st.session_state:
        st.session_state.reset_uploader = False

    # File uploader with a key; reset it conditionally
    uploaded_file = st.file_uploader(
        "Choose a text file containing accession numbers", 
        type=["txt"], 
        key="uploader" if not st.session_state.reset_uploader else "uploader_reset"
    )
    
    if st.button("Fetch FASTA Sequences", disabled=st.session_state.fetching):
        # Set fetching state to True
        st.session_state.fetching = True
        
        # Fetch the sequences
        output_file = fs.fetch_fasta_main(uploaded_file)
        if output_file:
            # Provide a download link
            with open(output_file, 'rb') as f:
                st.download_button(
                    label="Download Sequences",
                    data=f,
                    file_name='sequences.fasta',
                    mime='text/plain'
                )
            # Reset state after fetch completes
            st.session_state.fetching = False
            st.session_state.reset_uploader = True  # Signal to reset uploader
            st.rerun()  # Refresh the app
    
    # Reset uploader state after rerun
    if st.session_state.reset_uploader:
        st.session_state.reset_uploader = False  # Reset the flag
        st.rerun()  # Rerun again to stabilize with original key
    
    # Show fetching message only when in progress
    if st.session_state.fetching:
        st.warning("Fetching in progress. Please wait...")

if __name__ == "__main__":
    main()

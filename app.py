import streamlit as st
import fetch_fasta_sequence as fs

def main():
    st.markdown("<h1 style='color: pink;'>Protein Sequence Analysis Workflow Application</h1>", unsafe_allow_html=True)
    st.write("")
    st.subheader("Step 1: Fetch FASTA sequences from accession numbers")
    
    # CHANGE 1: Added key="uploader" to link file uploader to session state
    uploaded_file = st.file_uploader("Choose a text file containing accession numbers", type=["txt"], key="uploader")
    
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
                # CHANGE 2: Removed 'if' condition around st.download_button; it’s now a standalone widget
                st.download_button(
                    label="Download Sequences",
                    data=f,
                    file_name='sequences.fasta',
                    mime='text/plain'
                )
            # CHANGE 3: Moved state reset outside the download button block to execute after fetch
            st.session_state.fetching = False  # Reset fetching state
            # CHANGE 4: Removed st.session_state.clear() and kept targeted reset
            st.rerun()  # Restart the app to initial state
            # CHANGE 5: Added this warning block outside the if condition to show during fetch
    if st.session_state.fetching:
        st.warning("Fetching in progress. Please wait...")

if __name__ == "__main__":
    main()

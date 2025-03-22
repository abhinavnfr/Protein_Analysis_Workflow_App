import streamlit as st
import fetch_fasta_sequence as fs
import os

def main():
    st.markdown("<h1 style='color: pink;'>Protein Sequence Analysis Workflow Application</h1>", unsafe_allow_html=True)
    st.write("")
    st.subheader("Step 1: Fetch FASTA sequences from accession numbers")
    
    # Initialize session state
    if "fetching" not in st.session_state:
        st.session_state.fetching = False

    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a text file containing accession numbers", 
        type=["txt"], 
        key="uploader"
    )
    
    if st.button("Fetch FASTA Sequences", disabled=st.session_state.fetching):
        if uploaded_file is not None:
            st.session_state.fetching = True
            st.write("Starting fetch process...")  # Debug step
            
            # Fetch the sequences
            try:
                output_file = fs.fetch_fasta_main(uploaded_file)
                st.write(f"Output file from fetch_fasta_main: {output_file}")  # Debug step
                
                if output_file:
                    if os.path.exists(output_file):
                        st.write(f"File exists at: {output_file}")  # Debug step
                        with open(output_file, 'rb') as f:
                            st.download_button(
                                label="Download Sequences",
                                data=f,
                                file_name='sequences.fasta',
                                mime='text/plain'
                            )
                        st.success("Sequences fetched successfully!")
                    else:
                        st.error(f"File not found: {output_file}")
                else:
                    st.error("fetch_fasta_main returned None or empty value")
                
                # Reset state
                st.session_state.fetching = False
                st.rerun()  # Only rerun after everything is done
            
            except Exception as e:
                st.error(f"Error in fetch process: {e}")
                st.session_state.fetching = False
        else:
            st.warning("Please upload a file before fetching.")
    
    # Show fetching message
    if st.session_state.fetching:
        st.warning("Fetching in progress. Please wait...")

if __name__ == "__main__":
    main()
